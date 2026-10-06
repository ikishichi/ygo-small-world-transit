"""URL構築・選択ロジックモジュール"""

VALID_PREFIX_HTTP = "http://www.db.yugioh-card.com/yugiohdb/member_deck.action"
VALID_PREFIX_HTTPS = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action"


def has_query_params(query_params):
    """デッキを一意に識別できるクエリパラメータを持っているか

    Args:
        query_params: dict-like object

    Returns:
        (bool): cgid と dno の両方が含まれるか
    """
    return all(key in query_params for key in ("cgid", "dno"))


def build_url_from_query_params(query_params):
    """クエリパラメータから遊戯王DB公開デッキURLを構築する

    Args:
        query_params: dict-like object (cgid, dno 必須、request_locale は任意)

    Returns:
        (str): 構築した遊戯王DB公開デッキURL。必須パラメータが欠けていれば空文字を返す。
               request_locale が欠けている場合は "ja" を補完する。
    """
    if not has_query_params(query_params):
        return ""
    locale = query_params.get("request_locale", "ja")
    return (
        VALID_PREFIX_HTTP
        + "?cgid=" + query_params["cgid"]
        + "&dno=" + query_params["dno"]
        + "&request_locale=" + locale
    )


def select_url(input_url, query_params_url, submit_btn):
    """デッキ取得に使用するURLを選択する。

    Issue #32 regression guard: submit_btn=True のとき、クエリパラメータ由来のURLで
    ユーザー入力を上書きしてはならない。必ずユーザー入力 (input_url) を返す。
    ブックマーク経由の自動ロード (submit_btn=False) 時のみ query_params_url を使う。

    Args:
        input_url (str): フォームから受け取ったユーザー入力URL
        query_params_url (str): クエリパラメータから構築したURL
        submit_btn (bool): デッキ取得ボタンが押下されたか

    Returns:
        (str): 使用するURL
    """
    if submit_btn:
        return input_url
    return query_params_url
