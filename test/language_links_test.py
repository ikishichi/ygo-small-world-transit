"""ブラウザー設定に依存しない言語URLとデッキ共有の回帰テスト。"""

from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import streamlit as st
from streamlit.testing.v1 import AppTest

from src.language_links import build_language_urls, language_navigation
from test.ui_test import DECK_HTML, normalize_query_params


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_language_urls_preserve_deck_and_explicit_card_language():
    params = {"lang": "ja", "cgid": 'A&"<B>', "dno": "1", "request_locale": "ja"}
    urls = build_language_urls(params)
    for language, url in urls.items():
        assert parse_qs(urlsplit(url).query) == {
            **{key: [value] for key, value in params.items()},
            "lang": [language],
        }
    navigation = language_navigation(params)
    assert navigation.count('target="_self"') == 2
    assert 'hreflang="ja"' in navigation
    assert 'hreflang="en"' in navigation
    assert 'A&"<B>' not in navigation
    assert urls["en"] in unescape(navigation)
    assert params["lang"] == "ja"


@pytest.mark.parametrize(
    "browser, requested, title, fetch_label, search_label",
    [
        ("ja-JP", "en", "Yu-Gi-Oh! Small World Route Finder", "Load deck", "Find routes"),
        (None, "en", "Yu-Gi-Oh! Small World Route Finder", "Load deck", "Find routes"),
        ("en-US", "ja", "遊戯王スモール・ワールド乗り換え検索", "デッキ取得", "経路を検索"),
        ("en-US", "invalid", "Yu-Gi-Oh! Small World Route Finder", "Load deck", "Find routes"),
    ],
)
def test_language_url_controls_initial_content(
    monkeypatch, mocker, browser, requested, title, fetch_label, search_label
):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: browser))
    page_config = mocker.spy(st, "set_page_config")
    get = mocker.patch("requests.get")
    app = AppTest.from_file(str(PROJECT_ROOT / "src/ui.py"))
    app.query_params["lang"] = requested
    app.run()

    assert not app.exception
    page_config.assert_called_with(page_title=title)
    assert title in app.title[0].value
    assert len(app.button) == 3  # langのみのURLでもサンプルを表示する。
    assert app.button[0].label == fetch_label
    assert app.button[-1].label == search_label
    locale = "en" if fetch_label == "Load deck" else "ja"
    intro = next(
        item.value for item in [*app.caption, *app.markdown]
        if "card_search.action" in item.value
    )
    assert f"request_locale={locale}" in intro
    assert any('hreflang="en"' in item.proto.body for item in app.get("html"))
    get.assert_not_called()


@pytest.mark.parametrize("card_language", [None, "ja"])
def test_fixed_language_survives_deck_load_and_bookmark(
    monkeypatch, mocker, card_language
):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: "ja-JP"))
    get = mocker.patch(
        "requests.get",
        return_value=mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8")),
    )
    app = AppTest.from_file(str(PROJECT_ROOT / "src/ui.py"))
    app.query_params["lang"] = "en"
    app.run()
    deck_url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    if card_language:
        deck_url += "&request_locale=" + card_language
    app.text_input[0].set_value(deck_url)
    app.button[0].click().run()

    expected = {
        "lang": ["en"], "cgid": ["A"], "dno": ["1"],
        "request_locale": [card_language or "en"],
    }
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == expected
    get.assert_called_once()
    requested_locale = parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"]
    assert requested_locale == expected["request_locale"]
    # 新しいブラウザーセッションでブックマークを開いても、表示言語を維持する。
    bookmark = AppTest.from_file(str(PROJECT_ROOT / "src/ui.py"))
    bookmark.query_params.update(app.query_params)
    bookmark.run()
    assert not bookmark.exception
    assert not bookmark.error
    assert "Yu-Gi-Oh! Small World Route Finder" in bookmark.title[0].value
    assert bookmark.button[-1].label == "Find routes"
    navigation = next(
        item.proto.body for item in bookmark.get("html")
        if 'hreflang="en"' in item.proto.body
    )
    assert "cgid=A&amp;dno=1" in navigation
    assert f"request_locale={card_language or 'en'}" in navigation
    bookmark.run()
    assert get.call_count == 2
