"""デッキ情報管理クラス"""
from html_parser import HtmlParser
import pandas as pd


class Deck:
    def __init__(self, html):
        """Initialize this class

        Args:
            html (Response): デッキレシピのhtml
        """
        monsters = HtmlParser(html).get_monster_info_list()
        self.monsters_df = self.convert_monsters_to_df(monsters)

    @staticmethod
    def convert_monsters_to_df(monsters):
        """モンスター情報のリストをPandas.DataFrameに変換する

        Args:
            monsters (list[dict[str, str]]): メインデッキのモンスター情報のリスト

        Returns:
            pd.DataFrame: メインデッキのモンスター情報のPandas.DataFrame
        """
        monsters_df = pd.DataFrame(monsters)

        return monsters_df

    def get_monsters_df(self):
        """モンスター情報のDataFrameのGetter

        Returns:
            pd.DataFrame: メインデッキのモンスター情報のPandas.DataFrame
        """
        return self.monsters_df
