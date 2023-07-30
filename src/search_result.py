import pandas as pd
class SearchResult:
    def __init__(self, monster_list: pd.DataFrame, origin, destination=''):
        """Initialize this class
        Args:
            monster_list: (pandas) name, attribute, type, level, attack, defence
            origin: for Search
            destination: for Search
        """
        self.search_result = [[]]
        self.monster_list = monster_list
        self.origin = origin
        self.destination = destination

    def __name_search(self, monster_list: pd.DataFrame, target_name):
        """
            Return rows as pandas.Series type which contain strings matching target_name.
        Args:
            monster_list: (pandas) name, attribute, type, level, attack, defence
            target_name: for Search
        Return:
            monster data with matching name
        """
        return monster_list[monster_list['name'] == target_name]

    def get(self):
        """Get search result

        Args:
            monster_list: (pandas) name, attribute, type, level, attack, defence
            origin: for Search
            destination: for Search
        Return:
            2D list about destinations and transit points
            [search_dest_A, [transit_1, transit_2, transit_3, ...]], 
            [search_dest_B, [transit_1, transit_2, transit_3, ...]],
            [search_dest_C, [transit_1, transit_2, transit_3, ...]],
            ...
        """
        name_search_result = self.__name_search(self.monster_list, self.origin)
        return name_search_result