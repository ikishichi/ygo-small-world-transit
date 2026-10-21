"""スモール・ワールド乗り換え検索の画面表示モジュール"""
import logging

logger = logging.getLogger(__name__)
import urllib.parse

import pandas as pd
import requests
import streamlit as st

from deck import Deck
from deck_info import DeckInfo
from html_parser import DeckStructureError, NoMonsterError
from search_result import SearchResult
from url_resolver import (
    VALID_PREFIX_HTTP,
    VALID_PREFIX_HTTPS,
    build_url_from_query_params,
    has_query_params,
    select_url,
)


MATCH_FIELDS = {
    "attribute": "属性",
    "type": "種族",
    "level": "レベル",
    "attack": "攻撃力",
    "defence": "守備力",
}


def get_matching_attributes(
    monsters_df: pd.DataFrame, first_name: str, second_name: str
):
    """2体のモンスターで一致する検索項目を名前以外から返す。"""
    first_rows = monsters_df[monsters_df["name"] == first_name]
    second_rows = monsters_df[monsters_df["name"] == second_name]
    if first_rows.empty or second_rows.empty:
        return []

    first = first_rows.iloc[0]
    second = second_rows.iloc[0]
    return [
        (label, str(first[field]))
        for field, label in MATCH_FIELDS.items()
        if (
            pd.notna(first[field])
            and pd.notna(second[field])
            and first[field] == second[field]
        )
    ]


def initialize_session_state():
    """session_state変数を初期化する"""
    # モンスターのDataFrameを保持するsession_state変数
    columns = ['name', 'attribute', 'type', 'level', 'attack', 'defence']
    st.session_state["MONSTERS_DF"] = pd.DataFrame(columns=columns)

    # 検索結果を保持するsession_state変数
    st.session_state["SEARCH_RESULTS"] = None

    # 取得済みデッキの情報。再実行時はこの値を再利用する。
    st.session_state["DECK_NAME"] = None
    st.session_state["LOADED_DECK_URL"] = None

APP_TITLE = "遊戯王スモール・ワールド乗り換え検索"

deck_name = st.session_state.get("DECK_NAME")
st.set_page_config(
    page_title=f"{deck_name} | {APP_TITLE}" if deck_name else APP_TITLE
)
st.html(
    """
    <style>
        [data-testid="stHeadingWithActionElements"]:has(
            h1 a[href="https://ygo-small-world-transit.streamlit.app/"]
        ) {
            container-type: inline-size;
        }
        h1:has(a[href="https://ygo-small-world-transit.streamlit.app/"]) {
            font-size: 5.5cqi;
            line-height: 1.3;
            white-space: nowrap;
        }
        h1 a[href="https://ygo-small-world-transit.streamlit.app/"] {
            color: inherit !important;
            text-decoration: none !important;
        }
    </style>
    """
)
st.title(
    "[遊戯王スモール・ワールド乗り換え検索]"
    "(https://ygo-small-world-transit.streamlit.app/)",
    anchor=False,
)
st.caption("[遊戯王DB](https://www.db.yugioh-card.com/yugiohdb/)の公開デッキを読み込むことで、"
           "[<<スモール・ワールド>>](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja)のサーチ経路を検索できます。")

if 'MONSTERS_DF' not in st.session_state:
    initialize_session_state()
else:
    # 既存セッションにも新しいキャッシュ状態を追加する。
    st.session_state.setdefault("DECK_NAME", None)
    st.session_state.setdefault("LOADED_DECK_URL", None)

# クエリパラメータ取得
query_params = st.query_params

try:
    # クエリパラメータから遊戯王DBのURLを構築（必須パラメータが欠ければ空文字）
    query_params_url = build_url_from_query_params(query_params)

    # 初期値は一度だけ設定し、送信後も同じ入力欄でユーザー入力を保持する。
    if "deck_url_input" not in st.session_state:
        st.session_state["deck_url_input"] = query_params_url

    with st.form(key="deck_url"):
        # URL入力欄の入力値。ブックマーク経由アクセス時は構築済みURLを初期値として表示。
        input_url = st.text_input(
            "遊戯王DBの公開デッキのURLを入力してください。",
            key="deck_url_input",
        )

        # デッキ取得ボタンの押下状態（boolean）
        submit_btn = st.form_submit_button("デッキ取得")

    # 取得ボタン押下、またはクエリパラメータの指定がある場合
    if submit_btn or has_query_params(query_params):
        # Issue #32: submit 時は必ずユーザー入力を採用し、クエリパラメータで上書きしない
        url = select_url(input_url, query_params_url, submit_btn)

        # 取得ボタンが押下されている場合
        if submit_btn:
            if not url.startswith(VALID_PREFIX_HTTP) and not url.startswith(VALID_PREFIX_HTTPS):
                logger.warning(f"無効なURL: {url}")
                raise ValueError("無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。")

        # ソートや検索による再実行では取得済みデッキを再利用する。
        # 明示的な取得操作は、同じURLでも最新状態を読み直す。
        if submit_btn or st.session_state["LOADED_DECK_URL"] != url:
            with st.spinner("デッキを読み込んでいます…"):
                # 取得・解析に失敗した場合は、現在の検索状態とブックマークを保持する。
                deck_info = DeckInfo(url)
                deck_info.fetch_html()

                # 状態更新やブックマーク案内の表示前に、デッキの解析を完了する。
                deck = Deck(deck_info.html_content)
                deck.parse_html()

            if submit_btn:
                # 遊戯王DBのURLからクエリパラメータを取得し、乗り換え検索のクエリパラメータに反映する
                db_query_params = urllib.parse.parse_qs(str(urllib.parse.urlparse(url).query))
                st.query_params["cgid"] = db_query_params["cgid"][0]
                st.query_params["dno"] = db_query_params["dno"][0]
                st.query_params["request_locale"] = db_query_params.get(
                    "request_locale", ["ja"]
                )[0]
                st.info("現在のページをブックマークしておくと、次回からURLの入力を省略できます。")
                # 入力URLに言語指定がなくても、ブックマーク側の既定値と一致させる。
                loaded_url = build_url_from_query_params(st.query_params)
            else:
                loaded_url = url

            # 解析成功後にまとめて状態を更新し、失敗時は前のデッキを保つ。
            st.session_state["MONSTERS_DF"] = deck.monsters_df
            st.session_state["DECK_NAME"] = deck.deck_name
            st.session_state["LOADED_DECK_URL"] = loaded_url
            st.session_state["SEARCH_RESULTS"] = None

            st.set_page_config(
                page_title=f"{deck.deck_name} | {APP_TITLE}"
                if deck.deck_name else APP_TITLE
            )

        deck_name = st.session_state["DECK_NAME"]

        container = st.container(border=True)
        container.badge("取得成功", icon=":material/check:", color="green")
        container.write(f"デッキ：:blue-background[{deck_name}]")

    with st.form(key='select_box'):
        # サーチ元指定（プルダウン。DataFrameの1列目が候補として表示される）
        monsters_df = st.session_state["MONSTERS_DF"]
        deck_is_loaded = not monsters_df.empty
        transit_start = st.selectbox(
            "手札から見せるモンスターを選択してください:red[（必須）]",
            monsters_df,
            index=None,
            placeholder=(
                "モンスターを選択" if deck_is_loaded
                else "デッキを読み込むと選択できます"
            ),
            disabled=not deck_is_loaded,
        )

        # サーチ先指定（プルダウン）
        # 検索結果の中から候補を選ぶ「絞り込み検索」
        transit_goal = st.selectbox(
            "サーチ先とするモンスターを選択してください（任意）",
            monsters_df,
            index=None,
            placeholder=(
                "すべてのサーチ先（指定なし）" if deck_is_loaded
                else "デッキを読み込むと選択できます"
            ),
            disabled=not deck_is_loaded,
        )

        # 検索実行ボタン
        search_btn = st.form_submit_button(
            "検索", disabled=st.session_state["MONSTERS_DF"].empty
        )

    if search_btn:
        if transit_start is None:
            st.session_state["SEARCH_RESULTS"] = None
            st.warning("サーチ元のモンスターを選択してください。")
        else:
            st.session_state["SEARCH_RESULTS"] = SearchResult(
                st.session_state["MONSTERS_DF"], transit_start, transit_goal
            ).get()

    # 検索結果表示
    if st.session_state["SEARCH_RESULTS"] is not None:
        if st.session_state["SEARCH_RESULTS"].empty:
            st.info(
                "該当する経路はありません。サーチ元を変更するか、"
                "サーチ先の指定を外してお試しください。"
            )
        else:
            st.caption(f"検索結果：{len(st.session_state['SEARCH_RESULTS'])}経路")
            # ソート選択ラジオボタン
            sort = st.radio(
                "並べ替え",
                ["経由カード順", "サーチ先順"],
                index=1,
                horizontal=True,
            )

            if sort == "経由カード順":
                search_results = st.session_state["SEARCH_RESULTS"].sort_values(
                    "transit", kind="stable"
                )
            else:
                search_results = st.session_state["SEARCH_RESULTS"].sort_values(
                    "dest", kind="stable"
                )

            st.header("検索結果")
            monsters_df = st.session_state["MONSTERS_DF"]
            for i, route in enumerate(search_results.itertuples(index=False), 1):
                with st.container(border=True):
                    st.markdown(f"**経路 {i}**")
                    st.markdown(f"**手札から見せるカード：** {route.origin}")
                    first_matches = get_matching_attributes(
                        monsters_df, route.origin, route.transit
                    )
                    if first_matches:
                        label, value = first_matches[0]
                        st.caption(f"↓ {label}が一致：{value}")
                    else:
                        st.caption("↓ 一致項目を表示できません")
                    st.markdown(f"**経由するカード：** {route.transit}")
                    second_matches = get_matching_attributes(
                        monsters_df, route.transit, route.dest
                    )
                    if second_matches:
                        label, value = second_matches[0]
                        st.caption(f"↓ {label}が一致：{value}")
                    else:
                        st.caption("↓ 一致項目を表示できません")
                    st.markdown(f"**サーチするカード：** {route.dest}")

except NoMonsterError as error:
    st.error(error)
    st.info("モンスターを含む公開デッキのURLを指定してください。")
except DeckStructureError:
    logger.exception("遊戯王DBのデッキHTMLを解析できませんでした")
    st.error("デッキ情報を解析できませんでした。時間を置いて再試行してください。")
    st.info("デッキレシピが「公開」になっているか確認してください。")
except requests.exceptions.RequestException:
    logger.exception("遊戯王DBからデッキ情報を取得できませんでした")
    st.error("デッキ情報を取得できませんでした。通信状態を確認し、時間を置いて再試行してください。")
except ValueError as ve:
    st.error(ve)
except RuntimeError as re:
    st.error(re)
except Exception:
    logger.exception("予期せぬ例外")
    st.error("予期しないエラーが発生しました。時間を置いて再試行してください。")

finally:
    st.write("[GitHub](https://github.com/ikishichi/ygo-small-world-transit) / "
             "お問い合わせ・バグ報告は[こちら](https://docs.google.com/forms/d/18bz8n0Iw7zcS1Js1EhHxuyQ_HwOyts9goOyytDGqOvI/edit?pli=1)")
