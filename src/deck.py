# -*- coding: utf-8 -*-
"""デッキ情報管理クラス"""
import requests
from bs4 import BeautifulSoup


class Deck:
    def __init__(self, html):
        """Initialize this class

        Args:
            html (Response): デッキレシピのhtml
        """