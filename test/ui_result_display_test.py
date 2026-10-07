"""検索結果の経路表示を検証する。"""
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest


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
