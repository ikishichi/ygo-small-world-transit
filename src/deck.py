"""デッキ内容（DataFrame）管理モジュール"""
import pandas as pd

from html_parser import HtmlParser


class Deck:
    """デッキ内容管理クラス

    Attributes:
        html (bytes): 公開デッキのhtmlバイナリデータ
        monsters_df (Pandas.DataFrame): メインデッキのモンスターのDataFrame
    """

    def __init__(self, html):
        self.html = html
        self.monsters_df = None

    def parse_html(self):
        """HTMLを解析し、モンスター情報を取得"""
        try:
            monsters = HtmlParser(self.html).generate_monsters()
            self.monsters_df = self.convert_monsters_to_df(monsters)
        except Exception:
            raise

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
