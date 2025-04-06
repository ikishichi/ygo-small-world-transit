"""スモール・ワールド乗り換え検索の画面表示モジュール"""
import logging
import urllib.parse

import pandas as pd
import streamlit as st

from deck import Deck
from deck_info import DeckInfo
from search_result import SearchResult

VALID_PREFIX_HTTP = 'http://www.db.yugioh-card.com/yugiohdb/member_deck.action'
VALID_PREFIX_HTTPS = 'https://www.db.yugioh-card.com/yugiohdb/member_deck.action'

def initialize_session_state():
    """session_state変数を初期化する"""
    # モンスターのDataFrameを保持するsession_state変数
    columns = ['name', 'attribute', 'type', 'level', 'attack', 'defence']
    st.session_state["MONSTERS_DF"] = pd.DataFrame(columns=columns)

    # 検索結果を保持するsession_state変数
    st.session_state["SEARCH_RESULTS"] = None

def has_query_params(query_params):
    """デッキを一意に識別できるクエリパラメータを持っているか

    Args:
        query_params:

    Returns:
        (bool): has query params or not
    """
    return all(key in query_params for key in {"cgid", "dno"})

st.set_page_config(page_title="遊戯王スモール・ワールド乗り換え検索")
st.title("遊戯王スモール・ワールド乗り換え検索")
st.caption("[遊戯王DB](https://www.db.yugioh-card.com/yugiohdb/)の公開デッキを読み込むことで、"
           "[<<スモール・ワールド>>](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja)のサーチ経路を検索できます。")

if 'MONSTERS_DF' not in st.session_state:
    initialize_session_state()

# クエリパラメータ取得
query_params = st.query_params

try:
    with st.form(key="deck_url"):
        url = ""
        # クエリパラメータの設定がある場合、遊戯王DBのURLはクエリパラメータから生成する
        if has_query_params(query_params):
            # 国と地域の指定がない場合は日本をデフォルト値とする
            if "request_locale" not in query_params:
                query_params["request_locale"] = "ja"

            url = "http://www.db.yugioh-card.com/yugiohdb/member_deck.action" \
                        + "?cgid=" + query_params["cgid"] \
                        + "&dno=" + query_params["dno"] \
                        + "&request_locale=" + query_params["request_locale"]

        # URL入力欄の入力値
        input_url = st.text_input("遊戯王DBの公開デッキのURLを入力してください。")

        # デッキ取得ボタンの押下状態（boolean）
        submit_btn = st.form_submit_button("デッキ取得")

    container = st.container(border=True)

    # 取得ボタン押下、またはクエリパラメータの指定がある場合
    if submit_btn or has_query_params(query_params):
        # 取得ボタンが押下されている場合
        if submit_btn:
            url = input_url
            if not url.startswith(VALID_PREFIX_HTTP) and not url.startswith(VALID_PREFIX_HTTPS):
                logging.warning(f"無効なURL: {url}")
                raise ValueError("無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。")

            initialize_session_state()

            # 遊戯王DBのURLからクエリパラメータを取得し、乗り換え検索のクエリパラメータに反映する
            db_query_params = urllib.parse.parse_qs(str(urllib.parse.urlparse(url).query))
            st.query_params["cgid"] = db_query_params["cgid"][0]
            st.query_params["dno"] = db_query_params["dno"][0]
            if "request_locale" in db_query_params:
                st.query_params["request_locale"] = db_query_params["request_locale"][0]
            st.info("現在のページをブックマークしておくと、次回からURLの入力を省略できます。")

        # デッキ情報（htmlバイナリデータ）を取得する
        deckInfo = DeckInfo(url)
        deckInfo.fetch_html()

        # デッキからモンスターのDataFrameを取得する
        deck = Deck(deckInfo.html_content)
        deck.parse_html()
        st.session_state["MONSTERS_DF"] = deck.monsters_df
        deck_name = deck.deck_name

        container.badge("取得成功", icon=":material/check:", color="green")
        container.write(f"デッキ：:blue-background[{deck_name}]")

    with st.form(key='select_box'):
        # サーチ元指定（プルダウン。DataFrameの1列目が候補として表示される）
        transit_start = st.selectbox("サーチ元とするモンスターを選択してください。", st.session_state["MONSTERS_DF"], index=None)

        # サーチ先指定（プルダウン）
        # 検索結果の中から候補を選ぶ「絞り込み検索」
        transit_goal = st.selectbox("サーチ先とするモンスターを選択してください（任意）", st.session_state["MONSTERS_DF"], index=None)

        # 検索実行ボタン
        search_btn = st.form_submit_button("検索")

    if search_btn:
        # サーチ元に指定されたモンスターでSearchResultクラスに検索要求する
        st.session_state["SEARCH_RESULTS"] = SearchResult(st.session_state["MONSTERS_DF"], transit_start,
                                                          transit_goal).get()

    # 検索結果表示
    if st.session_state["SEARCH_RESULTS"] is not None:
        # ソート選択ラジオボタン
        sort = st.radio("ソート順", ["経由でソート", "サーチ先でソート"], index=1, horizontal=True)

        if sort == "経由でソート":
            search_results = st.session_state["SEARCH_RESULTS"].sort_values("transit")
        else:
            search_results = st.session_state["SEARCH_RESULTS"].sort_values("dest")

        # 経由とサーチ先を2列で表示する
        col1, col2 = st.columns(2)
        with col1:
            st.header("経由")
            for i, transit in enumerate(search_results["transit"], 1):
                st.write(str(i) + ". " + transit)

        with col2:
            st.header("サーチ先")
            for i, dest in enumerate(search_results["dest"], 1):
                st.write(str(i) + ". " + dest)

except ValueError as ve:
    st.error(ve)
except AttributeError as ae:
    st.error(ae)
    st.error("""以下の点をご確認ください。\n
    (1)デッキレシピが「公開」になっているか\n
    (2)デッキに最低1体以上のモンスターが含まれているか""")
except RuntimeError as re:
    st.error(re)
except Exception as e:
    logging.error(f"予期せぬ例外：{e}")
    st.error("""エラーが発生しました。以下の点をご確認ください。\n
             ・URLが間違っていないか""")

finally:
    st.write("[GitHub](https://github.com/ikishichi/ygo-small-world-transit) / "
             "お問い合わせ・バグ報告は[こちら](https://docs.google.com/forms/d/18bz8n0Iw7zcS1Js1EhHxuyQ_HwOyts9goOyytDGqOvI/edit?pli=1)")
