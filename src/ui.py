"""スモール・ワールド乗り換え検索の画面表示モジュール"""
import urllib.parse

import streamlit as st
import pandas as pd

from deckinfo import DeckInfo
from deck import Deck
from search_result import SearchResult

st.title("遊戯王スモール・ワールド乗り換え検索")
st.caption("遊戯王DBの公開デッキを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。")

# モンスターのDataFrameを保持するsession_state変数
if 'MONSTERS_DF' not in st.session_state:
    columns = ['name', 'attribute', 'type', 'level', 'attack', 'defence']
    st.session_state["MONSTERS_DF"] = pd.DataFrame(columns=columns)

# 検索結果を保持するsession_state変数
if 'SEARCH_RESULTS' not in st.session_state:
    st.session_state["SEARCH_RESULTS"] = None

# クエリパラメータ取得
query_params = st.experimental_get_query_params()

try:
    with st.form(key="deck_url"):
        input_url = None
        # クエリパラメータの設定がある場合、遊戯王DBのURLはクエリパラメータから生成する
        if query_params:
            input_url = "http://www.db.yugioh-card.com/yugiohdb/member_deck.action" \
                        + "?cgid=" + query_params["cgid"][0] \
                        + "&dno=" + query_params["dno"][0] \
                        + "&request_locale=" + query_params["request_locale"][0]

        # URL入力欄の入力値
        url = st.text_input("遊戯王DBの公開デッキのURLを入力してください。", input_url)

        # デッキ取得ボタンの押下状態（boolean）
        submit_btn = st.form_submit_button("デッキ取得")

    # 取得ボタン押下、またはクエリパラメータの指定がある場合
    if submit_btn or query_params:
        # デッキ情報（htmlバイナリデータ）を取得する
        di = DeckInfo(url)
        if di.is_success() is False:
            st.warning("無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。")
            st.stop()

        # 取得ボタンが押下されている場合
        if submit_btn:
            # 遊戯王DBのURLからクエリパラメータを取得し、乗り換え検索のクエリパラメータに反映する
            db_query_params = urllib.parse.parse_qs(str(urllib.parse.urlparse(url).query))
            st.experimental_set_query_params(
                cgid=db_query_params["cgid"][0],
                dno=db_query_params["dno"][0],
                request_locale=db_query_params["request_locale"][0],
            )
            st.info("現在のページをブックマークしておくと、次回からURLの入力を省略できます。")

        # デッキからモンスターのDataFrameを取得する
        deck = Deck(di.get())
        st.session_state["MONSTERS_DF"] = deck.get_monsters_df()

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

    if st.session_state["SEARCH_RESULTS"] is not None:
        # ソート選択ラジオボタン
        sort = st.radio("ソート順", ["経由でソート", "サーチ先でソート"], index=1, horizontal=True)

        if sort == "経由でソート":
            search_results = st.session_state["SEARCH_RESULTS"].sort_values("transit")
        else:
            search_results = st.session_state["SEARCH_RESULTS"].sort_values("dest")

        col2, col3 = st.columns(2)
        with col2:
            st.header("経由")
            for transit in search_results["transit"]:
                st.write(transit)

        with col3:
            st.header("サーチ先")
            for dest in search_results["dest"]:
                st.write(dest)

except AttributeError as ae:
    st.error(ae)
    st.error("""以下の点をご確認ください。
             (1)デッキレシピが「公開」になっているか
             (2)デッキに最低1体以上のモンスターが含まれているか""")
except Exception as e:
    st.error("予期せぬ例外が発生しました。繰り返し発生する場合は以下のエラーメッセージを添えてお問い合わせフォームからご連絡ください。")
    st.error(e)
