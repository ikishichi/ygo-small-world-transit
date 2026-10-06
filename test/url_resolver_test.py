"""url_resolver.py の単体テスト"""
from src.url_resolver import (
    VALID_PREFIX_HTTP,
    build_url_from_query_params,
    has_query_params,
    select_url,
)


class TestHasQueryParams:
    def test_both_present(self):
        assert has_query_params({"cgid": "A", "dno": "1"}) is True

    def test_with_extras(self):
        assert has_query_params({"cgid": "A", "dno": "1", "request_locale": "ja"}) is True

    def test_missing_dno(self):
        assert has_query_params({"cgid": "A"}) is False

    def test_missing_cgid(self):
        assert has_query_params({"dno": "1"}) is False

    def test_empty(self):
        assert has_query_params({}) is False


class TestBuildUrlFromQueryParams:
    def test_with_locale(self):
        params = {"cgid": "A", "dno": "1", "request_locale": "en"}
        expected = VALID_PREFIX_HTTP + "?cgid=A&dno=1&request_locale=en"
        assert build_url_from_query_params(params) == expected

    def test_default_locale_ja(self):
        """request_locale が無い場合は ja を補完する"""
        params = {"cgid": "A", "dno": "1"}
        expected = VALID_PREFIX_HTTP + "?cgid=A&dno=1&request_locale=ja"
        assert build_url_from_query_params(params) == expected

    def test_empty_when_no_query_params(self):
        assert build_url_from_query_params({}) == ""

    def test_empty_when_missing_cgid(self):
        assert build_url_from_query_params({"dno": "1"}) == ""

    def test_empty_when_missing_dno(self):
        assert build_url_from_query_params({"cgid": "A"}) == ""


class TestSelectUrl:
    def test_submit_returns_input_url(self):
        """submit_btn=True のとき、input_url をそのまま返す"""
        assert select_url("user_input", "from_params", submit_btn=True) == "user_input"

    def test_submit_prefers_input_over_query_params(self):
        """Issue #32 regression: submit 時はクエリパラメータ由来のURLで
        ユーザー入力を上書きしてはならない。

        具体例: ユーザーが deck A のクエリパラメータでページを開いたあと、
        deck B のURLを入力して submit したとき、deck B が使われなければならない。
        """
        deck_a_url = VALID_PREFIX_HTTP + "?cgid=A&dno=1&request_locale=ja"
        deck_b_url = VALID_PREFIX_HTTP + "?cgid=B&dno=2&request_locale=ja"
        # ユーザーが deck B を入力し submit。クエリパラメータは deck A 由来。
        # 期待: deck B が選ばれる。
        assert select_url(deck_b_url, deck_a_url, submit_btn=True) == deck_b_url

    def test_no_submit_returns_query_params_url(self):
        """submit_btn=False（ブックマーク経由の自動ロード）のときは
        クエリパラメータ由来のURLを返す"""
        assert select_url("", "from_params", submit_btn=False) == "from_params"

    def test_no_submit_ignores_input_url(self):
        """ブックマーク経由の自動ロード時はユーザー入力は考慮されない"""
        assert select_url("ignored", "from_params", submit_btn=False) == "from_params"
