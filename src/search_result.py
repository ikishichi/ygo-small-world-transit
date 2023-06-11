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

        """
        print(monster_list[monster_list['name'] == target_name])

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
        #test_pd = pd.DataFrame(['テストマン','光','サイバース','10','100','300'],columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
        test_pd = pd.DataFrame({'name':['テストマン','テストクリボー','LL-テスト・ダック'],
                                'attribute':['光','闇','風'],
                                'type':['サイバース族','悪魔族','鳥獣族'],
                                'level':['10','1','1'],
                                'attack':['100','0','50'],
                                'defence':['300','200','0']})
        print(test_pd)
        print('Go Test __name_search Go')
        self.__name_search(test_pd,'LL-テスト・ダック')
        "return self.search_result"
        return

def main():
    test_pd = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
    sr = SearchResult(test_pd,'test')
    print('Go Test get Go')
    sr.get()

main()