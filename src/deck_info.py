"""デッキ情報取得モジュール"""
import requests

class DeckInfo:
    """デッキ情報クラス

    Attributes:
        url (string): Deck URL
        html_content (bytes): 取得した公開デッキのhtmlバイナリデータ
    """
    CORRECT_URL_HTTP = 'http://www.db.yugioh-card.com/yugiohdb/member_deck.action'
    CORRECT_URL_HTTPS = 'https://www.db.yugioh-card.com/yugiohdb/member_deck.action'

    def __init__(self, url):
        if not url.startswith(self.CORRECT_URL_HTTP) and not url.startswith(self.CORRECT_URL_HTTPS):
            print(f"無効なURL: {url}")
            raise ValueError("無効なURLです。遊戯王DBの公開デッキレシピのURLを入力してください。")
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
