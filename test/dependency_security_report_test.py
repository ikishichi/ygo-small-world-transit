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


def run_report(report, requirements, summary, outcome="success"):
    return main(
        [
            "--report",
            str(report),
            "--requirements",
            str(requirements),
            "--scan-outcome",
            outcome,
            "--summary",
            str(summary),
        ]
    )


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
            "ありません",
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
