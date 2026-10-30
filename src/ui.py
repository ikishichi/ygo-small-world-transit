"""スモール・ワールド乗り換え検索の画面表示モジュール"""
import logging
import urllib.parse

import pandas as pd
import requests
import streamlit as st

from deck import Deck
from deck_info import DeckInfo, DeckRedirectError
from html_parser import DeckStructureError, NoMonsterError
from i18n import resolve_language, route_count, translate
from search_result import SearchResult
from url_resolver import (
    DeckUrlError,
    build_url_from_query_params,
    has_query_params,
    normalize_deck_url,
    select_url,
)

logger = logging.getLogger(__name__)
LANGUAGE = resolve_language(st.context.locale)


def t(key, **values):
    """現在のブラウザー言語で画面文言を取得する。"""
    return translate(key, LANGUAGE, **values)


MATCH_FIELDS = ("attribute", "type", "level", "attack", "defence")


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
        (t(field), str(first[field]))
        for field in MATCH_FIELDS
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
    st.session_state["SHOW_DECK_FORM"] = True


def show_deck_form():
    """読み込み済みデッキの変更・再読み込みフォームを開く。"""
    st.session_state["deck_url_input"] = st.session_state.get(
        "DECK_INPUT_URL", st.session_state["LOADED_DECK_URL"] or ""
    )
    st.session_state["SHOW_DECK_FORM"] = True


APP_TITLE = t("app_title")

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
    f"[{APP_TITLE}](https://ygo-small-world-transit.streamlit.app/)",
    anchor=False,
)
st.caption(t("intro", locale=LANGUAGE))

if 'MONSTERS_DF' not in st.session_state:
    initialize_session_state()
else:
    # 既存セッションにも新しいキャッシュ状態を追加する。
    st.session_state.setdefault("DECK_NAME", None)
    st.session_state.setdefault("LOADED_DECK_URL", None)
    st.session_state.setdefault(
        "SHOW_DECK_FORM", st.session_state["LOADED_DECK_URL"] is None
    )

# クエリパラメータ取得
query_params = st.query_params

try:
    # クエリパラメータから遊戯王ニューロンのURLを構築（必須パラメータが欠ければ空文字）
    query_params_url = build_url_from_query_params(
        query_params, default_locale=LANGUAGE
    )

    sample_btn = False
    submit_btn = False
    input_url = ""
    if st.session_state["SHOW_DECK_FORM"]:
        # 再表示時は保存した入力を復元する。閉じている間はwidget状態を作らない。
        if "deck_url_input" not in st.session_state:
            st.session_state["deck_url_input"] = st.session_state.get(
                "DECK_INPUT_URL", query_params_url
            )
        with st.form(key="deck_url"):
            input_url = st.text_input(
                t("deck_url_label"),
                key="deck_url_input",
                placeholder=t("url_placeholder"),
            )
            show_sample = not query_params and st.session_state["LOADED_DECK_URL"] is None
            if show_sample:
                fetch_column, sample_column = st.columns(2)
            else:
                fetch_column = st.container()
            with fetch_column:
                submit_btn = st.form_submit_button(
                    t("fetch_deck"),
                    type="primary",
                    width="stretch",
                )
            if show_sample:
                with sample_column:
                    sample_btn = st.form_submit_button(
                        t("sample"),
                        type="secondary",
                        width="stretch",
                    )

        if sample_btn:
            input_url = (
                "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"
                f"?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=193&request_locale={LANGUAGE}"
            )
            submit_btn = True

        if submit_btn:
            # 入力欄を閉じた後も、変更時には直前の入力を復元する。
            st.session_state["DECK_INPUT_URL"] = input_url

    # 取得ボタン押下、またはクエリパラメータの指定がある場合
    if submit_btn or has_query_params(query_params):
        # Issue #32: submit 時は必ずユーザー入力を採用し、クエリパラメータで上書きしない
        url = select_url(input_url, query_params_url, submit_btn)

        # 取得とブックマークに同じ言語の正規化済みURLを使う。
        url = normalize_deck_url(url, default_locale=LANGUAGE)

        # ソートや検索による再実行では取得済みデッキを再利用する。
        # 明示的な取得操作は、同じURLでも最新状態を読み直す。
        if submit_btn or st.session_state["LOADED_DECK_URL"] != url:
            with st.spinner(t("loading")):
                # 取得・解析に失敗した場合は、現在の検索状態とブックマークを保持する。
                deck_info = DeckInfo(url)
                deck_info.fetch_html()

                # 状態更新やブックマーク案内の表示前に、デッキの解析を完了する。
                deck = Deck(deck_info.html_content)
                deck.parse_html()

            if submit_btn:
                # 遊戯王ニューロンのURLからクエリパラメータを取得し、乗り換え検索のクエリパラメータに反映する
                db_query_params = urllib.parse.parse_qs(str(urllib.parse.urlparse(url).query))
                st.query_params["cgid"] = db_query_params["cgid"][0]
                st.query_params["dno"] = db_query_params["dno"][0]
                st.query_params["request_locale"] = db_query_params.get(
                    "request_locale", [LANGUAGE]
                )[0]
                # 入力URLに言語指定がなくても、ブックマーク側の既定値と一致させる。
                loaded_url = build_url_from_query_params(
                    st.query_params, default_locale=LANGUAGE
                )
            else:
                loaded_url = url
                st.session_state["DECK_INPUT_URL"] = url

            # 解析成功後にまとめて状態を更新し、失敗時は前のデッキを保つ。
            st.session_state["MONSTERS_DF"] = deck.monsters_df
            st.session_state["DECK_NAME"] = deck.deck_name
            st.session_state["LOADED_DECK_URL"] = loaded_url
            st.session_state["SEARCH_RESULTS"] = None

            # 取得が完了したら入力欄を閉じ、検索フォームへ進む。
            st.session_state["SHOW_DECK_FORM"] = False
            # フォームを閉じる再実行をまたいで、手動取得成功時の案内を一度だけ表示する。
            st.session_state["SHOW_BOOKMARK_HINT"] = submit_btn
            st.rerun()

        deck_name = st.session_state["DECK_NAME"] or t("unnamed_deck")
        summary, change = st.columns([4, 1.5], vertical_alignment="center")
        summary.markdown(t("loaded", name=deck_name))
        if not st.session_state["SHOW_DECK_FORM"]:
            change.button(t("change_deck"), key="change_deck", on_click=show_deck_form)
        if st.session_state.pop("SHOW_BOOKMARK_HINT", False):
            st.caption(t("bookmark_hint"))

    with st.form(key='select_box'):
        # サーチ元指定（プルダウン。DataFrameの1列目が候補として表示される）
        monsters_df = st.session_state["MONSTERS_DF"]
        deck_is_loaded = not monsters_df.empty
        transit_start = st.selectbox(
            t("origin_label"),
            monsters_df,
            index=None,
            placeholder=t("monster_placeholder"),
            disabled=not deck_is_loaded,
        )

        # サーチ先指定（プルダウン）
        # 検索結果の中から候補を選ぶ「絞り込み検索」
        transit_goal = st.selectbox(
            t("destination_label"),
            monsters_df,
            index=None,
            placeholder=t("monster_placeholder"),
            disabled=not deck_is_loaded,
        )

        # 検索実行ボタン
        search_btn = st.form_submit_button(
            t("search"),
            disabled=st.session_state["MONSTERS_DF"].empty,
            type="primary",
            width="stretch",
        )

    if search_btn:
        if transit_start is None:
            st.session_state["SEARCH_RESULTS"] = None
            st.warning(t("origin_required"))
        else:
            st.session_state["SEARCH_RESULTS"] = SearchResult(
                st.session_state["MONSTERS_DF"], transit_start, transit_goal
            ).get()

    # 検索結果表示
    if st.session_state["SEARCH_RESULTS"] is not None:
        if st.session_state["SEARCH_RESULTS"].empty:
            st.info(t("no_routes"))
        else:
            with st.container(horizontal=True, vertical_alignment="bottom"):
                st.header(t("results"), width="content")
                st.caption(
                    route_count(len(st.session_state["SEARCH_RESULTS"]), LANGUAGE),
                    width="content",
                )

            # ソート選択ラジオボタン
            sort = st.radio(
                t("sort"),
                [t("sort_transit"), t("sort_destination")],
                index=1,
                horizontal=True,
                label_visibility="collapsed",
            )

            if sort == t("sort_transit"):
                group_by_destination = False
                search_results = st.session_state["SEARCH_RESULTS"].sort_values(
                    "transit", kind="stable"
                )
            else:
                group_by_destination = True
                search_results = st.session_state["SEARCH_RESULTS"].sort_values(
                    "dest", kind="stable"
                )

            monsters_df = st.session_state["MONSTERS_DF"]
            group_label = t("destination") if group_by_destination else t("bridge")
            candidate_label = t("bridge") if group_by_destination else t("destination")
            group_field = "dest" if group_by_destination else "transit"
            candidate_field = "transit" if group_by_destination else "dest"

            route_groups = {}
            for route in search_results.itertuples(index=False):
                group_name = getattr(route, group_field)
                group_key = (
                    (True, None)
                    if pd.isna(group_name)
                    else (False, group_name)
                )
                route_group = route_groups.setdefault(
                    group_key,
                    {"name": group_name, "routes": []},
                )
                route_group["routes"].append(route)

            def display_card_name(name):
                return t("unnamed_card") if pd.isna(name) else str(name)

            origin_name = display_card_name(search_results.iloc[0]["origin"])
            st.markdown(t("origin_summary", name=origin_name))
            displayed_route_number = 0
            for route_group in route_groups.values():
                routes = route_group["routes"]
                candidate_names = list(dict.fromkeys(
                    display_card_name(getattr(route, candidate_field))
                    for route in routes
                ))
                with st.container(border=True):
                    st.markdown(
                        t(
                            "group_summary",
                            label=group_label,
                            names=display_card_name(route_group["name"]),
                        )
                    )
                    st.markdown(
                        t(
                            "group_summary",
                            label=candidate_label,
                            names=" / ".join(candidate_names),
                        )
                    )
                    st.caption(route_count(len(routes), LANGUAGE))
                    with st.expander(
                        t("match_details", routes=route_count(len(routes), LANGUAGE))
                    ):
                        for route in routes:
                            displayed_route_number += 1
                            transit_name = display_card_name(route.transit)
                            destination_name = display_card_name(route.dest)
                            st.markdown(
                                t(
                                    "route",
                                    number=displayed_route_number,
                                    origin=origin_name,
                                    transit=transit_name,
                                    destination=destination_name,
                                )
                            )
                            if pd.notna(route.origin) and pd.notna(route.transit):
                                first_matches = get_matching_attributes(
                                    monsters_df, route.origin, route.transit
                                )
                            else:
                                first_matches = []
                            if first_matches:
                                label, value = first_matches[0]
                                st.caption(t("first_match", label=label, value=value))
                            else:
                                st.caption(t("first_match_missing"))
                            if pd.notna(route.transit) and pd.notna(route.dest):
                                second_matches = get_matching_attributes(
                                    monsters_df, route.transit, route.dest
                                )
                            else:
                                second_matches = []
                            if second_matches:
                                label, value = second_matches[0]
                                st.caption(t("second_match", label=label, value=value))
                            else:
                                st.caption(t("second_match_missing"))

except NoMonsterError:
    st.error(t("no_monsters"))
    st.info(t("monsters_hint"))
except DeckStructureError:
    logger.exception("遊戯王ニューロンのデッキHTMLを解析できませんでした")
    st.error(t("parse_error"))
    st.info(t("public_hint"))
except requests.exceptions.RequestException:
    logger.exception("遊戯王ニューロンからデッキ情報を取得できませんでした")
    st.error(t("network_error"))
except DeckUrlError as error:
    st.error(t(error.code))
except DeckRedirectError:
    st.error(t("redirect_error"))
except Exception:
    logger.exception("予期せぬ例外")
    st.error(t("unexpected_error"))

finally:
    st.write(t("footer"))
