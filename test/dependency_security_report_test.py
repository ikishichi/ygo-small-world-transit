import json

import pytest

from scripts.dependency_security_report import main


@pytest.fixture
def files(tmp_path):
    requirements = tmp_path / "requirements.txt"
    requirements.write_text(
        "requests==2.34.2\nbeautifulsoup4==4.15.0 ; python_version >= '3.12'\n",
        encoding="utf-8",
    )
    report = tmp_path / "trivy.json"
    summary = tmp_path / "summary.md"
    return requirements, report, summary


def write_report(path, results):
    report = {"SchemaVersion": 2, "Results": results}
    path.write_text(json.dumps(report), encoding="utf-8")


def run_report(
    report,
    requirements,
    summary,
    outcome="success",
    filtered_report=None,
    filter_outcome=None,
    ignorefile=None,
):
    args = [
        "--report",
        str(report),
        "--requirements",
        str(requirements),
        "--scan-outcome",
        outcome,
        "--summary",
        str(summary),
    ]
    if filtered_report is not None:
        args.extend(("--filtered-report", str(filtered_report)))
    if filter_outcome is not None:
        args.extend(("--filter-outcome", filter_outcome))
    if ignorefile is not None:
        args.extend(("--ignorefile", str(ignorefile)))
    return main(args)


@pytest.fixture
def filtered_files(files, tmp_path):
    requirements, report, summary = files
    return (
        requirements,
        report,
        tmp_path / "filtered.json",
        tmp_path / ".trivyignore",
        summary,
    )


def make_pip_report(packages, vulnerabilities):
    return [{"Type": "pip", "Packages": packages, "Vulnerabilities": vulnerabilities}]


def write_filter_inputs(
    files, raw_findings, filtered_findings, ignore_text, filtered_packages=None
):
    requirements, report, filtered_report, ignorefile, summary = files
    packages = [
        {"Name": "requests", "Version": "2.34.2"},
        {"Name": "beautifulsoup4", "Version": "4.15.0"},
    ]
    write_report(report, make_pip_report(packages, raw_findings))
    write_report(
        filtered_report,
        make_pip_report(
            filtered_packages if filtered_packages is not None else packages,
            filtered_findings,
        ),
    )
    ignorefile.write_text(ignore_text, encoding="utf-8")
    return requirements, report, filtered_report, ignorefile, summary


def vulnerability(identifier, severity="HIGH", aliases=None):
    result = {
        "PkgName": "requests",
        "InstalledVersion": "2.34.2",
        "VulnerabilityID": identifier,
        "Severity": severity,
        "FixedVersion": "2.34.3",
    }
    if aliases is not None:
        result["Aliases"] = aliases
    return result


def test_writes_severity_counts_and_high_findings(files):
    requirements, report, summary = files
    write_report(
        report,
        [
            {
                "Type": "pip",
                "Packages": [
                    {"Name": "Requests", "Version": "2.34.2"},
                    {"Name": "beautifulsoup4", "Version": "4.15.0"},
                ],
                "Vulnerabilities": [
                    {
                        "PkgName": "requests",
                        "InstalledVersion": "2.34.2",
                        "VulnerabilityID": "GHSA-1234",
                        "Severity": "HIGH",
                        "FixedVersion": "2.34.3",
                    },
                    {
                        "PkgName": "requests",
                        "InstalledVersion": "2.34.2",
                        "VulnerabilityID": "GHSA-5678",
                        "Severity": "UNKNOWN",
                    },
                    {
                        "PkgName": "requests",
                        "InstalledVersion": "2.34.2",
                        "VulnerabilityID": "GHSA-9012",
                        "Severity": "CRITICAL",
                        "FixedVersion": "",
                    },
                ],
            }
        ],
    )

    assert run_report(report, requirements, summary) == 0

    output = summary.read_text(encoding="utf-8")
    assert "2 パッケージ" in output
    assert "| HIGH | 1 |" in output
    assert "| CRITICAL | 1 |" in output
    assert "| UNKNOWN | 1 |" in output
    assert "GHSA-1234" in output
    assert "GHSA-9012" in output
    assert "未公開" in output
    assert "重大度を判定できない脆弱性が **1 件**" in output


def test_escapes_untrusted_high_findings_in_markdown_table(files):
    requirements, report, summary = files
    write_report(
        report,
        [
            {
                "Type": "pip",
                "Packages": [
                    {"Name": "requests", "Version": "2.34.2"},
                    {"Name": "beautifulsoup4", "Version": "4.15.0"},
                ],
                "Vulnerabilities": [
                    {
                        "PkgName": "<img src=x>|[requests](https://example.com)",
                        "InstalledVersion": "2.34.2",
                        "VulnerabilityID": "<script>`alert(1)`</script>",
                        "Severity": "HIGH",
                        "FixedVersion": "2.34.3",
                    }
                ],
            }
        ],
    )

    assert run_report(report, requirements, summary) == 0

    output = summary.read_text(encoding="utf-8")
    assert "&lt;img src=x&gt;&#124;\\[requests\\]\\(https://example.com\\)" in output
    assert "&lt;script&gt;\\`alert\\(1\\)\\`&lt;/script&gt;" in output


@pytest.mark.parametrize(
    "specifier",
    ["requests>=2.34.2", "requests==2.34.*", "requests==2.34.2; "],
)
def test_rejects_unlocked_or_malformed_requirement_specifiers(files, specifier):
    requirements, report, summary = files
    requirements.write_text(specifier + "\n", encoding="utf-8")
    write_report(
        report,
        [{"Type": "pip", "Packages": [{"Name": "requests", "Version": "2.34.2"}]}],
    )

    assert run_report(report, requirements, summary) == 2
    assert "固定形式を解析できない" in summary.read_text(encoding="utf-8")


@pytest.mark.parametrize("outcome", ["failure", "skipped", "cancelled"])
def test_failed_or_skipped_scan_is_reported_as_error(files, outcome, caplog):
    requirements, report, summary = files
    write_report(report, [])

    assert run_report(report, requirements, summary, outcome) == 2
    assert "検査エラー" in summary.read_text(encoding="utf-8")
    assert "脆弱性スキャンに失敗しました" in caplog.text


@pytest.mark.parametrize(
    "results, message",
    [
        ([], "検出結果が空"),
        ([{"Type": "pip", "Packages": []}], "検出結果が空"),
        (
            [{"Type": "pip", "Packages": [{"Name": "requests", "Version": "2.34.2"}]}],
            "一部が検出されていません",
        ),
    ],
)
def test_empty_or_incomplete_results_fail_closed(files, results, message):
    requirements, report, summary = files
    write_report(report, results)

    assert run_report(report, requirements, summary) == 2
    assert message in summary.read_text(encoding="utf-8")


def test_malformed_json_and_missing_report_are_reported(files):
    requirements, report, summary = files
    report.write_text("not json", encoding="utf-8")
    assert run_report(report, requirements, summary) == 2
    assert "検査エラー" in summary.read_text(encoding="utf-8")

    summary.write_text("", encoding="utf-8")
    assert run_report(report.with_name("missing.json"), requirements, summary) == 2
    assert "検査エラー" in summary.read_text(encoding="utf-8")


def test_report_requires_expected_pip_target_not_just_any_target(files):
    requirements, report, summary = files
    write_report(
        report,
        [{"Type": "npm", "Packages": [{"Name": "requests", "Version": "2.34.2"}]}],
    )

    assert run_report(report, requirements, summary) == 2
    assert "検出結果が空" in summary.read_text(encoding="utf-8")

    report.write_text("[]", encoding="utf-8")
    summary.write_text("", encoding="utf-8")
    assert run_report(report, requirements, summary) == 2
    assert "Trivy JSONのルートが" in summary.read_text(encoding="utf-8")


def test_rejects_invalid_json_package_field_types(files):
    requirements, report, summary = files
    write_report(
        report,
        [
            {
                "Type": "pip",
                "Packages": [
                    {"Name": "requests", "Version": "2.34.2"},
                    {"Name": "beautifulsoup4", "Version": "4.15.0"},
                ],
                "Vulnerabilities": [{"PkgName": ["requests"], "Severity": "HIGH"}],
            }
        ],
    )

    assert run_report(report, requirements, summary) == 2
    assert "不正なPkgName" in summary.read_text(encoding="utf-8")


@pytest.mark.parametrize("entries", [{}, "", False, 0])
def test_invalid_empty_vulnerability_data_is_not_treated_as_clean(files, entries):
    requirements, report, summary = files
    write_report(
        report,
        [
            {
                "Type": "pip",
                "Packages": [
                    {"Name": "requests", "Version": "2.34.2"},
                    {"Name": "beautifulsoup4", "Version": "4.15.0"},
                ],
                "Vulnerabilities": entries,
            }
        ],
    )

    assert run_report(report, requirements, summary) == 2
    assert "Vulnerabilitiesが配列ではありません" in summary.read_text(encoding="utf-8")


def test_reports_native_exclusions_and_remaining_high_findings(filtered_files):
    raw = [vulnerability("CVE-2026-10001"), vulnerability("CVE-2026-10002")]
    files = write_filter_inputs(
        filtered_files,
        raw,
        [raw[1]],
        "# temporary exception: waiting for upstream fix\nCVE-2026-10001 exp:2099-12-31\n",
    )

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )

    output = files[4].read_text(encoding="utf-8")
    assert "脆弱性 **2 件** / 一時除外 **1 件** / 判定対象 **1 件**" in output
    assert "| HIGH | 1 |" in output
    assert "CVE-2026-10002" in output
    assert "CVE-2026-10001" in output
    assert "waiting for upstream fix" in output
    assert "2099-12-31" in output


def test_native_filtered_report_is_authoritative_for_expiry(filtered_files):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(
        filtered_files,
        [finding],
        [finding],
        "CVE-2026-10001 exp:2000-01-01\n",
    )

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )

    output = files[4].read_text(encoding="utf-8")
    assert "一時除外 **0 件**" in output
    assert "判定対象 **1 件**" in output
    assert "CVE-2026-10001" in output


def test_high_excluded_message_describes_remaining_scope(filtered_files):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(
        filtered_files,
        [finding],
        [],
        "CVE-2026-10001\n",
    )

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )

    output = files[4].read_text(encoding="utf-8")
    assert "除外後の判定対象にHigh・Criticalの脆弱性はありません" in output
    assert "一時除外 **1 件**" in output


def test_empty_ignorefile_and_unexpiring_entry(filtered_files):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(filtered_files, [finding], [finding], "\n# no rules\n")

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )

    files = write_filter_inputs(
        filtered_files,
        [finding],
        [],
        "CVE-2026-10001\n",
    )
    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )
    output = files[4].read_text(encoding="utf-8")
    assert "未記載" in output
    assert "期限なし" in output


@pytest.mark.parametrize(
    "ignore_text, message",
    [
        ("CVE-2026-10001 typo:2099-01-01\n", "不明な形式またはオプション"),
        ("CVE-2026-10001 exp:2026-02-30\n", "無効な期限"),
        ("CVE-2026-10001\nCVE-2026-10001\n", "重複しています"),
    ],
)
def test_invalid_ignore_entries_fail_closed(filtered_files, ignore_text, message):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(filtered_files, [finding], [], ignore_text)

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 2
    )
    assert message in files[4].read_text(encoding="utf-8")


def test_filtered_report_must_only_remove_configured_findings(filtered_files):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(filtered_files, [finding], [], "\n")

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 2
    )
    assert "理由なく消えた" in files[4].read_text(encoding="utf-8")

    write_report(
        files[2],
        make_pip_report(
            [
                {"Name": "requests", "Version": "2.34.2"},
                {"Name": "beautifulsoup4", "Version": "4.15.0"},
            ],
            [finding, vulnerability("CVE-2026-10002")],
        ),
    )
    files[4].write_text("", encoding="utf-8")
    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 2
    )
    assert "にない脆弱性があります" in files[4].read_text(encoding="utf-8")


def test_filtered_report_packages_must_match_raw_report(filtered_files):
    packages = [
        {"Name": "requests", "Version": "2.34.2"},
        {"Name": "beautifulsoup4", "Version": "4.15.0"},
    ]
    files = write_filter_inputs(
        filtered_files,
        [],
        [],
        "",
        filtered_packages=[*packages, {"Name": "extra", "Version": "1.0"}],
    )

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 2
    )
    assert "パッケージ検出結果が一致しません" in files[4].read_text(encoding="utf-8")


def test_filter_failure_and_partial_arguments_fail_closed(filtered_files):
    requirements, report, filtered_report, ignorefile, summary = filtered_files
    packages = [
        {"Name": "requests", "Version": "2.34.2"},
        {"Name": "beautifulsoup4", "Version": "4.15.0"},
    ]
    write_report(report, make_pip_report(packages, []))
    write_report(filtered_report, make_pip_report(packages, []))
    ignorefile.write_text("", encoding="utf-8")

    assert (
        run_report(
            report,
            requirements,
            summary,
            filtered_report=filtered_report,
            filter_outcome="failure",
            ignorefile=ignorefile,
        )
        == 2
    )
    assert "除外処理が完了しませんでした" in summary.read_text(encoding="utf-8")

    summary.write_text("", encoding="utf-8")
    assert (
        run_report(
            report,
            requirements,
            summary,
            filtered_report=filtered_report,
        )
        == 2
    )
    assert "すべて指定してください" in summary.read_text(encoding="utf-8")


def test_escapes_ignore_reasons_and_filter_metadata(filtered_files):
    finding = vulnerability("CVE-2026-10001")
    files = write_filter_inputs(
        filtered_files,
        [finding],
        [],
        "# [reason](https://example.com) *unsafe* `code`\nCVE-2026-10001\n",
    )

    assert (
        run_report(
            files[1],
            files[0],
            files[4],
            filtered_report=files[2],
            filter_outcome="success",
            ignorefile=files[3],
        )
        == 0
    )

    output = files[4].read_text(encoding="utf-8")
    assert "\\[reason\\]\\(https://example.com\\)" in output
    assert "\\*unsafe\\*" in output
    assert "\\`code\\`" in output
