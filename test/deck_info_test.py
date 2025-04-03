import pytest
import requests

from src.deck_info import DeckInfo

# 有効・無効なURLを定義
VALID_URL = "https://www.db.yugioh-card.com/yugiohdb/member_deck.action?deck_id=123"
INVALID_URL = "https://invalid-url.com"


def test_invalid_url():
    """無効なURLを渡した場合に ValueError が発生するかテスト"""
    with pytest.raises(ValueError, match="無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。"):
        DeckInfo(INVALID_URL)


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


if __name__ == "__main__":
    pytest.main()
