"""検索元の検証、0件の案内、取得中表示を検証する。"""

import pandas as pd
import streamlit as st
from streamlit.testing.v1 import AppTest

from test.ui_test import DECK_HTML, PROJECT_ROOT


def make_app(mocker, monkeypatch, loaded=True):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    if loaded:
        app.query_params.update({"cgid": "A", "dno": "1"})
    return app.run()


def test_search_disabled_until_deck_is_loaded(mocker, monkeypatch):
    app = make_app(mocker, monkeypatch, loaded=False)
    assert not app.exception
    search_buttons = [button for button in app.button if button.label == "検索"]
    assert not search_buttons or all(button.disabled for button in search_buttons)


def test_missing_origin_does_not_search_and_clears_previous_results(mocker, monkeypatch):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    search = mocker.patch("search_result.SearchResult")
    app = make_app(mocker, monkeypatch)
    previous = pd.DataFrame({"origin": ["A"], "transit": ["B"], "dest": ["C"]})
    app.session_state["SEARCH_RESULTS"] = previous.copy()
    app.button[1].click().run()

    assert not app.exception
    assert [warning.value for warning in app.warning] == [
        "サーチ元のモンスターを選択してください。"
    ]
    search.assert_not_called()
    assert app.session_state["SEARCH_RESULTS"] is None
    assert not app.radio


def test_no_routes_explains_next_action(mocker, monkeypatch):
    app = make_app(mocker, monkeypatch)
    app.selectbox[0].select("テストモンスター")
    app.button[1].click().run()

    assert not app.exception
    assert not app.error
    assert len(app.info) == 1
    assert "該当する経路はありません" in app.info[0].value
    assert "サーチ先の指定を外して" in app.info[0].value
    assert not app.radio
    assert not app.header


def test_nonempty_routes_have_count_and_sorting(mocker, monkeypatch):
    app = make_app(mocker, monkeypatch)
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame(
        {"origin": ["A", "A"], "transit": ["B", "D"], "dest": ["C", "E"]}
    )
    app.run()

    assert not app.exception
    assert not app.info
    assert any(caption.value == "検索結果：2経路" for caption in app.caption)
    assert len(app.radio) == 1


def test_deck_load_shows_loading_message(mocker, monkeypatch):
    spinner = mocker.spy(st, "spinner")
    app = make_app(mocker, monkeypatch)
    assert not app.exception
    spinner.assert_called_with("デッキを読み込んでいます…")
