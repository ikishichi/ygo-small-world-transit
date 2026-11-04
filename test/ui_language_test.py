"""URL・手動言語切り替えと既存ブックマークの回帰テスト。"""

from urllib.parse import parse_qs, urlsplit

import pandas as pd
import pytest
import streamlit as st
from streamlit.testing.v1 import AppTest

from src.i18n import get_request_locale
from test.html_parser_test import ENGLISH_DECK_HTML
from test.ui_test import DECK_HTML, PROJECT_ROOT, normalize_query_params

LANGUAGE_LABELS = {
    "ja": "日本語",
    "en": "English",
    "ko": "한국어",
    "zh-CN": "简体中文",
}


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


@pytest.mark.parametrize("browser", ["ja-JP", "en-US", "fr-FR", None])
@pytest.mark.parametrize(
    "lang, expected",
    [
        (None, "ja"),
        ("", "ja"),
        ("fr", "ja"),
        ("ja", "ja"),
        ("en", "en"),
        ("ko", "ko"),
        ("zh-CN", "zh-CN"),
    ],
)
def test_initial_language_and_sample(
    app_factory, monkeypatch, mocker, browser, lang, expected
):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: browser))
    page_config = mocker.spy(st, "set_page_config")
    make, get, _ = app_factory
    params = {} if lang is None else {"lang": lang}
    app = make(params)
    expected_title = {
        "ja": "遊戯王スモール・ワールド乗り換え検索",
        "en": "Yu-Gi-Oh! Small World Transit Search",
        "ko": "유희왕 스몰 월드 경로 검색",
        "zh-CN": "游戏王小世界检索路径查询",
    }[expected]

    assert not app.exception
    assert not app.error
    page_config.assert_called_with(page_title=expected_title)
    assert expected_title in app.title[0].value
    assert app.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[expected]
    assert app.menu_button(key="ui_language_menu").options == [
        f":red[**{label}**]" if language == expected else label
        for language, label in LANGUAGE_LABELS.items()
    ]
    assert normalize_query_params(app.query_params) == normalize_query_params(params)
    sample_label = {
        "ja": "サンプルで試す",
        "en": "Try a sample",
        "ko": "샘플로 체험",
        "zh-CN": "试用示例",
    }[expected]
    assert any(button.label == sample_label for button in app.button)
    assert all(app.selectbox(key=key).disabled for key in ("origin", "destination"))
    assert not app.menu_button(key="ui_language_menu").disabled
    get.assert_not_called()


@pytest.mark.parametrize("lang", ["ja", "en"])
def test_switch_reload_and_home_without_deck(app_factory, monkeypatch, lang):
    browser_locale = "en-US" if lang == "ja" else "ja-JP"
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: browser_locale))
    make, get, _ = app_factory
    app = make({"lang": "en" if lang == "ja" else "ja"})
    app.menu_button(key="ui_language_menu").click(lang).run()

    assert not app.exception
    assert not app.error
    assert app.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[lang]
    assert normalize_query_params(app.query_params) == {"lang": [lang]}
    # 新規セッションでURLを開き直しても、選択した言語を維持する。
    reloaded = make(dict(app.query_params))
    assert not reloaded.exception
    assert reloaded.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[lang]
    home_url = app.title[0].value.split("](")[1][:-1]
    assert home_url == f"https://ygo-small-world-transit.streamlit.app/?lang={lang}"
    home_params = {
        key: values[-1]
        for key, values in parse_qs(urlsplit(home_url).query).items()
    }
    home = make(home_params)
    assert not home.exception
    assert home.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[lang]
    get.assert_not_called()


@pytest.mark.parametrize(
    "browser, lang, expected",
    [
        ("ja-JP", "en", "en"),
        ("en-US", "ja", "ja"),
        ("en-US", None, "ja"),
        ("en-US", "", "ja"),
        ("en-US", "fr", "ja"),
        ("en-US", "ko", "ko"),
        ("en-US", "zh-CN", "zh-CN"),
        (None, None, "ja"),
    ],
)
def test_home_keeps_explicit_language_and_clears_deck(
    app_factory, monkeypatch, browser, lang, expected
):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: browser))
    make, get, _ = app_factory
    params = {"cgid": "A", "dno": "1", "request_locale": "ja"}
    if lang is not None:
        params["lang"] = lang
    app = make(params)
    assert not app.exception
    assert not app.error

    home_url = app.title[0].value.split("](")[1][:-1]
    expected_query = {"lang": [lang]} if lang in LANGUAGE_LABELS else {}
    assert parse_qs(urlsplit(home_url).query) == expected_query
    expected_url = "https://ygo-small-world-transit.streamlit.app/"
    if lang in LANGUAGE_LABELS:
        expected_url += f"?lang={lang}"
    assert home_url == expected_url
    home_params = {
        key: values[-1]
        for key, values in parse_qs(urlsplit(home_url).query).items()
    }
    home = make(home_params)
    assert not home.exception
    assert not home.error
    assert home.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[expected]
    assert home.session_state["LOADED_DECK_URL"] is None
    assert normalize_query_params(app.query_params) == normalize_query_params(params)
    get.assert_called_once()


@pytest.mark.parametrize("lang", [None, "ja", "en", "ko", "zh-CN"])
@pytest.mark.parametrize("request_locale", [None, "", "ja", "en", "ko", "cn"])
def test_bookmark_locale_survives_ui_switch(
    app_factory, monkeypatch, lang, request_locale
):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: "en-US"))
    make, get, _ = app_factory
    params = {"cgid": "A", "dno": "123"}
    if lang is not None:
        params["lang"] = lang
    if request_locale is not None:
        params["request_locale"] = request_locale
    app = make(params)
    expected_locale = request_locale or get_request_locale(lang or "ja")
    assert not app.exception
    assert not app.error
    assert parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"] == [
        expected_locale
    ]
    loaded_url = app.session_state["LOADED_DECK_URL"]
    next_language = "zh-CN" if lang == "ko" else "ko"
    app.menu_button(key="ui_language_menu").click(next_language).run()
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

    expected_headers = {
        "en": "Search results",
        "ja": "検索結果",
        "ko": "검색 결과",
        "zh-CN": "查询结果",
    }
    for language in ("en", "ja", "ko", "zh-CN", "en"):
        app.menu_button(key="ui_language_menu").click(language).run()
        assert not app.exception
        assert not app.error
        assert app.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[language]
        assert app.selectbox(key="origin").value == "Mulcharmy Fuwalos"
        assert app.selectbox(key="destination").value == "Dotscaper"
        assert app.radio(key="sort").value == "transit"
        pd.testing.assert_frame_equal(app.session_state["SEARCH_RESULTS"], previous_results)
        assert app.session_state["DECK_NAME"] == deck_name
        assert app.header[0].value == expected_headers[language]
    page_config.assert_called_with(
        page_title=f"{deck_name} | Yu-Gi-Oh! Small World Transit Search"
    )
    assert app.radio[0].options == ["Sort by bridge", "Sort by destination"]
    get.assert_called_once()


@pytest.mark.parametrize("lang", [None, "ja", "en"])
def test_sample_and_manual_load_keep_language_in_bookmark(
    app_factory, monkeypatch, lang
):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: "en-US"))
    make, get, _ = app_factory
    params = {} if lang is None else {"lang": lang}
    language = lang or "ja"
    expected_params = normalize_query_params(params)
    app = make(params)
    sample_label = "Try a sample" if language == "en" else "サンプルで試す"
    next(button for button in app.button if button.label == sample_label).click().run()
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == {
        **expected_params, "cgid": ["c8525f77e0268f9b1ba9110a8a05bc35"],
        "dno": ["193"], "request_locale": [language],
    }
    app.button(key="change_deck").click().run()
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    )
    fetch_label = "Load deck" if language == "en" else "デッキ取得"
    next(button for button in app.button if button.label == fetch_label).click().run()
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == {
        **expected_params, "cgid": ["B"], "dno": ["2"],
        "request_locale": [language],
    }
    assert get.call_count == 2
    reloaded = make(dict(app.query_params))
    assert not reloaded.exception
    assert not reloaded.error
    assert (
        reloaded.menu_button(key="ui_language_menu").label
        == LANGUAGE_LABELS[language]
    )
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


def test_url_language_changes_update_control(app_factory, monkeypatch):
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: "en-US"))
    make, get, _ = app_factory
    app = make({"lang": "ja"})
    app.query_params["lang"] = "en"
    app.run()
    assert app.menu_button(key="ui_language_menu").label == "English"
    assert not app.exception
    assert not app.error
    assert normalize_query_params(app.query_params) == {"lang": ["en"]}

    del app.query_params["lang"]
    app.run()
    assert not app.exception
    assert not app.error
    assert app.menu_button(key="ui_language_menu").label == "日本語"
    assert normalize_query_params(app.query_params) == {}
    get.assert_not_called()


@pytest.mark.parametrize("language", ["ko", "zh-CN"])
def test_new_languages_switch_and_reload_without_deck(app_factory, language):
    make, get, _ = app_factory
    app = make({"lang": "ja"})
    app.menu_button(key="ui_language_menu").click(language).run()

    assert not app.exception
    assert not app.error
    assert app.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[language]
    assert normalize_query_params(app.query_params) == {"lang": [language]}
    expected_titles = {
        "ko": "유희왕 스몰 월드 경로 검색",
        "zh-CN": "游戏王小世界检索路径查询",
    }
    assert expected_titles[language] in app.title[0].value

    reloaded = make(dict(app.query_params))
    assert not reloaded.exception
    assert not reloaded.error
    assert reloaded.menu_button(key="ui_language_menu").label == LANGUAGE_LABELS[language]
    assert get.call_count == 0


@pytest.mark.parametrize(
    "language, database_locale",
    [("ko", "ko"), ("zh-CN", "cn")],
)
def test_new_language_sample_and_manual_load_bookmark_locale(
    app_factory, language, database_locale
):
    make, get, _ = app_factory
    app = make({"lang": language})

    sample_label = "샘플로 체험" if language == "ko" else "试用示例"
    next(button for button in app.button if button.label == sample_label).click().run()
    assert not app.exception
    assert not app.error
    assert parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"] == [
        database_locale
    ]
    assert app.query_params["lang"] == language
    assert app.query_params["request_locale"] == database_locale

    app.button(key="change_deck").click().run()
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    )
    fetch_label = "덱 불러오기" if language == "ko" else "加载牌组"
    next(button for button in app.button if button.label == fetch_label).click().run()

    assert not app.exception
    assert not app.error
    assert app.query_params["lang"] == language
    assert app.query_params["request_locale"] == database_locale
    assert parse_qs(urlsplit(get.call_args.args[-1]).query)["request_locale"] == [
        database_locale
    ]


@pytest.mark.parametrize(
    "language, database_locale, fetch_label, expected_error",
    [
        (
            "ko",
            "ko",
            "덱 불러오기",
            "유효하지 않은 URL입니다. Yu-Gi-Oh! Neuron의 공개 덱 URL을 입력해 주세요.",
        ),
        (
            "zh-CN",
            "cn",
            "加载牌组",
            "URL 无效。请输入 Yu-Gi-Oh! Neuron 的公开牌组 URL。",
        ),
    ],
)
def test_new_language_error_and_database_links(
    app_factory, language, database_locale, fetch_label, expected_error
):
    make, get, _ = app_factory
    app = make({"lang": language})
    intro = app.caption[0].value
    assert f"request_locale={database_locale}" in intro

    app.text_input(key="deck_url_input").set_value("https://example.com/deck")
    next(button for button in app.button if button.label == fetch_label).click().run()

    assert not app.exception
    assert len(app.error) == 1
    assert app.error[0].value == expected_error
    get.assert_not_called()
