"""スモール・ワールド乗り換え検索の画面表示モジュール"""
import streamlit as st
import pandas as pd
from deckinfo import DeckInfo
from deck import Deck

st.title("遊戯王スモール・ワールド乗り換え検索")
st.caption("遊戯王DBの公開デッキを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。")

columns = ['name', 'attribute', 'type', 'level', 'attack', 'defence']
monsters_df = pd.DataFrame(columns=columns)

with st.form(key="deck_url"):

    # URL入力欄の入力値
    url = st.text_input("遊戯王DBの公開デッキのURLを入力してください。")

    # デッキ取得ボタンの押下状態（boolean）
    submit_btn = st.form_submit_button("デッキ取得")

    try:
        if submit_btn:
            # デッキ情報（htmlバイナリデータ）を取得する
            di = DeckInfo(url)
            if di.is_success() is False:
                st.warning("無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。")
                st.stop()

            # デッキからモンスターのDataFrameを取得する
            deck = Deck(di.get())
            monsters_df = deck.get_monsters_df()

        # サーチ元指定（プルダウン。DataFrameの1列目が候補として表示される）
        transit_start = st.selectbox("サーチ元となるモンスターを選択してください。", monsters_df)

        # TODO: サーチ元に指定されたモンスターでSearchResultクラスに検索要求する。
        search_results = pd.DataFrame(
            {
                "origin": ["マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー", "マイクロ・コーダー"],
                "transit": ["斬機シグマ", "斬機アディオン", "斬機シグマ", "斬機アディオン", "パラレル・エクシード", "斬機シグマ", "斬機アディオン", "パラレル・エクシード"],
                "dest": ["ガッチリ＠イグニスター", "ガッチリ＠イグニスター", "ドット・スケーパー", "ドット・スケーパー", "ドット・スケーパー", "夢幻崩界イヴリース", "夢幻崩界イヴリース", "夢幻崩界イヴリース"]
            }
        )

        # TODO: 検索結果をUI表示。
        # TODO: (opt)検索結果のモンスター名一覧を取得し、サーチ先プルダウンに表示する。

        # サーチ先指定（プルダウン）
        # 検索結果の中から候補を選ぶ「絞り込み検索」
        # transit_goal = st.selectbox("サーチ先とするモンスターを選択してください（任意）", monsters_df)

        col2, col3 = st.columns(2)
        origin = search_results

        # with col1:
        #     st.header("サーチ元")
        #     for origin in search_results["origin"]:
        #         st.write(origin)

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

