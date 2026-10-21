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
            1, "手札のカード", "経由Zulu", "サーチAardvark", "レベルが一致（1）",
            "種族が一致（ドラゴン）",
        )
        + expected_route(
            2, "手札のカード", "経由Alpha", "サーチZebra", "属性が一致（光）",
            "種族が一致（魔法）",
        )
    )

    app.radio[0].set_value("経由でソート").run()

    assert not app.exception
    assert route_output_events(app) == (
        expected_route(
            1, "手札のカード", "経由Alpha", "サーチZebra", "属性が一致（光）",
            "種族が一致（魔法）",
        )
        + expected_route(
            2, "手札のカード", "経由Zulu", "サーチAardvark", "レベルが一致（1）",
            "種族が一致（ドラゴン）",
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
        1, "手札", "経由", "サーチ先", "種族が一致（サイバース族）",
        "属性が一致（闇属性）",
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
            "origin": "手札",
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
            number, route["origin"], route["transit"], route["dest"],
            "一致項目を表示できません", "一致項目を表示できません",
        ))

    assert not app.exception
    assert not app.error
    assert route_output_events(app) == expected_events
    assert [expander.label for expander in app.expander] == [
        "一致理由を表示（10経路）", "一致理由を表示（10経路）",
    ]
    assert [element.value for element in app.markdown].count(
        "**手札から見せるカード：** 手札"
    ) == 1
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
    assert [
        element.value for element in app.caption
        if element.value.startswith(("手札→経由：", "経由→サーチ先："))
    ] == [
        "手札→経由：一致項目を表示できません",
        "経由→サーチ先：一致項目を表示できません",
    ]


def test_compact_results_group_destinations_without_losing_routes(monkeypatch):
    """単一のサーチ元で重複経路・欠損カード名を保って候補を集約する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["MONSTERS_DF"] = pd.DataFrame(
        columns=["name", "attribute", "type", "level", "attack", "defence"]
    )
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        {"origin": "元A", "transit": "経由1", "dest": "先X"},
        {"origin": "元A", "transit": "経由2", "dest": "先X"},
        {"origin": "元A", "transit": "経由2", "dest": "先X"},
        {"origin": "元A", "transit": None, "dest": "先X"},
    ])

    app.run()

    assert not app.exception
    assert any(caption.value == "検索結果：4経路" for caption in app.caption)
    assert [expander.label for expander in app.expander] == [
        "一致理由を表示（4経路）",
    ]
    markdown_values = [
        element.value for element in app.main if element.type == "markdown"
    ]
    assert markdown_values.count("**手札から見せるカード：** 元A") == 1
    assert "**経由：** 経由1 / 経由2 / カード名なし" in markdown_values
    assert route_output_events(app) == [
        ("markdown", "**経路 1：** 元A → 経由1 → 先X"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
        ("markdown", "**経路 2：** 元A → 経由2 → 先X"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
        ("markdown", "**経路 3：** 元A → 経由2 → 先X"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
        ("markdown", "**経路 4：** 元A → カード名なし → 先X"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
    ]



def test_grouping_follows_selected_sort_for_interleaved_candidates(monkeypatch):
    """交互に現れる候補も選択したソート軸の順で集約する。"""
    monkeypatch.syspath_prepend(str(PROJECT_ROOT / "src"))
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "ui.py")).run()
    app.session_state["MONSTERS_DF"] = pd.DataFrame(
        columns=["name", "attribute", "type", "level", "attack", "defence"]
    )
    app.session_state["SEARCH_RESULTS"] = pd.DataFrame([
        {"origin": "手札", "transit": "Alpha", "dest": "先Z"},
        {"origin": "手札", "transit": "Beta", "dest": "先Y"},
        {"origin": "手札", "transit": "Gamma", "dest": "先Z"},
    ])

    app.run()

    def group_summary_events():
        return [
            element.value for element in app.main
            if element.type == "markdown" and element.value.startswith((
                "**サーチ先：**", "**経由：**",
            ))
        ]

    assert not app.exception
    assert group_summary_events() == [
        "**サーチ先：** 先Y",
        "**経由：** Beta",
        "**サーチ先：** 先Z",
        "**経由：** Alpha / Gamma",
    ]

    app.radio[0].set_value("経由でソート").run()

    assert not app.exception
    assert group_summary_events() == [
        "**経由：** Alpha",
        "**サーチ先：** 先Z",
        "**経由：** Beta",
        "**サーチ先：** 先Y",
        "**経由：** Gamma",
        "**サーチ先：** 先Z",
    ]
    assert route_output_events(app) == [
        ("markdown", "**経路 1：** 手札 → Alpha → 先Z"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
        ("markdown", "**経路 2：** 手札 → Beta → 先Y"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
        ("markdown", "**経路 3：** 手札 → Gamma → 先Z"),
        ("caption", "手札→経由：一致項目を表示できません"),
        ("caption", "経由→サーチ先：一致項目を表示できません"),
    ]
