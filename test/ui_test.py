"""デッキ切り替え時のブックマーク更新の回帰テスト。"""
from pathlib import Path

import pandas as pd
import pytest
import requests
from streamlit.testing.v1 import AppTest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
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


def normalize_query_params(query_params):
    """AppTestのバージョンによる単一クエリ値の形式差を吸収する。"""
    return {
        key: [value] if isinstance(value, str) else value
        for key, value in query_params.items()
    }


@pytest.mark.parametrize("input_locale, expected_locale", [(None, "ja"), ("en", "en")])
def test_switch_deck_updates_bookmark_locale(mocker, monkeypatch, input_locale, expected_locale):
    """古い言語を残さず、送信したURLの言語または既定値を保存する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200)
    response.content = DECK_HTML.encode("utf-8")
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1", "request_locale": "en"})
    app.run()
    assert not app.exception
    assert not app.error
    assert app.text_input[0].value == (
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        + "?cgid=A&dno=1&request_locale=en"
    )

    input_url = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=B&dno=2"
    if input_locale is not None:
        input_url += "&request_locale=" + input_locale
    app.text_input[0].set_value(input_url)
    app.button[0].click().run()

    assert not app.exception
    assert not app.error
    query_params = normalize_query_params(app.query_params)
    assert query_params["cgid"] == ["B"]
    assert query_params["dno"] == ["2"]
    assert query_params["request_locale"] == [expected_locale]
    get.assert_called_with(input_url, allow_redirects=False, timeout=(5, 15))

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
    assert app.text_input[0].value == ""
    get.assert_not_called()

    for count, deck in enumerate(("A", "B", "C"), start=1):
        input_url = (
            f"{input_scheme}://www.db.yugioh-card.com/yugiohdb/member_deck.action"
            + f"?cgid={deck}&dno={count}&request_locale=ja"
        )
        app.text_input[0].set_value(input_url)
        app.button[0].click().run()

        assert not app.exception
        assert not app.error
        assert get.call_count == count
        get.assert_called_with(
            input_url.replace("http://", "https://", 1), allow_redirects=False,
            timeout=(5, 15),
        )
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
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1", "request_locale": "en"})
    app.run()
    assert not app.exception
    assert not app.error
    previous_params = normalize_query_params(app.query_params)
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
    app.text_input[0].set_value(input_url)
    app.button[0].click().run()

    assert not app.exception
    assert app.error
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
    assert app.text_input[0].value == input_url

    if failure in {"changed_monster_list", "changed_monster_content"}:
        assert "デッキ情報を解析できませんでした" in app.error[0].value
        assert "公開" in app.info[0].value
        assert "モンスターを含む公開デッキ" not in app.info[0].value

    get.side_effect = None
    response.status_code = 200
    response.raise_for_status.side_effect = None
    response.content = DECK_HTML.replace("テストモンスター", "モンスターB").encode("utf-8")
    app.button[0].click().run()

    assert not app.exception
    assert not app.error
    get.assert_called_with(input_url, allow_redirects=False, timeout=(5, 15))
    assert normalize_query_params(app.query_params) == {
        "cgid": ["B"], "dno": ["2"], "request_locale": ["ja"]
    }
    assert app.session_state["MONSTERS_DF"]["name"].tolist() == ["モンスターB"]
    assert app.session_state["SEARCH_RESULTS"] is None
    assert len(app.info) == 1


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

    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    app.button[0].click().run()

    assert not app.exception
    assert len(app.error) == 1
    assert len(app.info) == 1
    assert not app.query_params
    pd.testing.assert_frame_equal(app.session_state["MONSTERS_DF"], previous_monsters)
    assert app.session_state["SEARCH_RESULTS"] is None


def test_successful_deck_display_order(mocker, monkeypatch):
    """取得成功時の入力欄・案内・取得結果・検索欄の表示順を維持する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(status_code=200, content=DECK_HTML.encode("utf-8"))
    mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=A&dno=1"
    )
    app.button[0].click().run()

    assert not app.exception
    assert not app.error
    elements = [element.type for element in app.main]
    assert [kind for kind in elements if kind in {
        "text_input", "info", "markdown", "selectbox",
    }] == [
        "markdown", "text_input", "info", "markdown", "markdown",
        "selectbox", "selectbox", "markdown",
    ]
    assert 'target="_top"' in app.markdown[0].value
    assert "取得成功" in app.markdown[1].value
    assert "デッキ：:blue-background[テストデッキ]" == app.markdown[2].value


def test_loaded_deck_is_reused_until_explicit_refresh(mocker, monkeypatch):
    """通常のStreamlit再実行では再取得せず、明示取得では同じURLも読み直す。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
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
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame({
        "origin": ["テストモンスター"],
        "transit": ["経由モンスター"],
        "dest": ["サーチ先モンスター"],
    })
    app.run()
    app.radio[0].set_value("経由でソート").run()
    assert not app.exception
    assert get.call_count == 1

    app.button[0].click().run()
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
    assert "デッキ：:blue-background[デッキB]" in [
        element.value for element in app.markdown
    ]


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

    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        "/../../card_search.action?cgid=B&dno=2"
    )
    app.button[0].click().run()

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

    app.text_input[0].set_value(
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?" + query
    )
    app.button[0].click().run()

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

    app.text_input[0].set_value(url)
    app.button[0].click().run()

    assert not app.exception
    assert len(app.error) == 1
    assert "通信状態を確認し、時間を置いて再試行" in app.error[0].value
    assert "無効なURL" not in app.error[0].value
    assert not app.info
    get.assert_called_once_with(url, allow_redirects=False, timeout=(5, 15))


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

    app.text_input[0].set_value(url)
    app.button[0].click().run()

    assert not app.exception
    assert len(app.error) == 1
    assert "モンスターが見つかりませんでした" in app.error[0].value
    assert len(app.info) == 1
    assert "モンスターを含む公開デッキ" in app.info[0].value
    get.assert_called_once_with(url, allow_redirects=False, timeout=(5, 15))
