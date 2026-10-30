"""Chromium内で画面と通信障害を再現する。外部サービスには接続しない。"""

import asyncio
from pathlib import Path

import pytest

pytest.importorskip("playwright.async_api")

from playwright.async_api import Browser, async_playwright
from streamlit.testing.v1 import AppTest

from scripts.keep_alive import (
    APP_TITLE,
    DECK_URL_LABEL,
    WAKE_BUTTON,
    run,
    wait_until_ready,
)

READY_HTML = (
    f"<h1>{APP_TITLE}</h1>"
    f"<label>{DECK_URL_LABEL}<input></label>"
    "<button>デッキ取得</button>"
)
TEST_URL = "https://keep-alive.test/"


def test_deck_url_label_matches_actual_ui(monkeypatch):
    """起動確認に使うラベルが実際のUIと一致することを確認する。"""
    project_root = Path(__file__).resolve().parents[1]
    monkeypatch.syspath_prepend(str(project_root / "src"))
    app = AppTest.from_file(str(project_root / "src" / "ui.py")).run(timeout=10)

    assert not app.exception
    assert app.text_input[0].label == DECK_URL_LABEL


def test_waits_for_iframe_after_wake():
    async def check():
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            try:
                page = await browser.new_page()
                await page.set_content(f"<button>{WAKE_BUTTON}</button>")
                await page.evaluate(
                    """html => {
                        document.querySelector('button').onclick = () => {
                            document.querySelector('button').remove();
                            setTimeout(() => {
                                const frame = document.createElement('iframe');
                                frame.srcdoc = html;
                                document.body.append(frame);
                            }, 50);
                        };
                    }""",
                    READY_HTML,
                )
                assert await wait_until_ready(page, timeout_seconds=5) is True
            finally:
                await browser.close()

    asyncio.run(check())


@pytest.mark.parametrize(
    "html",
    [
        "<html><body>HTTP 200の外枠だけ</body></html>",
        READY_HTML.replace("<input>", "<input disabled>"),
        READY_HTML.replace("<input>", "<input readonly>"),
        READY_HTML.replace("<button>", "<button disabled>"),
        READY_HTML.replace(f"<h1>{APP_TITLE}</h1>", ""),
        f"<button>{WAKE_BUTTON}</button>",
    ],
)
def test_incomplete_ui_times_out(html):
    async def check():
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            try:
                page = await browser.new_page()
                await page.set_content(html)
                with pytest.raises(TimeoutError):
                    await wait_until_ready(page, timeout_seconds=0.2)
            finally:
                await browser.close()

    asyncio.run(check())


@pytest.mark.parametrize("scenario", ["ready", "retry", "shell", "network"])
def test_run_retries_and_reports_failure(mocker, tmp_path, scenario):
    attempts = []
    original_new_context = Browser.new_context

    async def new_context(browser, **kwargs):
        assert kwargs["locale"] == "ja-JP"
        context = await original_new_context(browser, **kwargs)

        async def respond(route):
            attempts.append(route.request.url)
            if scenario == "network":
                await route.abort("failed")
            else:
                html = READY_HTML
                if scenario == "shell" or (scenario == "retry" and len(attempts) == 1):
                    html = "<html><body>Loading</body></html>"
                await route.fulfill(
                    status=200, content_type="text/html; charset=utf-8", body=html
                )

        await context.route("**/*", respond)
        return context

    mocker.patch.object(Browser, "new_context", autospec=True, side_effect=new_context)
    result = asyncio.run(run(TEST_URL, timeout_seconds=3, artifacts_dir=tmp_path))

    assert result == (1 if scenario in ("shell", "network") else 0)
    assert attempts == [TEST_URL] * (1 if scenario == "ready" else 2)
    diagnostics = list(Path(tmp_path).glob("attempt-*"))
    assert (
        len(diagnostics) == {"ready": 0, "retry": 1, "shell": 2, "network": 2}[scenario]
    )
    for directory in diagnostics:
        assert (directory / "screenshot.png").is_file()
        assert (directory / "frame-0.html").is_file()
