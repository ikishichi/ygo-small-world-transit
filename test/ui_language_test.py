"""URL・手動言語切り替えと既存ブックマークの回帰テスト。"""

from urllib.parse import parse_qs, urlsplit

import pandas as pd
import pytest
import streamlit as st
from streamlit.testing.v1 import AppTest

from test.html_parser_test import ENGLISH_DECK_HTML
from test.ui_test import DECK_HTML, PROJECT_ROOT, normalize_query_params


@pytest.fixture
def app_factory(mocker, monkeypatch):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    get = mocker.patch("requests.get", return_value=response)

    def make(params=None):
        app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
        app.query_params.update(params or {})
        return app.run()

    return make, get, response


@pytest.mark.parametrize(
    "browser, lang, expected",
    [
        ("en-US", "ja", "ja"),
        ("ja-JP", "en", "en"),
        ("en-US", None, "en"),
        ("en-US", "fr", "en"),
        (None, None, "ja"),
    ],
)
def test_initial_language_and_sample(app_factory, monkeypatch, browser, lang, expected):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: browser))
    make, get, _ = app_factory
    params = {} if lang is None else {"lang": lang}
    app = make(params)

    assert not app.exception
    assert not app.error
    assert app.segmented_control[0].value == expected
    assert app.segmented_control[0].options == ["日本語", "English"]
    assert normalize_query_params(app.query_params) == normalize_query_params(params)
    assert any(button.label in ("サンプルで試す", "Try a sample") for button in app.button)
    assert all(selectbox.disabled for selectbox in app.selectbox)
    get.assert_not_called()


@pytest.mark.parametrize("lang", ["ja", "en"])
def test_switch_and_reload_without_deck(app_factory, lang):
    make, get, _ = app_factory
    app = make({"lang": "en" if lang == "ja" else "ja"})
    app.segmented_control[0].set_value(lang).run()

    assert not app.exception
    assert not app.error
    assert app.segmented_control[0].value == lang
    assert normalize_query_params(app.query_params) == {"lang": [lang]}
    # 新規セッションでURLを開き直しても、ブラウザー言語に戻らない。
    reloaded = make(dict(app.query_params))
    assert not reloaded.exception
    assert reloaded.segmented_control[0].value == lang
    get.assert_not_called()


@pytest.mark.parametrize("lang", [None, "ja", "en"])
@pytest.mark.parametrize("request_locale", [None, "", "ja", "en"])
def test_bookmark_locale_survives_ui_switch(app_factory, lang, request_locale):
    make, get, _ = app_factory
    params = {"cgid": "A", "dno": "123"}
    if lang is not None:
        params["lang"] = lang
    if request_locale is not None:
        params["request_locale"] = request_locale
    app = make(params)
    expected_locale = request_locale or lang or "ja"
    assert not app.exception
    assert not app.error
    assert parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"] == [
        expected_locale
    ]
    loaded_url = app.session_state["LOADED_DECK_URL"]
    next_language = "ja" if lang == "en" else "en"
    app.segmented_control[0].set_value(next_language).run()
    app.run()

    assert not app.exception
    assert not app.error
    assert app.session_state["LOADED_DECK_URL"] == loaded_url
    assert app.session_state["DECK_NAME"] == "テストデッキ"
    assert app.selectbox[0].options == ["テストモンスター"]
    assert normalize_query_params(app.query_params) == normalize_query_params(
        {**params, "lang": next_language}
    )
    get.assert_called_once()


def test_switch_preserves_search_selections_results_sort_and_title(app_factory, mocker):
    make, get, response = app_factory
    response.content = ENGLISH_DECK_HTML.encode("utf-8")
    page_config = mocker.spy(st, "set_page_config")
    app = make({"cgid": "A", "dno": "1"})
    app.selectbox(key="origin").select("Mulcharmy Fuwalos")
    app.selectbox(key="destination").select("Dotscaper")
    next(button for button in app.button if button.label == "経路を検索").click().run()
    app.radio(key="sort").set_value("transit").run()
    previous_results = app.session_state["SEARCH_RESULTS"].copy()
    assert not previous_results.empty
    deck_name = app.session_state["DECK_NAME"]

    for language in ("en", "ja", "en"):
        app.segmented_control[0].set_value(language).run()
        assert not app.exception
        assert not app.error
        assert app.selectbox(key="origin").value == "Mulcharmy Fuwalos"
        assert app.selectbox(key="destination").value == "Dotscaper"
        assert app.radio(key="sort").value == "transit"
        pd.testing.assert_frame_equal(app.session_state["SEARCH_RESULTS"], previous_results)
        assert app.session_state["DECK_NAME"] == deck_name
        assert app.header[0].value == ("Search results" if language == "en" else "検索結果")
    page_config.assert_called_with(
        page_title=f"{deck_name} | Yu-Gi-Oh! Small World Route Finder"
    )
    assert app.radio[0].options == ["Sort by bridge", "Sort by destination"]
    get.assert_called_once()


@pytest.mark.parametrize("lang", ["ja", "en"])
def test_sample_and_manual_load_keep_language_in_bookmark(app_factory, lang):
    make, get, _ = app_factory
    app = make({"lang": lang})
    sample_label = "Try a sample" if lang == "en" else "サンプルで試す"
    next(button for button in app.button if button.label == sample_label).click().run()
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == {
        "lang": [lang], "cgid": ["c8525f77e0268f9b1ba9110a8a05bc35"],
        "dno": ["193"], "request_locale": [lang],
    }
    app.button(key="change_deck").click().run()
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    )
    fetch_label = "Load deck" if lang == "en" else "デッキ取得"
    next(button for button in app.button if button.label == fetch_label).click().run()
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == {
        "lang": [lang], "cgid": ["B"], "dno": ["2"], "request_locale": [lang],
    }
    assert get.call_count == 2
    reloaded = make(dict(app.query_params))
    assert not reloaded.exception
    assert not reloaded.error
    assert reloaded.segmented_control[0].value == lang
    assert reloaded.session_state["DECK_NAME"] == "テストデッキ"
    assert get.call_count == 3


def test_explicit_deck_locale_change_still_reloads(app_factory):
    make, get, _ = app_factory
    app = make({"lang": "en", "cgid": "A", "dno": "1", "request_locale": "ja"})
    app.query_params["request_locale"] = "en"
    app.run()
    assert not app.exception
    assert not app.error
    assert get.call_count == 2
    assert parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"] == ["en"]


def test_url_language_changes_update_control_and_clearing_selection_is_safe(app_factory):
    make, get, _ = app_factory
    app = make({"lang": "ja"})
    app.query_params["lang"] = "en"
    app.run()
    assert app.segmented_control[0].value == "en"
    app.segmented_control[0].set_value(None).run()
    assert not app.exception
    assert not app.error
    assert app.segmented_control[0].value == "en"
    assert normalize_query_params(app.query_params) == {"lang": ["en"]}
    get.assert_not_called()
