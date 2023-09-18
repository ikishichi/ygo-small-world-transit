import pandas as pd
import numpy as np
class SearchResult:
    def __init__(self, monsters_df: pd.DataFrame, origin, destination=''):
        """Initialize this class
        Args:
            monsters_df: (pandas) name, attribute, type, level, attack, defence
            origin: for Search
            destination: for Search
        """
        self.search_result = [[]]
        self.monsters_df = monsters_df
        self.origin = origin
        self.destination = destination

    def __get_monster_data_with_name(self, monsters_df: pd.DataFrame, target_name):
        """
            Return rows as pandas.Series type which contain strings matching target_name.
        Args:
            monsters_df: (pandas) name, attribute, type, level, attack, defence
            target_name: for Search
        Return:
            monster data with matching name (ndarray)
        """
        return monsters_df[monsters_df['name'] == target_name].iloc[0]

    def __get_monster_data_with_only_one_matching(self, monsters_df: pd.DataFrame, target_monster_data: np.ndarray):
        """
            Return rows as pandas.Series type which contain only one matching data with target_monster_data.
        Args:
            monsters_df: (pandas) name, attribute, type, level, attack, defence
            target_monster_data: (pandas) name, attribute, type, level, attack, defence. for Search
        Return:
            monster list
        """
        # monsters_dfの一行ずつとtarget_monster_dataを突き合わせて、一つだけ一致するデータを取得し、リターン用のpd.DataFrameに格納する。
        result = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
        #monsters_dfから1行ずつ比較
        for index, row in monsters_df.iterrows():
            match_count = 0
            # 1要素だけ一致するデータを探す
            for column_name in row.index:
                if row[column_name] == target_monster_data[column_name]:
                    match_count += 1
                if match_count > 1:
                    break
            if match_count == 1:
                result = pd.concat([result, row.to_frame().T])
        return result

    def get(self):
        """Get search result

        Args:
            monsters_df: (pandas) name, attribute, type, level, attack, defence
            origin: for Search
            destination: for Search
        Return:
            2D list about origin and transit points, destinations: pandas.dataframe
            [
                [search_origin_A, transit_A, search_dest_A], 
                [search_origin_A, transit_B, search_dest_A], 
                [search_origin_A, transit_C, search_dest_B], ...
            ]
        """
        name_search_result = self.__get_monster_data_with_name(self.monsters_df, self.origin)
        transit_data = self.__get_monster_data_with_only_one_matching(self.monsters_df, name_search_result)
        # 結果を格納する配列
        result = pd.DataFrame(columns=['origin','transit','dest'])
        # 中継データごとに検索する
        for transit_index,transit_row in transit_data.iterrows():
            dest_data = self.__get_monster_data_with_only_one_matching(self.monsters_df, transit_row)
            for dest_index,dest_row in dest_data.iterrows():
                if self.origin != dest_row['name']:
                    result_data = pd.DataFrame({'origin':[self.origin],'transit':[transit_row['name']],'dest':[dest_row['name']]})
                    result = pd.concat([result,result_data])
        return result