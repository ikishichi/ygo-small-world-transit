class SearchResult:
    def __init__(self, MonsterList, origin, destination):
        """Initialize this class

        Args:
            MonsterList (string): Deck URL
            origin: for Search
            destination: for Search
        """
        self.search_result = []
        # MonsterListの列はname, attribute, type, level, attack, defence

    def get(self):
        return self.search_result