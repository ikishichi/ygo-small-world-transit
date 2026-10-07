"""デッキ情報取得モジュール"""
import logging

logger = logging.getLogger(__name__)

import requests

try:
    from .url_resolver import normalize_deck_url
except ImportError:
    from url_resolver import normalize_deck_url


class DeckInfo:
    """デッキ情報クラス

    Attributes:
        url (string): Deck URL
        html_content (bytes): 取得した公開デッキのhtmlバイナリデータ
    """

    def __init__(self, url):
        self.url = url
        self.html_content = None

    def fetch_html(self):
        """Fetch HTML content"""
        try:
            url = normalize_deck_url(self.url)
            response = requests.get(url, allow_redirects=False)
            if 300 <= response.status_code < 400:
                raise ValueError("デッキ取得先から転送応答が返されました")
            response.raise_for_status()
            self.html_content = response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching deck info: {e}")
            raise
