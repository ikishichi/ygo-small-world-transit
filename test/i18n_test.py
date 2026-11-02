"""表示言語と翻訳文の検証。"""

from string import Formatter

import pytest

from src.i18n import MESSAGES, resolve_language, route_count


@pytest.mark.parametrize(
    "lang, expected",
    [
        (None, "ja"),
        ("", "ja"),
        ("ja", "ja"),
        ("en", "en"),
        ("fr", "ja"),
        ("en-US", "ja"),
        ("JA", "ja"),
        ("EN", "ja"),
    ],
)
def test_url_language_and_japanese_default(lang, expected):
    assert resolve_language(lang) == expected


def test_language_is_japanese_when_omitted():
    assert resolve_language() == "ja"


def test_translation_keys_and_placeholders_match():
    assert MESSAGES["ja"].keys() == MESSAGES["en"].keys()

    def fields(text):
        return {
            field for _, field, _, _ in Formatter().parse(text) if field is not None
        }

    for key, japanese in MESSAGES["ja"].items():
        assert fields(japanese) == fields(MESSAGES["en"][key]), key


@pytest.mark.parametrize(
    "count, expected", [(0, "0 routes"), (1, "1 route"), (2, "2 routes")]
)
def test_english_route_count(count, expected):
    assert route_count(count, "en") == expected
    assert route_count(count, "ja") == f"{count}経路"
