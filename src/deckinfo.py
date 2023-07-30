import requests


class DeckInfo:
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
            self.htmlinfo = requests.get(url)
            if self.STATUS_CODE_SUCCESS == self.htmlinfo.status_code:
                self.gets_html = True

    def is_success(self):
        """Return true if html got

        Returns:
            bool: html got or not
        """
        if True == self.gets_html:
            return True
        return False

    def get(self):
        return self.htmlinfo.content
