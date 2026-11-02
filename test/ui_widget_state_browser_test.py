"""AppTestでは検出できないブラウザーの選択表示と結果の同期を検証する。"""

import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

import pytest

pytest.importorskip("playwright.sync_api")

from playwright.sync_api import expect, sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "en": {
        "search": "Find routes",
        "results": "Search results",
        "change": "Change deck",
        "load": "Load deck",
        "transit": "Sort by bridge",
        "destination": "Sort by destination",
        "group_transit": "Bridge: Mathmech Sigma",
        "group_destination": "Destination: Dotscaper",
    },
    "ja": {
        "search": "経路を検索",
        "results": "検索結果",
        "change": "デッキを変更",
        "load": "デッキ取得",
        "transit": "経由でソート",
        "destination": "サーチ先でソート",
        "group_transit": "経由： Mathmech Sigma",
        "group_destination": "サーチ先： Dotscaper",
    },
}


@pytest.fixture(scope="module")
def browser_app(tmp_path_factory):
    """外部HTTPをモックしたStreamlitとChromiumを起動・終了する。"""
    artifacts = tmp_path_factory.mktemp("widget-state-server")
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    url = f"http://127.0.0.1:{port}/"
    with (artifacts / "streamlit.log").open("w", encoding="utf-8") as log:
        server = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(PROJECT_ROOT / "test" / "fixtures" / "widget_state_app.py"),
                "--server.address=127.0.0.1",
                f"--server.port={port}",
                "--server.headless=true",
                "--browser.gatherUsageStats=false",
            ],
            cwd=PROJECT_ROOT,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        try:
            deadline = time.monotonic() + 30
            while True:
                if server.poll() is not None:
                    pytest.fail(
                        (artifacts / "streamlit.log").read_text(encoding="utf-8")
                    )
                try:
                    with urlopen(url + "_stcore/health", timeout=1):
                        break
                except (OSError, URLError):
                    if time.monotonic() >= deadline:
                        pytest.fail("Streamlitの起動がタイムアウトしました")
                    time.sleep(0.1)
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                try:
                    yield browser, url
                finally:
                    browser.close()
        finally:
            server.terminate()
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait(timeout=10)


@pytest.fixture
def page(browser_app):
    browser, _ = browser_app
    context = browser.new_context(locale="ja-JP")
    try:
        yield context.new_page()
    finally:
        context.close()


def load_and_search(page, url, language):
    labels = LABELS[language]
    page.goto(url + f"?lang={language}&cgid=A&dno=1&request_locale=en")
    page.get_by_role("button", name=labels["change"], exact=True).wait_for()
    for index, card in enumerate(("Mulcharmy Fuwalos", "Dotscaper")):
        page.get_by_role("combobox").nth(index).click()
        page.get_by_role("option", name=card, exact=True).click()
    page.get_by_role("button", name=labels["search"], exact=True).click()
    page.get_by_role("heading", name=labels["results"], exact=True).wait_for()


@pytest.mark.parametrize("language", ["en", "ja"])
@pytest.mark.parametrize("sort", ["transit", "destination"])
def test_language_round_trip_preserves_sort_display_and_grouping(
    browser_app, page, language, sort
):
    _, url = browser_app
    load_and_search(page, url, language)
    page.get_by_text(LABELS[language][sort], exact=True).click()
    expect(page.get_by_label(LABELS[language][sort], exact=True)).to_be_checked()

    for target in ("ja" if language == "en" else "en", language):
        expect(page.get_by_test_id("stStatusWidget")).not_to_be_visible()
        language_control = page.locator(".st-key-ui_language_menu")
        language_control.scroll_into_view_if_needed()
        expect(language_control).to_be_in_viewport(ratio=1)
        language_control.get_by_role("button").click()
        current_label = "English" if target == "ja" else "日本語"
        expect(
            page.get_by_role("menuitem", name=current_label, exact=True).locator("strong")
        ).to_have_text(current_label)
        page.get_by_role(
            "menuitem", name="日本語" if target == "ja" else "English", exact=True
        ).click()
        expect(language_control.get_by_role("button")).to_contain_text(
            "日本語" if target == "ja" else "English"
        )
        labels = LABELS[target]
        expect(page.get_by_label(labels[sort], exact=True)).to_be_checked()
        expect(page.get_by_text(labels[f"group_{sort}"], exact=True)).to_be_visible()
        summaries = page.locator(
            '[data-testid="stMarkdownContainer"]'
        ).all_text_contents()
        # グループ見出しと候補行の順序も、選択したソートに従う。
        bridge_index = summaries.index(labels["group_transit"])
        destination_index = summaries.index(labels["group_destination"])
        assert (bridge_index < destination_index) == (sort == "transit")
        expect(page.get_by_role("combobox").nth(0)).to_have_value("Mulcharmy Fuwalos")
        expect(page.get_by_role("combobox").nth(1)).to_have_value("Dotscaper")
        expect(page.get_by_text("The widget with key", exact=False)).to_have_count(0)


@pytest.mark.parametrize("language", ["en", "ja"])
def test_refresh_same_deck_clears_browser_selections(browser_app, page, language):
    _, url = browser_app
    load_and_search(page, url, language)
    labels = LABELS[language]
    page.get_by_role("button", name=labels["change"], exact=True).click()
    page.get_by_role("button", name=labels["load"], exact=True).click()
    expect(
        page.get_by_role("button", name=labels["change"], exact=True)
    ).to_be_visible()
    for index in (0, 1):
        expect(page.get_by_role("combobox").nth(index)).to_have_value("")
    expect(
        page.get_by_role("heading", name=labels["results"], exact=True)
    ).to_have_count(0)
