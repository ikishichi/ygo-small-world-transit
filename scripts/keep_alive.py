"""ブラウザーで公開アプリを開き、休眠解除と入力画面の表示を確認する。"""

import asyncio
import logging
from pathlib import Path
from time import monotonic

from playwright.async_api import Error, Page, async_playwright

APP_URL = "https://ygo-small-world-transit.streamlit.app/"
APP_TITLE = "遊戯王スモール・ワールド乗り換え検索"
DECK_URL_LABEL = "遊戯王ニューロンの公開デッキURLを入力してください。"
WAKE_BUTTON = "Yes, get this app back up!"
logger = logging.getLogger(__name__)


async def wait_until_ready(page: Page, timeout_seconds: float = 120) -> bool:
    """起動を待つ。Cloud側の外枠とアプリのiframeの両方を調べる。"""
    woke_app = False
    async with asyncio.timeout(timeout_seconds):
        while True:
            for frame in page.frames:
                title = frame.get_by_role("heading", name=APP_TITLE, exact=True)
                textbox = frame.get_by_role("textbox", name=DECK_URL_LABEL, exact=True)
                submit = frame.get_by_role("button", name="デッキ取得", exact=True)
                if (
                    await title.is_visible()
                    and await textbox.is_visible()
                    and await textbox.is_editable()
                    and await submit.is_visible()
                    and await submit.is_enabled()
                ):
                    return woke_app

                wake = frame.get_by_role("button", name=WAKE_BUTTON, exact=True)
                if not woke_app and await wake.is_visible():
                    logger.info("休眠解除ボタンをクリックします")
                    await wake.click(timeout=5_000)
                    woke_app = True

            # DOMの読み込み・iframeの追加・休眠解除後の遷移を短い間隔で確認する。
            await asyncio.sleep(0.5)


async def save_diagnostics(page: Page, directory: Path) -> None:
    """失敗時の画面と、iframeを含むHTMLを保存する。"""
    directory.mkdir(parents=True, exist_ok=True)
    try:
        await page.screenshot(path=str(directory / "screenshot.png"), timeout=5_000)
    except Error:
        logger.exception("失敗画面を保存できませんでした")
    for index, frame in enumerate(page.frames):
        try:
            (directory / f"frame-{index}.html").write_text(
                await frame.content(), encoding="utf-8"
            )
        except Error:
            logger.exception("frame %sのHTMLを保存できませんでした", index)


async def run(
    url: str = APP_URL,
    timeout_seconds: float = 120,
    artifacts_dir: Path = Path("tmp/keep-alive"),
) -> int:
    """一時的な通信失敗は一度再試行し、起動を確認できなければ失敗する。"""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        try:
            for attempt in range(1, 3):
                started = monotonic()
                # 再試行時も新しいセッションで接続し直す。
                context = await browser.new_context()
                page = await context.new_page()
                try:
                    await page.goto(url, wait_until="domcontentloaded", timeout=30_000)
                    woke_app = await wait_until_ready(page, timeout_seconds)
                    logger.info(
                        "起動確認成功: attempt=%s wake=%s elapsed=%.1fs",
                        attempt,
                        woke_app,
                        monotonic() - started,
                    )
                    return 0
                except (Error, TimeoutError):
                    logger.exception("起動確認失敗: attempt=%s", attempt)
                    await save_diagnostics(page, artifacts_dir / f"attempt-{attempt}")
                finally:
                    await context.close()
        finally:
            await browser.close()
    return 1


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    raise SystemExit(asyncio.run(run()))
