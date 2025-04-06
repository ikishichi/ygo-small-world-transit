"""デッキ情報取得モジュール"""
import requests

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
            response = requests.get(self.url)
            response.raise_for_status() # ステータスコードが200番台（成功）以外の場合に例外をスロー
            self.html_content = response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching deck info: {e}")
            raise
