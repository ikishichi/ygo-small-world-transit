# -*- coding: utf-8 -*-
"""デッキ情報管理クラス"""
import html_parser
import pandas as pd


class Deck:
    def __init__(self, html):
        """Initialize this class

        Args:
            html (Response): デッキレシピのhtml
        """
        parser = html_parser.HtmlParser(html)
        monsters = parser.get_monster_info_list()

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
