"""HTMLパーサークラス"""
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, html):
        """Initialize this class

        Args:
            html (Response): デッキレシピのhtml
        """
        monster_soups = self.generate_monster_soups(html)
        self.monsters = self.generate_monsters(monster_soups)

    def get_monster_info_list(self):
        """メインデッキのモンスター情報のGetter

        Returns:
            list[dict[str, str]]: メインデッキのモンスター情報のリスト
        """
        return self.monsters

    @staticmethod
    def generate_monster_soups(html):
        """メインデッキのモンスター1体毎のsoupのリストを生成する

        Args:
            html (Response): デッキレシピのhtml

        Returns:
            ResultSet[Tag] :モンスター1体毎のsoup
        """
        # htmlをsoupオブジェクトに変換
        soup = BeautifulSoup(html.content, "html.parser")

        # メインデッキのモンスターのみのsoupを生成
        main_monsters_soup = soup.find(id="detailtext_main").find("div", class_="t_body")

        # モンスター1体毎のsoupに分解
        monster_soups = main_monsters_soup.select("[class='t_row c_simple']")

        return monster_soups

    @staticmethod
    def generate_monsters(monster_soups):
        """メインデッキ内のモンスターのリストを生成する

        Args:
            monster_soups (ResultSet[Tag]): モンスター1体毎のsoup

        Returns:
            list[dict[str, str]]: メインデッキのモンスター情報のリスト

        Raises:
            AttributeError: モンスター情報のタグを取得できなかった場合に発生
        """
        try:
            # モンスター1体毎のパラメータの辞書を作成し、リストに格納
            monsters: list[dict[str, str]] = []
            for monster_soup in monster_soups:
                # 各パラメータのタグを取得
                name = monster_soup.find("span", class_="name").text
                attribute = monster_soup.find("div", class_="item_set").find("span").text
                type_ = monster_soup.find("div", class_="flex_2 other").find("span").text
                level = monster_soup.find("div", class_="num_set flex_1").find("span").text
                attack = monster_soup.select("div.inside > div.element > div.num_set.flex_1 > div > span:nth-child(1)")[0].text
                defence = monster_soup.select("div.inside > div.element > div.num_set.flex_1 > div > span:nth-child(2)")[0].text

                # 改行やタブを削除
                attribute = "".join(attribute.split())
                type_ = "".join(type_.split())
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
        except AttributeError:
            print("AttributeError: メインデッキのモンスター情報が正しく取得できませんでした。")
            raise AttributeError("メインデッキのモンスター情報が正しく取得できませんでした。")
        except Exception as e:
            print("予期せぬ例外が発生しました")
            print(e)
            raise e


