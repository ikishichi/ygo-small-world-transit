"""検索経路の内容と、一致項目数による境界値を検証する。"""

import pandas as pd
import pytest

from src.search_result import SearchResult


MATCH_COLUMNS = ["attribute", "type", "level", "attack", "defence"]
RESULT_COLUMNS = ["origin", "transit", "dest"]


@pytest.fixture
def monsters():
    return pd.DataFrame(
        {
            "name": [
                "テストマン",
                "テストクリボー",
                "LL-テスト・ダック",
                "テストマンネオ",
                "テストマンオリジン",
            ],
            "attribute": ["光", "闇", "風", "光", "光"],
            "type": [
                "サイバース族",
                "悪魔族",
                "鳥獣族",
                "サイバース族",
                "サイバース族",
            ],
            "level": ["10", "1", "1", "10", "10"],
            "attack": ["100", "0", "50", "10000", "10000"],
            "defence": ["200", "200", "0", "200", "0"],
        }
    )


def assert_routes(actual, routes):
    """余分な経路・不足・重複も含めて、返却内容を比較する。"""
    expected = pd.DataFrame(routes, columns=RESULT_COLUMNS, dtype=object)
    pd.testing.assert_frame_equal(actual.reset_index(drop=True), expected)


def test_get_no_destination(monsters):
    actual = SearchResult(monsters, "LL-テスト・ダック").get()
    assert_routes(
        actual,
        [
            ["LL-テスト・ダック", "テストクリボー", "テストマン"],
            ["LL-テスト・ダック", "テストクリボー", "LL-テスト・ダック"],
            ["LL-テスト・ダック", "テストクリボー", "テストマンネオ"],
            ["LL-テスト・ダック", "テストマンオリジン", "LL-テスト・ダック"],
        ],
    )


def test_get_set_destination(monsters):
    actual = SearchResult(monsters, "LL-テスト・ダック", "テストマン").get()
    assert_routes(actual, [["LL-テスト・ダック", "テストクリボー", "テストマン"]])


def test_get_not_exist(monsters):
    assert SearchResult(monsters, "存在しないモンスター").get() is None


def test_get_unselected_origin(monsters):
    assert SearchResult(monsters, None).get() is None


@pytest.mark.parametrize("destination", ["テストマンオリジン", "存在しないモンスター"])
def test_get_unreachable_destination(monsters, destination):
    assert_routes(SearchResult(monsters, "LL-テスト・ダック", destination).get(), [])


def test_get_no_transit():
    monsters = pd.DataFrame(
        [
            ["A", "光", "戦士族", "4", "1000", "1000"],
            ["B", "闇", "悪魔族", "1", "2000", "2000"],
        ],
        columns=["name", *MATCH_COLUMNS],
    )
    assert_routes(SearchResult(monsters, "A").get(), [])


def test_get_empty_deck():
    monsters = pd.DataFrame(columns=["name", *MATCH_COLUMNS])
    assert SearchResult(monsters, "A").get() is None


@pytest.mark.parametrize("matching_column", MATCH_COLUMNS)
def test_get_accepts_each_single_matching_property(matching_column):
    origin = dict(
        zip(["name", *MATCH_COLUMNS], ["A", "光", "戦士族", "4", "1000", "1000"])
    )
    transit = dict(
        zip(["name", *MATCH_COLUMNS], ["B", "闇", "悪魔族", "1", "2000", "2000"])
    )
    transit[matching_column] = origin[matching_column]
    destination = dict(
        zip(["name", *MATCH_COLUMNS], ["C", "風", "鳥獣族", "7", "3000", "3000"])
    )
    destination["defence"] = transit["defence"]
    monsters = pd.DataFrame([origin, transit, destination])

    assert_routes(SearchResult(monsters, "A", "C").get(), [["A", "B", "C"]])


@pytest.mark.parametrize("match_count", [0, 2, 3, 4, 5])
def test_get_rejects_other_match_counts(match_count):
    origin = dict(
        zip(["name", *MATCH_COLUMNS], ["A", "光", "戦士族", "4", "1000", "1000"])
    )
    transit = dict(
        zip(["name", *MATCH_COLUMNS], ["B", "闇", "悪魔族", "1", "2000", "2000"])
    )
    for column in MATCH_COLUMNS[:match_count]:
        transit[column] = origin[column]
    destination = dict(
        zip(["name", *MATCH_COLUMNS], ["C", "風", "鳥獣族", "7", "3000", "3000"])
    )
    destination["defence"] = transit["defence"]
    monsters = pd.DataFrame([origin, transit, destination])

    assert_routes(SearchResult(monsters, "A", "C").get(), [])


def test_get_rejects_second_hop_with_two_matching_properties():
    monsters = pd.DataFrame(
        [
            ["A", "光", "戦士族", "4", "1000", "1000"],
            ["B", "光", "悪魔族", "1", "2000", "2000"],
            ["C", "闇", "鳥獣族", "7", "2000", "2000"],
        ],
        columns=["name", *MATCH_COLUMNS],
    )
    assert_routes(SearchResult(monsters, "A", "C").get(), [])


def test_get_does_not_mutate_deck(monsters):
    original = monsters.copy(deep=True)
    SearchResult(monsters, "LL-テスト・ダック").get()
    pd.testing.assert_frame_equal(monsters, original)
