"""Write a concise GitHub Actions summary for a Trivy dependency scan."""

import argparse
import html
import json
import logging
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

SEVERITIES = ("CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN")
LOGGER = logging.getLogger(__name__)
REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*==\s*"
    r"([A-Za-z0-9][A-Za-z0-9.!+_-]*)"
    r"(?:\s*;\s*(?P<marker>[^#\r\n]*))?\s*(?:#.*)?$"
)
MARKDOWN_SPECIALS = re.compile(r"([\\`*_{}\[\]()!#>])")
IGNORE_ENTRY_PATTERN = re.compile(
    r"(?P<id>[A-Za-z0-9][A-Za-z0-9._:-]*)(?:[ \t]+exp:(?P<expiry>\S+))?"
)


def normalize_name(name):
    """Normalize a Python distribution name according to PEP 503."""
    return re.sub(r"[-_.]+", "-", name).lower()


def read_requirements(path):
    """Return normalized names and versions pinned with ==."""
    pinned = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = REQUIREMENT_PATTERN.fullmatch(line)
        if (
            not match
            or "*" in match.group(2)
            or (match.group("marker") is not None and not match.group("marker").strip())
        ):
            raise ValueError(f"固定形式を解析できない依存指定があります: {stripped}")
        pinned.add((normalize_name(match.group(1)), match.group(2)))
    if not pinned:
        raise ValueError("固定バージョンを含むrequirementsファイルが空です")
    return pinned


def collect_packages(results):
    packages = set()
    findings = []
    for result in results:
        if not isinstance(result, dict):
            raise TypeError("TrivyのResultsに不正な項目があります")
        target_type = result.get("Type", "")
        if not isinstance(target_type, str):
            raise TypeError("TrivyのTypeが文字列ではありません")
        if target_type.lower() != "pip":
            continue
        package_entries = result.get("Packages")
        if package_entries is None:
            package_entries = []
        if not isinstance(package_entries, list):
            raise TypeError("TrivyのPackagesが配列ではありません")
        for package in package_entries:
            if not isinstance(package, dict):
                raise TypeError("TrivyのPackagesに不正な項目があります")
            name = package.get("Name")
            version = package.get("Version")
            if (
                not isinstance(name, str)
                or not name
                or not isinstance(version, str)
                or not version
            ):
                raise TypeError("Trivyのパッケージ名またはバージョンが不正です")
            packages.add((normalize_name(name), version))
        vulnerability_entries = result.get("Vulnerabilities")
        if vulnerability_entries is None:
            vulnerability_entries = []
        if not isinstance(vulnerability_entries, list):
            raise TypeError("TrivyのVulnerabilitiesが配列ではありません")
        for finding in vulnerability_entries:
            if not isinstance(finding, dict):
                raise TypeError("TrivyのVulnerabilitiesに不正な項目があります")
            for field in (
                "PkgName",
                "InstalledVersion",
                "VulnerabilityID",
                "Severity",
                "FixedVersion",
            ):
                value = finding.get(field)
                if value is not None and not isinstance(value, str):
                    raise TypeError(f"TrivyのVulnerabilitiesに不正な{field}があります")
            aliases = finding.get("Aliases")
            if aliases is not None and (
                not isinstance(aliases, list)
                or any(not isinstance(alias, str) for alias in aliases)
            ):
                raise TypeError("TrivyのAliasesが文字列配列ではありません")
            findings.append(finding)
    return packages, findings


def escape_cell(value):
    """Escape untrusted package/advisory data for a GitHub Markdown table."""
    value = str(value).replace("\r", " ").replace("\n", " ")
    value = html.escape(value, quote=True)
    return MARKDOWN_SPECIALS.sub(r"\\\1", value).replace("|", "&#124;")


def read_ignorefile(path):
    """Read ignore identifiers and their display-only reason and expiry metadata."""
    entries = {}
    pending_comments = []
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            pending_comments.clear()
            continue
        if stripped.startswith("#"):
            pending_comments.append(stripped[1:].strip())
            continue

        match = IGNORE_ENTRY_PATTERN.fullmatch(stripped)
        if not match:
            raise ValueError(
                f".trivyignoreの{line_number}行目に不明な形式またはオプションがあります"
            )
        identifier = match.group("id")
        if identifier in entries:
            raise ValueError(f".trivyignoreで脆弱性IDが重複しています: {identifier}")
        expiry = match.group("expiry")
        if expiry:
            try:
                if date.fromisoformat(expiry).isoformat() != expiry:
                    raise ValueError
            except ValueError:
                raise ValueError(
                    f".trivyignoreの{line_number}行目に無効な期限があります: {expiry}"
                ) from None
        entries[identifier] = {
            "reason": " ".join(comment for comment in pending_comments if comment)
            or "未記載",
            "expiry": expiry or "期限なし",
        }
        pending_comments.clear()
    return entries


def finding_key(finding):
    """Return a stable key for comparing one Trivy finding across native reports."""
    name = finding.get("PkgName")
    version = finding.get("InstalledVersion")
    identifier = finding.get("VulnerabilityID")
    if (
        not isinstance(name, str)
        or not name
        or not isinstance(version, str)
        or not version
    ):
        raise ValueError("Trivyの脆弱性結果にパッケージ名またはバージョンがありません")
    if not isinstance(identifier, str) or not identifier:
        raise ValueError("Trivyの脆弱性結果にVulnerabilityIDがありません")
    return normalize_name(name), version, identifier


def finding_identifiers(finding):
    identifiers = {finding_key(finding)[2]}
    aliases = finding.get("Aliases")
    if aliases is not None:
        if not isinstance(aliases, list) or any(
            not isinstance(alias, str) for alias in aliases
        ):
            raise TypeError("TrivyのAliasesが文字列配列ではありません")
        identifiers.update(alias for alias in aliases if alias)
    return identifiers


def index_findings(findings, report_name):
    indexed = {}
    for finding in findings:
        key = finding_key(finding)
        if key in indexed:
            raise ValueError(f"{report_name}に脆弱性キーが重複しています: {key[2]}")
        indexed[key] = finding
    return indexed


def compare_findings(raw_findings, filtered_findings, ignore_entries):
    raw_by_key = index_findings(raw_findings, "除外前レポート")
    filtered_by_key = index_findings(filtered_findings, "除外後レポート")
    unexpected = filtered_by_key.keys() - raw_by_key.keys()
    if unexpected:
        raise ValueError(
            "除外後レポートに除外前レポートにない脆弱性があります: "
            f"{next(iter(unexpected))[2]}"
        )

    excluded = []
    for key, finding in raw_by_key.items():
        if key in filtered_by_key:
            continue
        configured_ids = finding_identifiers(finding) & ignore_entries.keys()
        if len(configured_ids) != 1:
            raise ValueError(
                f"除外後レポートから理由なく消えた脆弱性があります: {key[2]}"
            )
        identifier = configured_ids.pop()
        excluded.append(
            {**finding, "IgnoreID": identifier, **ignore_entries[identifier]}
        )
    return excluded


def validate_packages(packages, requirements, report_name):
    if not packages:
        raise ValueError(f"{report_name}のTrivy pipパッケージ検出結果が空です")
    missing = requirements - packages
    if missing:
        names = ", ".join(f"{name}=={version}" for name, version in sorted(missing))
        raise ValueError(
            f"{report_name}で固定依存関係の一部が検出されていません: {names}"
        )


def finding_display(finding):
    severity = str(finding.get("Severity") or "UNKNOWN").upper()
    if severity not in SEVERITIES:
        severity = "UNKNOWN"
    return {
        "name": finding.get("PkgName") or "不明",
        "version": finding.get("InstalledVersion") or "不明",
        "id": finding.get("IgnoreID") or finding.get("VulnerabilityID") or "不明",
        "severity": severity,
        "fixed": finding.get("FixedVersion") or "未公開",
    }


def append_finding_table(lines, title, findings, extra_columns=()):
    lines.extend(["", f"### {title}"])
    if not findings:
        lines.extend(["", "該当する脆弱性はありません。"])
        return
    extra_headers = {"reason": "理由", "expiry": "期限"}
    headers = (
        "パッケージ",
        "使用版",
        "脆弱性ID",
        "重大度",
        "修正版",
        *(extra_headers[column] for column in extra_columns),
    )
    lines.extend(
        [
            "",
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
        ]
    )
    for finding in findings:
        cells = [
            finding["name"],
            finding["version"],
            finding["id"],
            finding["severity"],
            finding["fixed"],
        ]
        cells.extend(finding[column] for column in extra_columns)
        lines.append("| " + " | ".join(escape_cell(cell) for cell in cells) + " |")


def build_summary(
    raw_results, requirements, filtered_results=None, ignore_entries=None
):
    raw_packages, raw_findings = collect_packages(raw_results)
    validate_packages(raw_packages, requirements, "除外前レポート")
    if filtered_results is None:
        filtered_findings = raw_findings
        excluded = []
    else:
        filtered_packages, filtered_findings = collect_packages(filtered_results)
        validate_packages(filtered_packages, requirements, "除外後レポート")
        if filtered_packages != raw_packages:
            raise ValueError("除外前後のパッケージ検出結果が一致しません")
        excluded = compare_findings(
            raw_findings, filtered_findings, ignore_entries or {}
        )

    normalized_findings = [finding_display(finding) for finding in filtered_findings]
    counts = Counter(item["severity"] for item in normalized_findings)
    normalized_excluded = []
    for finding in excluded:
        item = finding_display(finding)
        item["reason"] = finding["reason"]
        item["expiry"] = finding["expiry"]
        normalized_excluded.append(item)

    total_count = len(raw_findings)
    target_count = len(filtered_findings)

    lines = [
        "## 依存パッケージの脆弱性スキャン",
        "",
        f"固定依存関係 **{len(raw_packages)} パッケージ**を検査しました。",
        f"脆弱性 **{total_count} 件** / 一時除外 **{len(normalized_excluded)} 件** / 判定対象 **{target_count} 件**",
        "",
        "| 判定対象の重大度 | 件数 |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {severity} | {counts[severity]} |" for severity in SEVERITIES)

    high_findings = sorted(
        (
            item
            for item in normalized_findings
            if item["severity"] in ("CRITICAL", "HIGH")
        ),
        key=lambda item: (
            SEVERITIES.index(item["severity"]),
            item["name"].lower(),
            item["id"],
        ),
    )
    if not high_findings:
        lines.extend(["", "除外後の判定対象にHigh・Criticalの脆弱性はありません。"])
    else:
        append_finding_table(lines, "判定対象のHigh・Critical", high_findings)

    append_finding_table(
        lines,
        "一時除外した脆弱性",
        sorted(
            normalized_excluded, key=lambda item: (item["name"].lower(), item["id"])
        ),
        extra_columns=("reason", "expiry"),
    )

    if counts["UNKNOWN"]:
        lines.extend(
            [
                "",
                (
                    f"⚠️ 重大度を判定できない脆弱性が **{counts['UNKNOWN']} 件**あります。"
                    "詳細はスキャンレポートを確認してください。"
                ),
            ]
        )
    return "\n".join(lines) + "\n"


def append_summary(path, text):
    summary_path = Path(path)
    with summary_path.open("a", encoding="utf-8", newline="\n") as summary_file:
        summary_file.write(text)


def error_summary(message):
    return "\n".join(
        (
            "## 依存パッケージの脆弱性スキャン",
            "",
            f"❌ **検査エラー:** {escape_cell(message)}",
            "",
        )
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--requirements", required=True, type=Path)
    parser.add_argument(
        "--scan-outcome",
        required=True,
        choices=("success", "failure", "skipped", "cancelled"),
    )
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--filtered-report", type=Path)
    parser.add_argument(
        "--filter-outcome",
        choices=("success", "failure", "skipped", "cancelled"),
    )
    parser.add_argument("--ignorefile", type=Path)
    args = parser.parse_args(argv)

    try:
        if args.scan_outcome != "success":
            raise ValueError(
                f"Trivyスキャンが完了しませんでした（{args.scan_outcome}）"
            )
        report = json.loads(args.report.read_text(encoding="utf-8"))
        if not isinstance(report, dict):
            raise TypeError("Trivy JSONのルートがオブジェクトではありません")
        results = report.get("Results")
        if not isinstance(results, list):
            raise TypeError("Trivy JSONにResults配列がありません")
        filter_arguments = (
            args.filtered_report is not None,
            args.filter_outcome is not None,
            args.ignorefile is not None,
        )
        if any(filter_arguments) and not all(filter_arguments):
            raise ValueError(
                "filtered-report、filter-outcome、ignorefileはすべて指定してください"
            )

        filtered_results = None
        ignore_entries = None
        if args.filtered_report is not None:
            if args.filter_outcome != "success":
                raise ValueError(
                    f"Trivy除外処理が完了しませんでした（{args.filter_outcome}）"
                )
            filtered_report = json.loads(
                args.filtered_report.read_text(encoding="utf-8")
            )
            if not isinstance(filtered_report, dict) or not isinstance(
                filtered_report.get("Results"), list
            ):
                raise TypeError("Trivyの除外後JSONにResults配列がありません")
            filtered_results = filtered_report["Results"]
            ignore_entries = read_ignorefile(args.ignorefile)
        summary = build_summary(
            results,
            read_requirements(args.requirements),
            filtered_results,
            ignore_entries,
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        TypeError,
    ) as error:
        message = str(error)
        LOGGER.error("依存パッケージの脆弱性スキャンに失敗しました: %s", message)
        try:
            append_summary(args.summary, error_summary(message))
        except OSError:
            LOGGER.exception("GitHub Actions Summaryへ検査エラーを書き込めませんでした")
        return 2

    try:
        append_summary(args.summary, summary)
    except OSError as error:
        LOGGER.error(
            "GitHub Actions Summaryへ検査結果を書き込めませんでした: %s", error
        )
        return 2
    return 0


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr
    )
    sys.exit(main())
