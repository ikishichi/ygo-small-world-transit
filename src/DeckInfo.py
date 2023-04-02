import requests
class DeckInfo:
    def __init__(self, url):
        """Initialize this class

        Args:
            url (string): Deck URL
        """
        self.url = url
        self.html = requests.get(url)

    def success(self):
        """Return true if html got

        Returns:
            bool: html got or not
        """
        ret = False
        if self.html.status_code == 200:
            ret = True
        return ret

    def Get(self):
        return self.html
