# ygo-small-world-transit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ygo-small-world-transit.streamlit.app/?lang=en)

This app finds [**Small World**](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=en) search routes from a public deck on [Yu-Gi-Oh! Neuron](https://www.db.yugioh-card.com/yugiohdb/?request_locale=en).

<div align="center">

[日本語](README.md) | **English** | [한국어](README.ko.md) | [简体中文](README.zh-CN.md)

</div>

## How to use

See the [usage video on YouTube](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s).

1. Paste the public deck URL shown at the top of its deck page and select **Load deck**, or select **Try a sample** on the initial screen.
2. Select a monster to reveal from your hand. Optionally select a destination. Leave it empty to find every reachable destination in the loaded deck.
3. Select **Find routes**. Results are grouped by destination. Use **Sort by bridge** to group them by bridge instead.
4. Open **Show matching properties** to see each hand → bridge → destination route and the matching property at each step.

After loading, use **Change deck** to open the URL form and load another deck or refresh the current one. Bookmark the page after loading to load the same deck next time. Search selections and results are not saved.

## Language

[日本語](https://ygo-small-world-transit.streamlit.app/?lang=ja) / [English](https://ygo-small-world-transit.streamlit.app/?lang=en) / [한국어](https://ygo-small-world-transit.streamlit.app/?lang=ko) / [简体中文](https://ygo-small-world-transit.streamlit.app/?lang=zh-CN)

Japanese is the default. Use the globe menu above the app title to change the display language. The display language and deck data language are independent. Deck data uses the language in `request_locale`, or the display language when it is omitted. The database locale for Simplified Chinese is `cn`.

## Run locally

Python 3.12 or later is required.

1. Clone this repository and change to its root directory.
2. Install the required packages.

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the app.

   ```bash
   python -m streamlit run ./src/ui.py
   ```

Use a virtual environment to avoid conflicts with other Python projects. If the `streamlit` command is unavailable, run it with `python -m streamlit`. If Python reports `No module named streamlit`, install the requirements using the same Python interpreter used to launch the app.

## Development

Run tests from the project root.

```bash
python -m pytest
```

See the [design document](docs/ygo-small-world-transit.md) for requirements and architecture.

### Managing dependencies

Declare dependencies in `requirements.in`. `requirements.txt` is generated with pinned direct and transitive versions. Commit both files and install from `requirements.txt`. The project pins `uv` in `requirements-tools.txt` to generate the lock file.

```bash
python -m pip install -r requirements-tools.txt
python -m uv pip compile requirements.in --output-file requirements.txt
```

Edit `requirements.in` when changing dependencies, then regenerate `requirements.txt`. Do not edit the generated file directly. Add `--upgrade-package PACKAGE` to update one package within the declared range, or `--upgrade` to update all packages.

```bash
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade-package streamlit
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade
```

CI checks that regenerating the lock file produces no changes before running tests.

### Dependency security scans

The [Dependency security workflow](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/dependency-security.yml) scans `requirements.txt` with Trivy every Saturday and when a pull request targeting `main` is opened, updated, or reopened. It can also be run manually. The check fails when High or Critical findings remain after exclusions, when the database cannot be fetched, or when the report or exclusions are invalid. Findings without a published fix are included.

The workflow summary reports detected, temporarily excluded, and evaluated findings, including High and Critical findings that block the check and reasons and expiry dates for exclusions. Scan errors include database download failures, missing or malformed reports, invalid exclusions, and fixed packages that Trivy did not detect. The `dependency-security-report` artifact stores the raw and filtered JSON reports, summary, scanned lock file, and exclusions for 14 days. To temporarily exclude a vulnerability, add its ID to `.trivyignore` and remove it after upgrading to a fixed version. Findings before exclusions remain in the raw JSON report.

## Keeping the hosted app awake

The [Keep Streamlit app awake workflow](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/keep_alive.yml) opens the hosted app with Playwright Chromium every three hours. It uses the `ja-JP` locale. If a sleep screen appears, it dismisses it and checks that the title, editable deck URL field, and enabled **デッキ取得** button appear. It does not load a deck or run a search. This scheduled workflow does not run on forks.

### Checking recovery and handling failures

The workflow waits up to 120 seconds for recovery and retries once. Each page navigation can take up to 30 additional seconds. If recovery fails, the workflow fails and stores screenshots and each iframe's HTML as artifacts for seven days. Review the logs and artifacts for network issues, Streamlit outages, or changes to the page and button. This check verifies the UI only. It does not test deck loading or search behavior.

GitHub [scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) can be delayed or skipped, and are automatically disabled after 60 days of inactivity in public repositories. Re-enable the workflow from the Actions page if needed. [Streamlit Community Cloud hibernation](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation) behavior and the interface may change, so continuous availability is not guaranteed.

### Testing the keep-alive script locally

Install the optional test dependency and Chromium as needed.

```bash
python -m pip install playwright==1.63.0
python -m playwright install chromium
python scripts/keep_alive.py
python -m pytest test/keep_alive_test.py
```

`python scripts/keep_alive.py` checks the hosted app. The test runs Chromium against a local reproduction and does not contact the hosted app. It is skipped when Playwright is not installed.

## License

The code in this repository is released under the MIT License. See [LICENSE.txt](LICENSE.txt).
