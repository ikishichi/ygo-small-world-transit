# -*- coding: utf-8 -*-
"""デッキ情報管理クラス"""
import html_parser


class Deck:
    def __init__(self, html):
        """Initialize this class

        Args:
            html (Response): デッキレシピのhtml
        """

        parser = html_parser.HtmlParser(html)
        monsters = parser.get_monster_info_list()

    def convert_monsters_to_df(self, monsters):
