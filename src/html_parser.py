"""HTMLパーサーモジュール"""
import logging

from bs4 import BeautifulSoup


class HtmlParser:
    """公開デッキのHTMLからモンスターリストを作成するパーサークラス

    Attributes:
        soup (BeautifulSoup): 公開デッキの解析データ
    """

    def __init__(self, html):
        # htmlをsoupオブジェクトに変換
        self.soup = BeautifulSoup(html, "lxml")

    def get_deck_name(self):
        """デッキ名を取得する

        Returns:
            (str): 公開デッキのデッキ名

        Raises:
            AttributeError: デッキ名のタグを取得できなかった場合に発生
        """

        try:
            # htmlをsoupオブジェクトに変換
            meta_tag = self.soup.find("meta", attrs={"name": "description"})
            if not meta_tag or "content" not in meta_tag.attrs:
                raise AttributeError("デッキ名の取得に失敗しました。HTML構造が変更された可能性があります。")

            return meta_tag["content"].strip(" /")  # 末尾の不要なスラッシュと空白を削除

        except AttributeError as e:
            logging.error(f"デッキ名取得失敗:{e}")
            raise AttributeError("デッキの読み込みに失敗しました")
        except Exception as e:
            logging.error(f"デッキ名取得失敗:{e}")
            raise

    def generate_monsters(self):
        """メインデッキ内のモンスターのリストを生成する

        Returns:
            list[dict[str, str]]: メインデッキのモンスター情報のリスト

        Raises:
            AttributeError: モンスター情報のタグを取得できなかった場合に発生
        """

        try:
            # メインデッキ内の最初のt_bodyからsoupを抽出（モンスターが含まれる場合、モンスターのsoupが抽出される）
            main_monsters_soup = self.soup.find(id="detailtext_main").find("div", class_="t_body mlist_m")

            # モンスター1体毎のsoupに分解
            monster_soups = main_monsters_soup.select("[class='t_row c_normal']")

            # モンスター1体毎のパラメータの辞書を作成し、リストに格納
            monsters: list[dict[str, str]] = []
            for monster_soup in monster_soups:
                # 各パラメータのタグを取得
                name = monster_soup.find("span", class_="card_name").text
                attribute = monster_soup.find("span", class_="box_card_attribute").find("span").text
                level = monster_soup.find("span", class_="box_card_level_rank level").find("span").text
                type_ = monster_soup.find("span", class_="card_info_species_and_other_item").text
                attack = monster_soup.find("span", class_="atk_power").find("span").text
                defence = monster_soup.find("span", class_="def_power").find("span").text

                if None in [name, attribute, level, type_, attack, defence]:
                    raise AttributeError("モンスターのパラメータ取得に失敗しました。HTML構造が変更された可能性があります。")

                # 改行やタブを削除
                attribute = "".join(attribute.split())
                type_ = "".join(type_.split()).split('／')[0]
                level = "".join(level.split())
                attack = "".join(attack.split())
                defence = "".join(defence.split())

                # 辞書に格納
                monster_dct = {
                    "name": name,
                    "attribute": attribute,
                    "type": type_,
                    "level": level,
                    "attack": attack,
                    "defence": defence
                }

                # リストに追加
                monsters.append(monster_dct)

            return monsters
        except AttributeError as e:
            logging.error(f"モンスター取得失敗:{e}")
            raise AttributeError("デッキの読み込みに失敗しました")
        except Exception as e:
            logging.error(f"モンスター取得失敗:{e}")
            raise
