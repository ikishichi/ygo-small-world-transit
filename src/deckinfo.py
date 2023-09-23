"""デッキ情報取得モジュール"""
import requests


class DeckInfo:
    """デッキ情報クラス

    Attributes:
        gets_html (bool): デッキ情報の取得結果
        html_info (bytes): 取得した公開デッキのhtmlバイナリデータ
    """
    STATUS_CODE_SUCCESS = 200
    CORRECT_URL_HTTP = 'http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid='
    CORRECT_URL_HTTPS = 'https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid='

    def __init__(self, url):
        """Initialize this class

        Args:
            url (string): Deck URL
        """
        self.gets_html = False
        if url.startswith(self.CORRECT_URL_HTTP) or url.startswith(self.CORRECT_URL_HTTPS):
            self.html_info = requests.get(url)
            if self.STATUS_CODE_SUCCESS == self.html_info.status_code:
                self.gets_html = True

    def is_success(self):
        """Return true if html got

        Returns:
            bool: html got or not
        """
        if self.gets_html is True:
            return True
        return False

    def get(self):
        """Getter of the response data

        Returns:
            bytes: Content of the response(binary)
        """
        return self.html_info.content
