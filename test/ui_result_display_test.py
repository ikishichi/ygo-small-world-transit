"""検索結果の経路表示を検証する。"""
from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from src.html_parser import HtmlParser
from src.search_result import SearchResult
from test.html_parser_test import MONSTER_HTML


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def route_output_events(app):
    """経路カードに表示するカード名と一致項目を順番に返す。"""
    events = []
    for element in app.main:
        if element.type == "caption" and element.value.startswith("↓"):
            events.append((element.type, element.value))
        elif element.type == "markdown" and element.value.startswith((
            "**経路 ", "**手札から見せるカード：**", "**経由するカード：**",
            "**サーチするカード：**",
        )):
            events.append((element.type, element.value))
    return events


def expected_route(number, origin, transit, first_match, dest, second_match):
    """1経路分の期待する表示順を作る。"""
    return [
        ("markdown", f"**経路 {number}**"),
        ("markdown", f"**手札から見せるカード：** {origin}"),
        ("caption", f"↓ {first_match}"),
        ("markdown", f"**経由するカード：** {transit}"),
        ("caption", f"↓ {second_match}"),
        ("markdown", f"**サーチするカード：** {dest}"),
    ]


def test_search_results_display_complete_routes_and_matching_fields(monkeypatch):
    """ソートごとの並びと、各経路内の3カード・2一致項目を検証する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["MONSTERS_DF"] = pd.DataFrame([
        {"name": "手札のカード", "attribute": "光", "type": "戦士", "level": "1",
         "attack": "100", "defence": "200"},
        {"name": "経由Alpha", "attribute": "光", "type": "魔法", "level": "2",
         "attack": "300", "defence": "400"},
        {"name": "サーチZebra", "attribute": "闇", "type": "魔法", "level": "3",
         "attack": "500", "defence": "600"},
        {"name": "経由Zulu", "attribute": "闇", "type": "ドラゴン", "level": "1",
         "attack": "700", "defence": "800"},
        {"name": "サーチAardvark", "attribute": "地", "type": "ドラゴン", "level": "5",
         "attack": "900", "defence": "1000"},
    ])
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        {"origin": "手札のカード", "transit": "経由Alpha", "dest": "サーチZebra"},
        {"origin": "手札のカード", "transit": "経由Zulu", "dest": "サーチAardvark"},
    ])

    app.run()
    assert app.radio[0].value == "サーチ先でソート"
    assert not app.exception
    assert route_output_events(app) == (
        expected_route(
            1, "手札のカード", "経由Zulu", "レベルが一致：1",
            "サーチAardvark", "種族が一致：ドラゴン",
        )
        + expected_route(
            2, "手札のカード", "経由Alpha", "属性が一致：光",
            "サーチZebra", "種族が一致：魔法",
        )
    )

    app.radio[0].set_value("経由でソート").run()

    assert not app.exception
    assert route_output_events(app) == (
        expected_route(
            1, "手札のカード", "経由Alpha", "属性が一致：光",
            "サーチZebra", "種族が一致：魔法",
        )
        + expected_route(
            2, "手札のカード", "経由Zulu", "レベルが一致：1",
            "サーチAardvark", "種族が一致：ドラゴン",
        )
    )


def test_parsed_species_match_is_displayed_without_brackets(monkeypatch):
    """HTML解析・検索を通した種族の一致理由に表示用の括弧が残らない。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    monsters = []
    for name, attribute, species, level, attack, defence in [
        ("手札", "光", "サイバース族", 4, 1500, 1200),
        ("経由", "闇", "サイバース族", 5, 2000, 1600),
        ("サーチ先", "闇", "魔法使い族", 6, 2500, 1800),
    ]:
        html = (
            MONSTER_HTML.replace("テストモンスター", name)
            .replace("光属性", f"{attribute}属性")
            .replace("戦士族", species)
            .replace("レベル 4", f"レベル {level}")
            .replace("攻撃力 1500", f"攻撃力 {attack}")
            .replace("守備力 1200", f"守備力 {defence}")
        )
        monsters.extend(HtmlParser(html).generate_monsters())
    monsters_df = pd.DataFrame(monsters)
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["MONSTERS_DF"] = monsters_df
    app.session_state["SEARCH_RESULTS"] = SearchResult(
        monsters_df, "手札", "サーチ先"
    ).get()

    app.run()

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_route(
        1, "手札", "経由", "種族が一致：サイバース族",
        "サーチ先", "属性が一致：闇属性",
    )


@pytest.mark.parametrize("sort_label, sort_field, other_field", [
    ("経由でソート", "transit", "dest"),
    ("サーチ先でソート", "dest", "transit"),
])
def test_search_results_keep_input_order_for_equal_sort_keys(
    monkeypatch, sort_label, sort_field, other_field
):
    """同値キーの入力順と、各経路のカードの対応を維持する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    routes = []
    for index in range(20):
        routes.append({
            "origin": f"手札{index:02d}",
            sort_field: "共通Zulu" if index % 2 == 0 else "共通Alpha",
            other_field: f"カード{19 - index:02d}",
        })
    original_results = pd.DataFrame(routes, columns=["origin", "transit", "dest"])
    app.session_state["SEARCH_RESULTS"] = original_results.copy()
    app.run()
    app.radio[0].set_value(sort_label).run()

    # キーで並べ替えても、同値の経路は元の奇数番・偶数番の順に残る。
    expected_indices = [*range(1, 20, 2), *range(0, 20, 2)]
    expected_events = []
    for number, index in enumerate(expected_indices, 1):
        route = routes[index]
        expected_events.extend(expected_route(
            number, route["origin"], route["transit"],
            "一致項目を表示できません", route["dest"],
            "一致項目を表示できません",
        ))

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_events
    pd.testing.assert_frame_equal(
        app.session_state["SEARCH_RESULTS"], original_results
    )


def test_search_results_without_matching_monster_records_are_explained(monkeypatch):
    """カード情報と検索結果が不整合でも、理由を示して例外にしない。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        {"origin": "未登録の元", "transit": "未登録の経由", "dest": "未登録の先"},
    ])

    app.run()

    assert not app.exception
    assert [element.value for element in app.caption if element.value.startswith("↓")] == [
        "↓ 一致項目を表示できません",
        "↓ 一致項目を表示できません",
    ]
