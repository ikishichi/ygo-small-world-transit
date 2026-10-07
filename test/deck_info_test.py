import pytest
import requests

from src.deck_info import DeckInfo

# 有効・無効なURLを定義
VALID_URL = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2"

def test_fetch_html_success(mocker):
    """デッキ情報取得が成功するケース"""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = b"<html><body>Mock Deck Page</body></html>"

    mocker.patch("requests.get", return_value=mock_response)

    deck_info = DeckInfo(VALID_URL)
    deck_info.fetch_html()

    assert deck_info.html_content is not None
    assert b"Mock Deck Page" in deck_info.html_content


def test_fetch_html_http_error(mocker):
    """HTTPエラー（例えば404）が発生した場合のテスト"""
    mocker.patch("requests.get", side_effect=requests.exceptions.HTTPError("404 Client Error"))

    deck_info = DeckInfo(VALID_URL)
    with pytest.raises(requests.exceptions.HTTPError, match="404 Client Error"):
        deck_info.fetch_html()


@pytest.mark.parametrize(
    ("url", "expected_url"),
    [
        (
            "http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2#deck",
            "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2",
        ),
        (
            "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2",
            "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2",
        ),
    ],
)
def test_fetch_html_normalizes_allowed_url(mocker, url, expected_url):
    response = mocker.Mock()
    response.status_code = 200
    response.content = b"<html>Deck</html>"
    get = mocker.patch("requests.get", return_value=response)

    deck_info = DeckInfo(url)
    deck_info.fetch_html()

    get.assert_called_once_with(expected_url, allow_redirects=False, timeout=(5, 15))
    assert deck_info.html_content == response.content


@pytest.mark.parametrize(
    "url",
    [
        "https://attacker.example/yugiohdb/member_deck.action?cgid=1&dno=2",
        "https://user@www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2",
        "https://www.db.yugioh-card.com:443/yugiohdb/member_deck.action?cgid=1&dno=2",
        "https://www.db.yugioh-card.com/yugiohdb/other.action?cgid=1&dno=2",
        "https://www.db.yugioh-card.com/yugiohdb/../member_deck.action?cgid=1&dno=2",
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action/../../card_search.action",
        "https://www.db.yugioh-card.com/yugiohdb/member_deck.action.extra?cgid=1&dno=2",
        "ftp://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1&dno=2",
    ],
)
def test_fetch_html_rejects_untrusted_url_without_request(mocker, url):
    get = mocker.patch("requests.get")

    with pytest.raises(ValueError):
        DeckInfo(url).fetch_html()

    get.assert_not_called()


@pytest.mark.parametrize("url", [
    "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?dno=2",
    "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=1",
    "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=&dno=2",
])
def test_fetch_html_rejects_url_without_deck_identity(mocker, url):
    get = mocker.patch("requests.get")

    with pytest.raises(ValueError, match="必須情報（cgid、dno）"):
        DeckInfo(url).fetch_html()

    get.assert_not_called()


@pytest.mark.parametrize("status_code", [301, 302, 303, 304, 307, 308])
def test_fetch_html_rejects_redirect_without_following_it(mocker, status_code):
    response = mocker.Mock()
    response.status_code = status_code
    get = mocker.patch("requests.get", return_value=response)

    with pytest.raises(ValueError, match="デッキ取得先から転送応答が返されました"):
        DeckInfo(VALID_URL).fetch_html()

    get.assert_called_once_with(VALID_URL, allow_redirects=False, timeout=(5, 15))


@pytest.mark.parametrize("status_code", [400, 500])
def test_fetch_html_preserves_http_error_for_error_status(mocker, status_code):
    response = mocker.Mock()
    response.status_code = status_code
    response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        f"{status_code} Client Error"
    )
    mocker.patch("requests.get", return_value=response)

    with pytest.raises(requests.exceptions.HTTPError, match=f"{status_code} Client Error"):
        DeckInfo(VALID_URL).fetch_html()


def test_fetch_html_preserves_connection_error(mocker):
    get = mocker.patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError("connection failed"),
    )

    with pytest.raises(requests.exceptions.ConnectionError, match="connection failed"):
        DeckInfo(VALID_URL).fetch_html()

    get.assert_called_once_with(VALID_URL, allow_redirects=False, timeout=(5, 15))


if __name__ == "__main__":
    pytest.main()
