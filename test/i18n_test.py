"""表示言語、取得言語、翻訳文の検証。"""

from string import Formatter

import pytest

from src.i18n import (
    LANGUAGE_NAMES,
    MESSAGES,
    get_request_locale,
    resolve_language,
    route_count,
)


@pytest.mark.parametrize(
    "lang, expected",
    [
        (None, "ja"),
        ("", "ja"),
        ("ja", "ja"),
        ("en", "en"),
        ("ko", "ko"),
        ("zh-CN", "zh-CN"),
        ("fr", "ja"),
        ("en-US", "ja"),
        ("ZH-CN", "ja"),
        ("JA", "ja"),
        ("EN", "ja"),
    ],
)
def test_url_language_and_japanese_default(lang, expected):
    assert resolve_language(lang) == expected


def test_language_is_japanese_when_omitted():
    assert resolve_language() == "ja"


@pytest.mark.parametrize(
    "language, expected",
    [("ja", "ja"), ("en", "en"), ("ko", "ko"), ("zh-CN", "cn")],
)
def test_ui_language_maps_to_card_database_locale(language, expected):
    assert get_request_locale(language) == expected


def test_language_names_cover_all_supported_languages():
    assert LANGUAGE_NAMES == {
        "ja": "日本語",
        "en": "English",
        "ko": "한국어",
        "zh-CN": "简体中文",
    }


def test_translation_keys_and_placeholders_match_for_all_languages():
    assert set(MESSAGES) == set(LANGUAGE_NAMES)
    assert MESSAGES["ja"].keys() == MESSAGES["en"].keys()
    assert MESSAGES["ja"].keys() == MESSAGES["ko"].keys()
    assert MESSAGES["ja"].keys() == MESSAGES["zh-CN"].keys()

    def fields(text):
        return {
            field for _, field, _, _ in Formatter().parse(text) if field is not None
        }

    for key, japanese in MESSAGES["ja"].items():
        for language in ("en", "ko", "zh-CN"):
            assert fields(japanese) == fields(MESSAGES[language][key]), (
                language, key
            )


@pytest.mark.parametrize(
    "count, expected",
    [(0, "0 routes"), (1, "1 route"), (2, "2 routes")],
)
def test_english_route_count(count, expected):
    assert route_count(count, "en") == expected


@pytest.mark.parametrize(
    "language, expected",
    [("ja", "0経路"), ("ko", "0개의 경로"), ("zh-CN", "0条路径")],
)
def test_non_english_route_count(language, expected):
    assert route_count(0, language) == expected
