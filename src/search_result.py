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

    def __name_search(self, monster_list: pd.DataFrame, target_name):
        monster_list

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
        return self.search_result