import requests
class DeckInfo:
    def __init__(self, url):
        """Initialize this class

        Args:
            url (string): Deck URL
        """
        self.gets_html = False
        correct_url = 'https://www.db.yugioh-card.com/yugiohdb/'
        if True == url.startswith(correct_url):
            self.html = requests.get(url)
            STATUS_CODE_SUCCESS = 200
            if STATUS_CODE_SUCCESS == self.html.status_code:
                self.gets_html = True

    def success(self):
        """Return true if html got

        Returns:
            bool: html got or not
        """
        ret = False
        if True == self.gets_html:
            ret = True
        return ret

    def Get(self):
        return self.html
