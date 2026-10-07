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
    response = mocker.Mock()
    response.content = DECK_HTML.encode("utf-8")
    get = mocker.patch("requests.get", return_value=response)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py"))
    app.query_params.update({"cgid": "A", "dno": "1", "request_locale": "en"})
    app.run()
    assert not app.exception
    assert not app.error
    assert app.text_input[0].value == (
        "http://www.db.yugioh-card.com/yugiohdb/member_deck.action"
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
    get.assert_called_with(input_url)

    app.run()
    assert not app.exception
    assert not app.error
    get.assert_called_with(
        "http://www.db.yugioh-card.com/yugiohdb/member_deck.action"
        + "?cgid=B&dno=2&request_locale=" + expected_locale
    )


def test_switch_decks_without_initial_bookmark(mocker, monkeypatch):
    """初回アクセス後も、連続したデッキ切り替えを1回の送信で反映する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    responses = []
    for deck in ("A", "B", "C"):
        response = mocker.Mock()
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
            "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
            + f"?cgid={deck}&dno={count}&request_locale=ja"
        )
        app.text_input[0].set_value(input_url)
        app.button[0].click().run()

        assert not app.exception
        assert not app.error
        assert get.call_count == count
        get.assert_called_with(input_url)
        assert app.text_input[0].value == input_url
        query_params = normalize_query_params(app.query_params)
        assert query_params["cgid"] == [deck]
        assert query_params["dno"] == [str(count)]
        assert app.session_state["MONSTERS_DF"]["name"].tolist() == [
            f"モンスター{deck}"
        ]


@pytest.mark.parametrize("failure", ["http_error", "connection_error"])
def test_failed_deck_switch_preserves_state(mocker, monkeypatch, failure):
    """取得失敗時は元の状態を保ち、再試行成功時にデッキを切り替える。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    response = mocker.Mock(content=DECK_HTML.encode("utf-8"))
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
    assert not app.info
    get.assert_called_with(input_url)
    assert normalize_query_params(app.query_params) == previous_params
    pd.testing.assert_frame_equal(app.session_state["MONSTERS_DF"], previous_monsters)
    pd.testing.assert_frame_equal(app.session_state["SEARCH_RESULTS"], previous_results)
    assert app.text_input[0].value == input_url

    get.side_effect = None
    response.raise_for_status.side_effect = None
    response.content = DECK_HTML.replace("テストモンスター", "モンスターB").encode("utf-8")
    app.button[0].click().run()

    assert not app.exception
    assert not app.error
    get.assert_called_with(input_url)
    assert normalize_query_params(app.query_params) == {
        "cgid": ["B"], "dno": ["2"], "request_locale": ["ja"]
    }
    assert app.session_state["MONSTERS_DF"]["name"].tolist() == ["モンスターB"]
    assert app.session_state["SEARCH_RESULTS"] is None
