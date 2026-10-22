"""実在するカード情報を使い、検索結果の経路表示を検証する。"""
from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from src.html_parser import HtmlParser
from src.search_result import SearchResult
from test.html_parser_test import MONSTER_HTML


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FLAME_MATCH = "属性が一致（炎属性）"


@pytest.fixture
def monsters_df():
    """公式DBで確認した実カードの値を、HTML解析後の形式で返す。

    確認日: 2026-10-21。テスト実行時の外部通信は行わない。
    参照した公開デッキ:
    https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=193&request_locale=ja
    https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=6bc9142dfec79ce7c911d979fadee289&dno=50&request_locale=ja
    https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=196&request_locale=ja
    """
    return pd.DataFrame([
        ("R－ACEタービュランス", "炎属性", "機械族", "レベル9",
         "攻撃力3000", "守備力3000"),
        ("R－ACEプリベンター", "炎属性", "機械族", "レベル8",
         "攻撃力2800", "守備力2800"),
        ("R－ACEファイア・エンジン", "炎属性", "機械族", "レベル7",
         "攻撃力2500", "守備力2500"),
        ("R－ACEファイア・アタッカー", "炎属性", "機械族", "レベル6",
         "攻撃力2200", "守備力2200"),
        ("R－ACEエアホイスター", "炎属性", "戦士族", "レベル4",
         "攻撃力1700", "守備力1700"),
        ("R－ACEインパルス", "炎属性", "戦士族", "レベル3",
         "攻撃力1500", "守備力1500"),
        ("R－ACEハイドラント", "炎属性", "機械族", "レベル1",
         "攻撃力0", "守備力0"),
        ("怒炎壊獣ドゴラン", "炎属性", "恐竜族", "レベル8",
         "攻撃力3000", "守備力1200"),
        ("灰流うらら", "炎属性", "アンデット族", "レベル3",
         "攻撃力0", "守備力1800"),
        ("増殖するG", "地属性", "昆虫族", "レベル2",
         "攻撃力500", "守備力200"),
        ("俱利伽羅天童", "炎属性", "天使族", "レベル1",
         "攻撃力1500", "守備力1500"),
        ("エフェクト・ヴェーラー", "光属性", "魔法使い族", "レベル1",
         "攻撃力0", "守備力0"),
        ("スポーア", "風属性", "植物族", "レベル1",
         "攻撃力400", "守備力800"),
        ("カオス・ソーサラー", "闇属性", "魔法使い族", "レベル6",
         "攻撃力2300", "守備力2000"),
        ("カードガンナー", "地属性", "機械族", "レベル3",
         "攻撃力400", "守備力400"),
        ("ドッペル・ウォリアー", "闇属性", "戦士族", "レベル2",
         "攻撃力800", "守備力800"),
        ("マルチャミー・フワロス", "風属性", "鳥獣族", "レベル4",
         "攻撃力100", "守備力600"),
        ("斬機シグマ", "光属性", "サイバース族", "レベル4",
         "攻撃力1000", "守備力1500"),
        ("ドットスケーパー", "地属性", "サイバース族", "レベル1",
         "攻撃力0", "守備力2100"),
    ], columns=["name", "attribute", "type", "level", "attack", "defence"])


@pytest.fixture
def app(monkeypatch, monsters_df):
    """実カード情報を読み込み済みにした表示テスト用アプリ。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["MONSTERS_DF"] = monsters_df
    return app


def route_output_events(app):
    """展開された経路詳細のカード名と一致理由を順番に返す。"""
    events = []
    for element in app.main:
        if element.type == "caption" and element.value.startswith(
            ("手札→経由：", "経由→サーチ先：")
        ):
            events.append((element.type, element.value))
        elif element.type == "markdown" and element.value.startswith("**経路 "):
            events.append((element.type, element.value))
    return events


def expected_route(number, origin, transit, dest, first_match, second_match):
    """1経路分の期待する詳細表示を作る。"""
    return [
        ("markdown", f"**経路 {number}：** {origin} → {transit} → {dest}"),
        ("caption", f"手札→経由：{first_match}"),
        ("caption", f"経由→サーチ先：{second_match}"),
    ]


def test_search_results_display_complete_routes_and_matching_fields(app):
    """実際に成立する3経路で、5種類の一致理由とソート順を検証する。"""
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        ("エフェクト・ヴェーラー", "カオス・ソーサラー", "ドッペル・ウォリアー"),
        ("エフェクト・ヴェーラー", "スポーア", "カードガンナー"),
        ("エフェクト・ヴェーラー", "スポーア", "ドッペル・ウォリアー"),
    ], columns=["origin", "transit", "dest"])
    app.run()

    assert app.radio[0].value == "サーチ先でソート"
    assert not app.exception
    assert not app.error
    assert route_output_events(app) == (
        expected_route(
            1, "エフェクト・ヴェーラー", "スポーア", "カードガンナー",
            "レベルが一致（レベル1）", "攻撃力が一致（攻撃力400）",
        )
        + expected_route(
            2, "エフェクト・ヴェーラー", "カオス・ソーサラー", "ドッペル・ウォリアー",
            "種族が一致（魔法使い族）", "属性が一致（闇属性）",
        )
        + expected_route(
            3, "エフェクト・ヴェーラー", "スポーア", "ドッペル・ウォリアー",
            "レベルが一致（レベル1）", "守備力が一致（守備力800）",
        )
    )

    app.radio[0].set_value("経由でソート").run()

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == (
        expected_route(
            1, "エフェクト・ヴェーラー", "カオス・ソーサラー", "ドッペル・ウォリアー",
            "種族が一致（魔法使い族）", "属性が一致（闇属性）",
        )
        + expected_route(
            2, "エフェクト・ヴェーラー", "スポーア", "カードガンナー",
            "レベルが一致（レベル1）", "攻撃力が一致（攻撃力400）",
        )
        + expected_route(
            3, "エフェクト・ヴェーラー", "スポーア", "ドッペル・ウォリアー",
            "レベルが一致（レベル1）", "守備力が一致（守備力800）",
        )
    )


def test_parsed_species_match_is_displayed_without_brackets(app, monsters_df):
    """実カードのHTML解析・検索を通し、種族名に装飾括弧が残らない。"""
    selected = monsters_df[monsters_df["name"].isin([
        "マルチャミー・フワロス", "斬機シグマ", "ドットスケーパー",
    ])].reset_index(drop=True)
    monsters = []
    for card in selected.itertuples(index=False):
        html = (
            MONSTER_HTML.replace("テストモンスター", card.name)
            .replace("光属性", card.attribute)
            .replace("【戦士族／通常】", f"【{card.type}／効果】")
            .replace("レベル 4", card.level.replace("レベル", "レベル "))
            .replace("攻撃力 1500", card.attack.replace("攻撃力", "攻撃力 "))
            .replace("守備力 1200", card.defence.replace("守備力", "守備力 "))
        )
        monsters.extend(HtmlParser(html).generate_monsters())
    parsed_monsters = pd.DataFrame(monsters)
    pd.testing.assert_frame_equal(parsed_monsters, selected)
    app.session_state["MONSTERS_DF"] = parsed_monsters
    app.session_state["SEARCH_RESULTS"] = SearchResult(
        parsed_monsters, "マルチャミー・フワロス", "ドットスケーパー"
    ).get()
    app.run()

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_route(
        1, "マルチャミー・フワロス", "斬機シグマ", "ドットスケーパー",
        "レベルが一致（レベル4）", "種族が一致（サイバース族）",
    )


@pytest.mark.parametrize("sort_label, expected_indices, group_sizes", [
    (
        "経由でソート",
        [18, 0, 4, 8, 12, 3, 7, 11, 15, 17, 2, 6, 10, 14, 16, 1, 5, 9, 13, 19],
        [1, 4, 5, 5, 4, 1],
    ),
    (
        "サーチ先でソート",
        [4, 9, 14, 17, 3, 8, 13, 16, 18, 19, 1, 6, 11, 12, 2, 7, 0, 5, 10, 15],
        [4, 4, 2, 4, 2, 4],
    ),
])
def test_search_results_keep_input_order_for_equal_sort_keys(
    app, sort_label, expected_indices, group_sizes
):
    """実在カード間の異なる20経路で、同値キーの入力順を維持する。"""
    pairs = [
        ("R－ACEタービュランス", "灰流うらら"),
        ("R－ACEプリベンター", "俱利伽羅天童"),
        ("R－ACEファイア・エンジン", "怒炎壊獣ドゴラン"),
        ("R－ACEファイア・アタッカー", "R－ACEエアホイスター"),
        ("R－ACEタービュランス", "R－ACEインパルス"),
        ("R－ACEプリベンター", "灰流うらら"),
        ("R－ACEファイア・エンジン", "俱利伽羅天童"),
        ("R－ACEファイア・アタッカー", "怒炎壊獣ドゴラン"),
        ("R－ACEタービュランス", "R－ACEエアホイスター"),
        ("R－ACEプリベンター", "R－ACEインパルス"),
        ("R－ACEファイア・エンジン", "灰流うらら"),
        ("R－ACEファイア・アタッカー", "俱利伽羅天童"),
        ("R－ACEタービュランス", "俱利伽羅天童"),
        ("R－ACEプリベンター", "R－ACEエアホイスター"),
        ("R－ACEファイア・エンジン", "R－ACEインパルス"),
        ("R－ACEファイア・アタッカー", "灰流うらら"),
        ("R－ACEファイア・エンジン", "R－ACEエアホイスター"),
        ("R－ACEファイア・アタッカー", "R－ACEインパルス"),
        ("R－ACEエアホイスター", "R－ACEファイア・エンジン"),
        ("怒炎壊獣ドゴラン", "R－ACEファイア・エンジン"),
    ]
    original_results = pd.DataFrame([
        ("灰流うらら", transit, dest) for transit, dest in pairs
    ], columns=["origin", "transit", "dest"])
    app.session_state["SEARCH_RESULTS"] = original_results.copy()
    app.run()
    app.radio[0].set_value(sort_label).run()

    expected_events = []
    for number, index in enumerate(expected_indices, 1):
        transit, dest = pairs[index]
        expected_events.extend(expected_route(
            number, "灰流うらら", transit, dest, FLAME_MATCH, FLAME_MATCH,
        ))

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_events
    assert [expander.label for expander in app.expander] == [
        f"一致理由を表示（{size}経路）" for size in group_sizes
    ]
    assert [element.value for element in app.markdown].count(
        "**手札から見せるカード：** 灰流うらら"
    ) == 1
    pd.testing.assert_frame_equal(
        app.session_state["SEARCH_RESULTS"], original_results
    )


def test_search_results_without_matching_monster_records_are_explained(
    app, monsters_df
):
    """異常系: 経由カードの情報を意図的に欠落させ、理由を表示できない状態を作る。"""
    app.session_state["MONSTERS_DF"] = monsters_df[
        monsters_df["name"] != "R－ACEタービュランス"
    ]
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        ("灰流うらら", "R－ACEタービュランス", "R－ACEエアホイスター"),
    ], columns=["origin", "transit", "dest"])
    app.run()

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_route(
        1, "灰流うらら", "R－ACEタービュランス", "R－ACEエアホイスター",
        "一致項目を表示できません", "一致項目を表示できません",
    )


def test_compact_results_group_destinations_without_losing_routes(app):
    """異常系: 実在経路に重複と欠損を意図的に加えても候補を集約できる。"""
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        ("灰流うらら", "R－ACEタービュランス", "R－ACEエアホイスター"),
        ("灰流うらら", "R－ACEプリベンター", "R－ACEエアホイスター"),
        ("灰流うらら", "R－ACEプリベンター", "R－ACEエアホイスター"),
        ("灰流うらら", None, "R－ACEエアホイスター"),
    ], columns=["origin", "transit", "dest"])
    app.run()

    assert not app.exception
    assert not app.error
    assert any(caption.value == "検索結果：4経路" for caption in app.caption)
    assert [expander.label for expander in app.expander] == [
        "一致理由を表示（4経路）",
    ]
    markdown_values = [element.value for element in app.markdown]
    assert markdown_values.count("**手札から見せるカード：** 灰流うらら") == 1
    assert (
        "**経由：** R－ACEタービュランス / R－ACEプリベンター / カード名なし"
    ) in markdown_values
    assert route_output_events(app) == (
        expected_route(
            1, "灰流うらら", "R－ACEタービュランス", "R－ACEエアホイスター",
            FLAME_MATCH, FLAME_MATCH,
        )
        + expected_route(
            2, "灰流うらら", "R－ACEプリベンター", "R－ACEエアホイスター",
            FLAME_MATCH, FLAME_MATCH,
        )
        + expected_route(
            3, "灰流うらら", "R－ACEプリベンター", "R－ACEエアホイスター",
            FLAME_MATCH, FLAME_MATCH,
        )
        + expected_route(
            4, "灰流うらら", "カード名なし", "R－ACEエアホイスター",
            "一致項目を表示できません", "一致項目を表示できません",
        )
    )


def test_grouping_follows_selected_sort_for_interleaved_candidates(app):
    """実際に成立する経路で、交互に現れる候補をソート軸に従って集約する。"""
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        ("灰流うらら", "R－ACEエアホイスター", "俱利伽羅天童"),
        ("灰流うらら", "R－ACEタービュランス", "R－ACEインパルス"),
        ("灰流うらら", "R－ACEプリベンター", "俱利伽羅天童"),
    ], columns=["origin", "transit", "dest"])
    app.run()

    def group_summary_events():
        return [
            element.value for element in app.markdown
            if element.value.startswith(("**サーチ先：**", "**経由：**"))
        ]

    assert not app.exception
    assert not app.error
    assert group_summary_events() == [
        "**サーチ先：** R－ACEインパルス",
        "**経由：** R－ACEタービュランス",
        "**サーチ先：** 俱利伽羅天童",
        "**経由：** R－ACEエアホイスター / R－ACEプリベンター",
    ]

    app.radio[0].set_value("経由でソート").run()

    assert not app.exception
    assert not app.error
    assert group_summary_events() == [
        "**経由：** R－ACEエアホイスター",
        "**サーチ先：** 俱利伽羅天童",
        "**経由：** R－ACEタービュランス",
        "**サーチ先：** R－ACEインパルス",
        "**経由：** R－ACEプリベンター",
        "**サーチ先：** 俱利伽羅天童",
    ]
    assert route_output_events(app) == (
        expected_route(
            1, "灰流うらら", "R－ACEエアホイスター", "俱利伽羅天童",
            FLAME_MATCH, FLAME_MATCH,
        )
        + expected_route(
            2, "灰流うらら", "R－ACEタービュランス", "R－ACEインパルス",
            FLAME_MATCH, FLAME_MATCH,
        )
        + expected_route(
            3, "灰流うらら", "R－ACEプリベンター", "俱利伽羅天童",
            FLAME_MATCH, FLAME_MATCH,
        )
    )


def test_search_results_recover_after_empty_search(app, monsters_df):
    """結果あり→0件→復帰の再検索で、古い集約結果が残らない。"""
    app.session_state["MONSTERS_DF"] = monsters_df[
        monsters_df["name"].isin([
            "灰流うらら", "R－ACEエアホイスター", "増殖するG",
        ])
    ]
    app.run()
    expected_results = pd.DataFrame([
        ("灰流うらら", "R－ACEエアホイスター", "灰流うらら"),
    ], columns=["origin", "transit", "dest"], dtype=object)
    expected_events = expected_route(
        1, "灰流うらら", "R－ACEエアホイスター", "灰流うらら",
        FLAME_MATCH, FLAME_MATCH,
    )

    for origin, count in [("灰流うらら", 1), ("増殖するG", 0), ("灰流うらら", 1)]:
        app.selectbox[0].select(origin)
        next(button for button in app.button if button.label == "経路を検索").click().run()

        assert not app.exception
        assert not app.error
        assert not app.warning
        actual_results = app.session_state["SEARCH_RESULTS"]
        assert len(actual_results) == count
        if count:
            pd.testing.assert_frame_equal(
                actual_results.reset_index(drop=True), expected_results
            )
            assert route_output_events(app) == expected_events
            assert any(caption.value == "検索結果：1経路" for caption in app.caption)
            assert [expander.label for expander in app.expander] == [
                "一致理由を表示（1経路）",
            ]
            assert len(app.radio) == 1
            assert [header.value for header in app.header] == ["検索結果"]
            assert [element.value for element in app.markdown].count(
                "**手札から見せるカード：** 灰流うらら"
            ) == 1
            assert not app.info
        else:
            assert route_output_events(app) == []
            assert not app.expander
            assert not app.radio
            assert not app.header
            assert not any(
                caption.value.startswith("検索結果：") for caption in app.caption
            )
            assert not any(
                element.value.startswith("**手札から見せるカード：**")
                for element in app.markdown
            )
            assert len(app.info) == 1
            assert "該当する経路はありません" in app.info[0].value
