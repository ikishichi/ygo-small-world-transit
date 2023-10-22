"""デッキ内容（DataFrame）管理モジュール"""
import pandas as pd

from html_parser import HtmlParser


class Deck:
    """デッキ内容管理クラス

    Attributes:
        monsters_df (Pandas.DataFrame): メインデッキのモンスターのDataFrame
    """

    def __init__(self, html):
        """Initialize this class

        Args:
            html (bytes): 公開デッキのhtmlバイナリデータ
        """
        try:
            monsters = HtmlParser(html).generate_monsters()
        except Exception as e:
            raise e
        else:
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
