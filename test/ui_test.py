"""デッキ切り替え時のブックマーク更新の回帰テスト。"""
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pandas as pd
import pytest
import requests
import streamlit as st
from streamlit.testing.v1 import AppTest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_TITLE = "遊戯王スモール・ワールド乗り換え検索"
DECK_HTML = """
<html>
<head><meta name="description" content="テストデッキ"></head>
<body>
<div id="detailtext_main">
  <div class="t_body mlist_m">
    <div class="t_row c_normal">
      <span class="card_name">テストモンスター</span>
      <span class="box_card_attribute"><span>光属性</span></span>
      <span class="box_card_level_rank level"><span>レベル1</span></span>
      <span class="card_info_species_and_other_item">【戦士族／通常】</span>
      <span class="atk_power"><span>攻撃力0</span></span>
      <span class="def_power"><span>守備力0</span></span>
    </div>
  </div>
</div>
</body>
</html>
"""


def open_deck_form(app):
    """閉じたURLフォームを、利用者と同じ操作で開く。"""
    if not app.text_input:
        app.button(key="change_deck").click().run()


def submit_deck(app):
    """デッキの取得・再読み込みを実行する。"""
    open_deck_form(app)
    next(button for button in app.button if button.label == "デッキ取得").click().run()


def normalize_query_params(query_params):
    """AppTestのバージョンによる単一クエリ値の形式差を吸収する。"""
    return {
        key: [value] if isinstance(value, str) else value
        for key, value in query_params.items()
    }


@pytest.mark.parametrize("from_bookmark", [False, True])
@pytest.mark.parametrize("deck_name", ["青眼デッキ", "", "<青眼> & 'デッキ'"])
def test_page_title_reflects_loaded_deck(
    mocker, monkeypatch, from_bookmark, deck_name
):
    """入力・ブックマーク経由の取得成功時にデッキ名をタイトルへ反映する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    page_config = mocker.spy(st, "set_page_config")
    response = mocker.Mock(
        status_code=200,
        content=DECK_HTML.replace("テストデッキ", deck_name).encode("utf-8"),
    )
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    assert not app.exception
    page_config.assert_called_with(page_title=APP_TITLE)
    get.assert_not_called()

    if from_bookmark:
        app.query_params.update({"cgid": "A", "dno": "1"})
        app.run()
    else:
        open_deck_form(app)
        app.text_input[0].set_value(
            "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
        )
        submit_deck(app)

    assert not app.exception
    assert not app.error
    expected_title = f"{deck_name} | {APP_TITLE}" if deck_name else APP_TITLE
    page_config.assert_called_with(page_title=expected_title)

    # 読み込み後の再実行でもタイトルを維持し、HTTP取得を増やさない。
    app.run()
    assert not app.exception
    page_config.assert_called_with(page_title=expected_title)
    get.assert_called_once()


def test_switching_deck_updates_page_title(mocker, monkeypatch):
    """送信したデッキへ切り替えた同じ実行内でタイトルを更新する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    page_config = mocker.spy(st, "set_page_config")
    mocker.patch("requests.get", side_effect=[
        mocker.Mock(
            status_code=200,
            content=DECK_HTML.replace("テストデッキ", name).encode("utf-8"),
        )
        for name in ("デッキA", "デッキB")
    ])
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1"})
    app.run()
    page_config.assert_called_with(page_title=f"デッキA | {APP_TITLE}")

    open_deck_form(app)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    )
    submit_deck(app)

    assert not app.exception
    assert not app.error
    page_config.assert_called_with(page_title=f"デッキB | {APP_TITLE}")


@pytest.mark.parametrize(
    "input_locale, expected_locale", [(None, "ja"), ("", "ja"), ("ja", "ja"), ("en", "en")]
)
def test_switch_deck_updates_bookmark_locale(mocker, monkeypatch, input_locale, expected_locale):
    """初回取得のカード名とブックマークの言語を一致させる。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))

    def fetch_deck(url, **kwargs):
        locale = parse_qs(urlsplit(url).query).get("request_locale", ["en"])[0]
        name = "テストモンスター" if locale == "ja" else "Test Monster"
        return mocker.Mock(
            status_code=200,
            content=DECK_HTML.replace("テストモンスター", name).encode("utf-8"),
        )

    get = mocker.patch("requests.get", side_effect=fetch_deck)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1", "request_locale": "en"})
    app.run()
    assert not app.exception
    assert not app.error
    open_deck_form(app)
    assert app.text_input[0].value == (
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        + "?cgid=A&dno=1&request_locale=en"
    )

    input_url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    if input_locale is not None:
        input_url += "&request_locale=" + input_locale
    open_deck_form(app)
    app.text_input[0].set_value(input_url)
    submit_deck(app)

    assert not app.exception
    assert not app.error
    query_params = normalize_query_params(app.query_params)
    assert query_params["cgid"] == ["B"]
    assert query_params["dno"] == ["2"]
    assert query_params["request_locale"] == [expected_locale]
    expected_url = (
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        + "?cgid=B&dno=2&request_locale=" + expected_locale
    )
    get.assert_called_with(expected_url, allow_redirects=False, timeout=(5, 15))
    expected_name = "テストモンスター" if expected_locale == "ja" else "Test Monster"
    assert app.selectbox[0].options == [expected_name]
    assert app.selectbox[1].options == [expected_name]

    app.run()
    assert not app.exception
    assert not app.error
    assert get.call_count == 2


@pytest.mark.parametrize("input_scheme", ["http", "https"])
def test_switch_decks_without_initial_bookmark(mocker, monkeypatch, input_scheme):
    """初回アクセス後も、連続したデッキ切り替えを1回の送信で反映する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    responses = []
    for deck in ("A", "B", "C"):
        response = mocker.Mock(status_code=200)
        response.content = DECK_HTML.replace(
            "テストモンスター", f"モンスター{deck}"
        ).encode("utf-8")
        responses.append(response)
    get = mocker.patch("requests.get", side_effect=responses)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.run()
    assert not app.exception
    assert not app.error
    open_deck_form(app)
    assert app.text_input[0].value == ""
    assert app.text[0].value == (
        "遊戯王ニューロンの公開デッキから"
        "<<スモール・ワールド>>のサーチ経路を検索します。"
    )
    assert "[遊戯王ニューロン](" in app.caption[0].value
    assert "[<<スモール・ワールド>>](" in app.caption[0].value
    assert app.caption[0].value.count("request_locale=ja") == 2
    get.assert_not_called()

    for count, deck in enumerate(("A", "B", "C"), start=1):
        input_url = (
            f"{input_scheme}://www.db.yugioh-card.com/yugiohdb/member_deck.action"
            + f"?cgid={deck}&dno={count}&request_locale=ja"
        )
        open_deck_form(app)
        app.text_input[0].set_value(input_url)
        submit_deck(app)

        assert not app.exception
        assert not app.error
        assert get.call_count == count
        get.assert_called_with(
            input_url.replace("http://", "https://", 1), allow_redirects=False,
            timeout=(5, 15),
        )
        open_deck_form(app)
        assert app.text_input[0].value == input_url
        query_params = normalize_query_params(app.query_params)
        assert query_params["cgid"] == [deck]
        assert query_params["dno"] == [str(count)]
        assert app.session_state["MONSTERS_DF"]["name"].tolist() == [
            f"モンスター{deck}"
        ]


@pytest.mark.parametrize("failure", [
    "http_error", "connection_error", "redirect",
    "missing_deck", "missing_monsters", "missing_deck_name", "changed_monster_list",
    "changed_monster_content", "timeout",
])
def test_failed_deck_switch_preserves_state(mocker, monkeypatch, failure):
    """取得失敗時は元の状態を保ち、再試行成功時にデッキを切り替える。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    page_config = mocker.spy(st, "set_page_config")
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1", "request_locale": "en"})
    app.run()
    assert not app.exception
    assert not app.error
    previous_params = normalize_query_params(app.query_params)
    previous_title = page_config.call_args.kwargs["page_title"]
    previous_monsters = app.session_state["MONSTERS_DF"].copy()
    previous_results = pd.DataFrame(
        {"origin": ["元モンスター"], "transit": ["経由モンスター"], "dest": ["先モンスター"]}
    )
    app.session_state["SEARCH_RESULTS"] = previous_results.copy()

    if failure == "http_error":
        response.raise_for_status.side_effect = requests.exceptions.HTTPError("503")
    elif failure == "redirect":
        response.status_code = 302
    elif failure == "missing_deck":
        response.content = b"<html></html>"
    elif failure == "missing_monsters":
        response.content = b'<html><div id="detailtext_main"></div></html>'
    elif failure == "missing_deck_name":
        response.content = DECK_HTML.replace(
            '<meta name="description" content="テストデッキ">', ""
        ).encode("utf-8")
    elif failure == "timeout":
        get.side_effect = requests.exceptions.Timeout("取得タイムアウト")
    elif failure == "changed_monster_list":
        response.content = DECK_HTML.replace("mlist_m", "changed_monsters").replace(
            '</div>\n</body>',
            '<div class="t_body mlist_s"></div></div>\n</body>',
        ).encode("utf-8")
    elif failure == "changed_monster_content":
        response.content = DECK_HTML.replace("t_row c_normal", "card_row").replace(
            "card_name", "renamed_card"
        ).encode("utf-8")
    else:
        get.side_effect = requests.exceptions.ConnectionError("接続失敗")
    input_url = (
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        + "?cgid=B&dno=2&request_locale=ja"
    )
    open_deck_form(app)
    app.text_input[0].set_value(input_url)
    submit_deck(app)

    assert not app.exception
    assert app.error
    assert page_config.call_args.kwargs["page_title"] == previous_title
    if failure in {
        "missing_monsters", "missing_deck", "missing_deck_name", "changed_monster_list",
        "changed_monster_content",
    }:
        assert app.info
    else:
        assert not app.info
    get.assert_called_with(input_url, allow_redirects=False, timeout=(5, 15))
    assert normalize_query_params(app.query_params) == previous_params
    pd.testing.assert_frame_equal(app.session_state["MONSTERS_DF"], previous_monsters)
    pd.testing.assert_frame_equal(app.session_state["SEARCH_RESULTS"], previous_results)
    open_deck_form(app)
    assert app.text_input[0].value == input_url

    if failure in {"changed_monster_list", "changed_monster_content"}:
        assert "デッキ情報を解析できませんでした" in app.error[0].value
        assert "公開" in app.info[0].value
        assert "モンスターを含む公開デッキ" not in app.info[0].value

    get.side_effect = None
    response.status_code = 200
    response.raise_for_status.side_effect = None
    response.content = DECK_HTML.replace("テストモンスター", "モンスターB").encode("utf-8")
    submit_deck(app)

    assert not app.exception
    assert not app.error
    get.assert_called_with(input_url, allow_redirects=False, timeout=(5, 15))
    assert normalize_query_params(app.query_params) == {
        "cgid": ["B"], "dno": ["2"], "request_locale": ["ja"]
    }
    assert app.session_state["MONSTERS_DF"]["name"].tolist() == ["モンスターB"]
    assert app.session_state["SEARCH_RESULTS"] is None
    assert not app.info
    assert any(
        caption.value == "このページをブックマークすると、次回のデッキ入力を省略できます。"
        for caption in app.caption
    )


@pytest.mark.parametrize("html", [
    b"<html></html>",
    b'<html><div id="detailtext_main"></div></html>',
    DECK_HTML.replace(
        '<meta name="description" content="テストデッキ">', ""
    ).encode("utf-8"),
], ids=["missing_deck", "missing_monsters", "missing_deck_name"])
def test_first_deck_parse_failure_does_not_offer_bookmark(mocker, monkeypatch, html):
    """初回取得でも解析失敗時は案内を出さず、未取得の状態を保持する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=html)
    mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.run()
    previous_monsters = app.session_state["MONSTERS_DF"].copy()

    open_deck_form(app)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    submit_deck(app)

    assert not app.exception
    assert len(app.error) == 1
    assert len(app.info) == 1
    assert not app.query_params
    pd.testing.assert_frame_equal(app.session_state["MONSTERS_DF"], previous_monsters)
    assert app.session_state["SEARCH_RESULTS"] is None


def test_successful_deck_display_order(mocker, monkeypatch):
    """取得後は入力欄を閉じ、要約と主操作の検索を表示する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    open_deck_form(app)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    submit_deck(app)

    assert not app.exception
    assert not app.error
    assert not app.text_input
    assert not app.info
    assert any(
        caption.value == "このページをブックマークすると、次回のデッキ入力を省略できます。"
        for caption in app.caption
    )
    assert ":green[✓ 読み込み済]　**テストデッキ**" == app.markdown[0].value
    assert [button.label for button in app.button] == ["デッキを変更", "経路を検索"]
    assert app.button[1].proto.type == "primary"
    assert len(app.selectbox) == 2
    assert not app.button[1].disabled


def test_loaded_deck_is_reused_until_explicit_refresh(mocker, monkeypatch):
    """通常のStreamlit再実行では再取得せず、明示取得では同じURLも読み直す。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    page_config = mocker.spy(st, "set_page_config")
    responses = [
        mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8")),
        mocker.Mock(
            status_code=200,
            content=DECK_HTML.replace(
                "テストモンスター", "更新後のモンスター"
            ).encode("utf-8"),
        ),
    ]
    get = mocker.patch("requests.get", side_effect=responses)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1"})
    app.run()

    assert not app.exception
    assert not app.error
    assert get.call_count == 1
    app.run()
    assert get.call_count == 1

    app.selectbox[0].select("テストモンスター").run()
    assert get.call_count == 1
    app.button[1].click().run()
    assert not app.exception
    assert get.call_count == 1
    page_config.assert_called_with(page_title=f"テストデッキ | {APP_TITLE}")
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame({
        "origin": ["テストモンスター"],
        "transit": ["経由モンスター"],
        "dest": ["サーチ先モンスター"],
    })
    app.run()
    app.radio[0].set_value("経由でソート").run()
    assert not app.exception
    assert get.call_count == 1
    page_config.assert_called_with(page_title=f"テストデッキ | {APP_TITLE}")

    submit_deck(app)
    assert not app.exception
    assert not app.error
    assert get.call_count == 2
    assert app.session_state["MONSTERS_DF"]["name"].tolist() == ["更新後のモンスター"]
    assert app.session_state["SEARCH_RESULTS"] is None
    get.assert_called_with(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        "?cgid=A&dno=1&request_locale=ja",
        allow_redirects=False,
        timeout=(5, 15),
    )


def test_bookmark_deck_change_fetches_and_clears_previous_results(mocker, monkeypatch):
    """ブックマークのデッキ識別子変更時にデッキ情報を差し替える。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    responses = [
        mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8")),
        mocker.Mock(
            status_code=200,
            content=DECK_HTML.replace("テストデッキ", "デッキB")
            .replace("テストモンスター", "モンスターB")
            .encode("utf-8"),
        ),
    ]
    get = mocker.patch("requests.get", side_effect=responses)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1"})
    app.run()
    assert not app.exception
    assert get.call_count == 1

    app.session_state["SEARCH_RESULTS"] = pd.DataFrame({
        "origin": ["テストモンスター"],
        "transit": ["経由モンスター"],
        "dest": ["サーチ先モンスター"],
    })
    app.query_params["cgid"] = "B"
    app.run()

    assert not app.exception
    assert not app.error
    assert get.call_count == 2
    assert app.session_state["MONSTERS_DF"]["name"].tolist() == ["モンスターB"]
    assert app.session_state["DECK_NAME"] == "デッキB"
    assert app.session_state["SEARCH_RESULTS"] is None
    assert ":green[✓ 読み込み済]　**デッキB**" in [
        element.value for element in app.markdown
    ]
    open_deck_form(app)
    assert app.text_input[0].value == (
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        "?cgid=B&dno=1&request_locale=ja"
    )
    assert get.call_count == 2


def test_invalid_deck_path_preserves_bookmark_without_request(mocker, monkeypatch):
    """旧プレフィックス検査を通る不正パスでも、取得前に拒否する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1"})
    app.run()
    assert not app.error
    previous_params = normalize_query_params(app.query_params)
    previous_monsters = app.session_state["MONSTERS_DF"].copy()
    get.reset_mock()

    open_deck_form(app)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        "/../../card_search.action?cgid=B&dno=2"
    )
    submit_deck(app)

    assert not app.exception
    assert app.error
    assert not app.info
    get.assert_not_called()
    assert normalize_query_params(app.query_params) == previous_params
    pd.testing.assert_frame_equal(app.session_state["MONSTERS_DF"], previous_monsters)


@pytest.mark.parametrize("query", ["cgid=A", "dno=1", "cgid=&dno=1"])
def test_deck_url_missing_required_identity_is_rejected_before_request(
    mocker, monkeypatch, query
):
    """cgidまたはdnoが欠けたURLは入力不備を示し、通信を開始しない。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    get = mocker.patch("requests.get")
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()

    open_deck_form(app)
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?" + query
    )
    submit_deck(app)

    assert not app.exception
    assert len(app.error) == 1
    assert "必須情報（cgid、dno）がありません" in app.error[0].value
    assert not app.info
    get.assert_not_called()


@pytest.mark.parametrize("error", [
    requests.exceptions.Timeout("timeout"),
    requests.exceptions.HTTPError("503"),
    requests.exceptions.ConnectionError("connection failed"),
])
def test_network_failures_show_retry_guidance_without_blame_on_url(
    mocker, monkeypatch, error
):
    """タイムアウト・HTTP・接続失敗は通信案内となり、URL不備を示さない。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    get = mocker.patch("requests.get", side_effect=error)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"

    open_deck_form(app)
    app.text_input[0].set_value(url)
    submit_deck(app)

    assert not app.exception
    assert len(app.error) == 1
    assert "通信状態を確認し、時間を置いて再試行" in app.error[0].value
    assert "無効なURL" not in app.error[0].value
    assert not app.info
    get.assert_called_once_with(
        url + "&request_locale=ja", allow_redirects=False, timeout=(5, 15)
    )


def test_no_monster_deck_shows_specific_guidance(mocker, monkeypatch):
    """モンスターがないデッキではモンスターを含むURLを案内する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(
        status_code=200,
        content=(
            '<html><head><meta name="description" content="魔法罠デッキ"></head>'
            '<body><div id="detailtext_main"><div class="t_body mlist_m"></div>'
            '<div class="t_body mlist_s"></div>'
            '</div></body></html>'
        ).encode("utf-8"),
    )
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"

    open_deck_form(app)
    app.text_input[0].set_value(url)
    submit_deck(app)

    assert not app.exception
    assert len(app.error) == 1
    assert "モンスターが見つかりませんでした" in app.error[0].value
    assert len(app.info) == 1
    assert "モンスターを含む公開デッキ" in app.info[0].value
    get.assert_called_once_with(
        url + "&request_locale=ja", allow_redirects=False, timeout=(5, 15)
    )


def test_deck_form_closes_after_refresh_and_restores_input(mocker, monkeypatch):
    """取得・変更・同URL再取得で入力を復元し、成功後は再び閉じる。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    get = mocker.patch("requests.get", return_value=mocker.Mock(
        status_code=200, content=DECK_HTML.encode("utf-8")
    ))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    app.text_input[0].set_value(url)
    submit_deck(app)

    assert not app.exception
    assert not app.text_input
    assert [button.label for button in app.button] == ["デッキを変更", "経路を検索"]
    assert any(
        caption.value == "このページをブックマークすると、次回のデッキ入力を省略できます。"
        for caption in app.caption
    )
    assert all("再読み込みできます" not in caption.value for caption in app.caption)
    get.assert_called_once()

    # ブラウザーから古い空のwidget状態が届いても、変更操作で復元する。
    app.session_state["deck_url_input"] = ""
    open_deck_form(app)
    assert app.text_input[0].value == url
    assert [button.label for button in app.button] == ["デッキ取得", "経路を検索"]
    assert all(
        "ブックマーク" not in caption.value for caption in app.caption
    )
    assert get.call_count == 1
    submit_deck(app)

    assert not app.exception
    assert not app.error
    assert not app.text_input
    assert [button.label for button in app.button] == ["デッキを変更", "経路を検索"]
    assert any(
        caption.value == "このページをブックマークすると、次回のデッキ入力を省略できます。"
        for caption in app.caption
    )
    assert get.call_count == 2
    assert app.button[1].proto.type == "primary"

    # 取得成功時の案内は、その後の検索操作では表示しない。
    app.button[1].click().run()
    assert not app.exception
    assert app.warning
    assert all(
        "ブックマーク" not in caption.value for caption in app.caption
    )
    assert get.call_count == 2


@pytest.fixture
def english_app(monkeypatch):
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    monkeypatch.setattr(type(st.context), "locale", property(lambda _: "en-US"))
    return AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))


def test_english_initial_screen(english_app, mocker):
    page_config = mocker.spy(st, "set_page_config")
    english_app.run()
    assert not english_app.exception
    page_config.assert_called_with(page_title="Yu-Gi-Oh! Small World Route Finder")
    assert "Yu-Gi-Oh! Small World Route Finder" in english_app.title[0].value
    assert (
        english_app.text_input[0].label
        == "Enter a public deck URL from the Yu-Gi-Oh! Card Database."
    )
    assert [button.label for button in english_app.button] == [
        "Load deck",
        "Try a sample",
        "Find routes",
    ]
    assert english_app.selectbox[0].disabled
    assert english_app.selectbox[1].disabled
    assert english_app.text[0].value == (
        "Load a public deck from the Yu-Gi-Oh! Card Database "
        "to find search routes for Small World."
    )
    assert "[Yu-Gi-Oh! Card Database](" in english_app.caption[0].value
    assert "[Small World](" in english_app.caption[0].value
    assert english_app.caption[0].value.count("request_locale=en") == 2
    assert "Contact us or report a bug" in english_app.markdown[-1].value


@pytest.mark.parametrize("entry", ["input", "bookmark"])
@pytest.mark.parametrize(
    "specified, expected", [(None, "en"), ("", "en"), ("ja", "ja"), ("en", "en")]
)
def test_english_deck_locale_and_cache(english_app, mocker, entry, specified, expected):
    from test.html_parser_test import ENGLISH_DECK_HTML

    get = mocker.patch(
        "requests.get",
        return_value=mocker.Mock(
            status_code=200,
            content=ENGLISH_DECK_HTML.encode("utf-8"),
        ),
    )
    if entry == "bookmark":
        english_app.query_params.update({"cgid": "A", "dno": "1"})
        if specified is not None:
            english_app.query_params["request_locale"] = specified
        english_app.run()
    else:
        english_app.run()
        url = "http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
        if specified is not None:
            url += "&request_locale=" + specified
        english_app.text_input[0].set_value(url)
        next(
            button for button in english_app.button if button.label == "Load deck"
        ).click().run()
    assert not english_app.exception
    assert not english_app.error
    assert parse_qs(urlsplit(get.call_args.args[0]).query)["request_locale"] == [
        expected
    ]
    assert english_app.selectbox[0].options[0] == "Mulcharmy Fuwalos"
    if entry != "bookmark":
        assert normalize_query_params(english_app.query_params)["request_locale"] == [
            expected
        ]
    english_app.run()
    assert not english_app.exception
    get.assert_called_once()
    # フォームを開いてもデッキ取得や検索状態の消去は起こらない。
    english_app.button(key="change_deck").click().run()
    get.assert_called_once()


@pytest.mark.parametrize(
    "failure, expected",
    [
        ("invalid", "Invalid URL."),
        ("missing", "missing required information"),
        ("redirect", "returned a redirect"),
        ("network", "Check your connection"),
        ("structure", "Could not read the deck information"),
        ("empty", "No monsters were found"),
        ("unexpected", "An unexpected error occurred"),
    ],
)
def test_english_errors_do_not_expose_internal_messages(
    english_app, mocker, failure, expected
):
    content = DECK_HTML
    if failure == "structure":
        content = "<html></html>"
    elif failure == "empty":
        content = '<div id="detailtext_main"><div class="t_body mlist_m"></div></div>'
    get = mocker.patch(
        "requests.get",
        return_value=mocker.Mock(
            status_code=302 if failure == "redirect" else 200,
            content=content.encode("utf-8"),
        ),
    )
    if failure == "network":
        get.side_effect = requests.exceptions.ConnectionError("内部通信エラー")
    elif failure == "unexpected":
        get.side_effect = RuntimeError("内部処理エラー")
    english_app.run()
    url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    if failure == "invalid":
        url = "https://example.com/"
    elif failure == "missing":
        url = url.split("&dno")[0]
    english_app.text_input[0].set_value(url)
    next(
        button for button in english_app.button if button.label == "Load deck"
    ).click().run()
    assert not english_app.exception
    assert len(english_app.error) == 1
    assert expected in english_app.error[0].value
    assert "内部" not in english_app.error[0].value
    assert not english_app.query_params
    if failure in ("invalid", "missing"):
        get.assert_not_called()
