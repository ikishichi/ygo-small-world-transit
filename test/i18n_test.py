"""表示言語と翻訳文の検証。"""

from string import Formatter

import pytest

from src.i18n import MESSAGES, resolve_language, route_count


@pytest.mark.parametrize(
    "locale, expected",
    [
        ("en", "en"),
        ("en-US", "en"),
        ("en-GB", "en"),
        ("EN-us", "en"),
        ("en_AU", "en"),
        ("ja-JP", "ja"),
        ("fr-FR", "ja"),
        (None, "ja"),
        ("", "ja"),
        ("english", "ja"),
    ],
)
def test_browser_language(locale, expected):
    assert resolve_language(locale) == expected


@pytest.mark.parametrize("browser_locale", ["ja-JP", "en-US", "fr-FR", None, ""])
@pytest.mark.parametrize("lang", ["ja", "en", None, "", "fr", "en-US"])
def test_url_language_priority(browser_locale, lang):
    expected = lang if lang in {"ja", "en"} else resolve_language(browser_locale)
    assert resolve_language(browser_locale, lang) == expected


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
