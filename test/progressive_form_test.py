"""デッキ未取得・取得成功・失敗時の検索フォーム表示。"""

from streamlit.testing.v1 import AppTest

from test.ui_test import DECK_HTML, PROJECT_ROOT, get_button


def make_app(mocker, monkeypatch, html=DECK_HTML):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=html.encode("utf-8"))
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    return app, get


def form_button_labels(app):
    """画面タイトルを除いたフォームボタンの順序を返す。"""
    title = get_button(app, "遊戯王スモール・ワールド乗り換え検索")
    return [button.label for button in app.button if button is not title]


def test_initial_page_shows_search_form_with_disabled_search(mocker, monkeypatch):
    app, get = make_app(mocker, monkeypatch)

    assert not app.exception
    assert len(app.selectbox) == 2
    assert all(not selectbox.options for selectbox in app.selectbox)
    assert form_button_labels(app) == ["デッキ取得", "検索"]
    assert get_button(app, "検索").disabled
    get.assert_not_called()


def test_loading_deck_enables_search(mocker, monkeypatch):
    app, _ = make_app(mocker, monkeypatch)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    get_button(app, "デッキ取得").click().run()

    assert not app.exception
    assert not app.error
    assert len(app.selectbox) == 2
    assert app.selectbox[0].options == ["テストモンスター"]
    assert form_button_labels(app) == ["デッキ取得", "検索"]
    assert not get_button(app, "検索").disabled


def test_bookmark_enables_search(mocker, monkeypatch):
    app, _ = make_app(mocker, monkeypatch)
    app.query_params.update({"cgid": "A", "dno": "1"})
    app.run()

    assert not app.exception
    assert not app.error
    assert len(app.selectbox) == 2
    assert not get_button(app, "検索").disabled


def test_failed_first_load_does_not_reveal_search_form(mocker, monkeypatch):
    app, _ = make_app(mocker, monkeypatch, html="<html></html>")
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    get_button(app, "デッキ取得").click().run()

    assert not app.exception
    assert app.error
    assert not app.selectbox
    assert form_button_labels(app) == ["デッキ取得"]
