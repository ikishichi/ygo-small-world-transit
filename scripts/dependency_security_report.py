"""Write a concise GitHub Actions summary for a Trivy dependency scan."""

import argparse
import html
import json
import logging
import re
import sys
from collections import Counter
from pathlib import Path

SEVERITIES = ("CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN")
LOGGER = logging.getLogger(__name__)
REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*==\s*"
    r"([A-Za-z0-9][A-Za-z0-9.!+_-]*)"
    r"(?:\s*;\s*(?P<marker>[^#\r\n]*))?\s*(?:#.*)?$"
)
MARKDOWN_SPECIALS = re.compile(r"([\\`*_{}\[\]()!#>])")


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
            findings.append(finding)
    return packages, findings


def escape_cell(value):
    """Escape untrusted package/advisory data for a GitHub Markdown table."""
    value = str(value).replace("\r", " ").replace("\n", " ")
    value = html.escape(value, quote=True)
    return MARKDOWN_SPECIALS.sub(r"\\\1", value).replace("|", "&#124;")


def build_summary(results, requirements):
    packages, findings = collect_packages(results)
    if not packages:
        raise ValueError("Trivyのpipパッケージ検出結果が空です")

    missing = requirements - packages
    if missing:
        names = ", ".join(f"{name}=={version}" for name, version in sorted(missing))
        raise ValueError(f"固定依存関係の一部がスキャン結果にありません: {names}")

    normalized_findings = []
    counts = Counter()
    for finding in findings:
        severity = str(finding.get("Severity", "UNKNOWN")).upper()
        if severity not in SEVERITIES:
            severity = "UNKNOWN"
        normalized = {
            "name": finding.get("PkgName") or "不明",
            "version": finding.get("InstalledVersion") or "不明",
            "id": finding.get("VulnerabilityID") or "不明",
            "severity": severity,
            "fixed": finding.get("FixedVersion") or "未公開",
        }
        normalized_findings.append(normalized)
        counts[severity] += 1

    lines = [
        "## 依存パッケージの脆弱性スキャン",
        "",
        f"固定依存関係 **{len(packages)} パッケージ**を検査しました。検出された脆弱性は **{len(normalized_findings)} 件**です。",
        "",
        "| 重大度 | 件数 |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {severity} | {counts[severity]} |" for severity in SEVERITIES)

    high_findings = [
        item for item in normalized_findings if item["severity"] in ("CRITICAL", "HIGH")
    ]
    lines.extend(["", "### High・Critical"])
    if high_findings:
        lines.extend(
            [
                "",
                "| パッケージ | 使用版 | 脆弱性ID | 重大度 | 修正版 |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        high_findings.sort(
            key=lambda item: (
                SEVERITIES.index(item["severity"]),
                item["name"].lower(),
                item["id"],
            )
        )
        for item in high_findings:
            cells = (
                item["name"],
                item["version"],
                item["id"],
                item["severity"],
                item["fixed"],
            )
            lines.append("| " + " | ".join(escape_cell(cell) for cell in cells) + " |")
    else:
        lines.extend(["", "High・Criticalの脆弱性は検出されませんでした。"])

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
        summary = build_summary(results, read_requirements(args.requirements))
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
