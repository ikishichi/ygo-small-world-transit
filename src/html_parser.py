"""HTMLパーサーモジュール"""
from bs4 import BeautifulSoup


class DeckStructureError(AttributeError):
    """遊戯王DBのデッキHTMLから必要な構造を取得できない場合の例外。"""


class NoMonsterError(ValueError):
    """デッキにメインデッキのモンスターが含まれない場合の例外。"""


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
            DeckStructureError: デッキ名のタグを取得できなかった場合に発生
        """

        meta_tag = self.soup.find("meta", attrs={"name": "description"})
        if not meta_tag or "content" not in meta_tag.attrs:
            raise DeckStructureError(
                "デッキ名を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
            )

        return meta_tag["content"].strip(" /")  # 末尾の不要なスラッシュと空白を削除

    def generate_monsters(self):
        """メインデッキ内のモンスターのリストを生成する

        Returns:
            list[dict[str, str]]: メインデッキのモンスター情報のリスト

        Raises:
            DeckStructureError: デッキHTMLの構造やモンスター項目を読み取れない場合に発生
            NoMonsterError: メインデッキにモンスターが含まれない場合に発生
        """

        main_deck_soup = self.soup.find(id="detailtext_main")
        if main_deck_soup is None:
            raise DeckStructureError(
                "デッキ情報を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
            )

        # 領域の欠落だけではモンスター0体と断定できないため、構造変更とする。
        main_monsters_soup = main_deck_soup.select_one(".t_body.mlist_m")
        if main_monsters_soup is None:
            raise DeckStructureError(
                "モンスター情報を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
            )

        monster_soups = main_monsters_soup.select(".t_row.c_normal")
        if not monster_soups:
            if main_monsters_soup.select_one(".t_row, .card_name"):
                raise DeckStructureError(
                    "モンスター情報を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
                )
            raise NoMonsterError("メインデッキにモンスターが見つかりませんでした。")

        # モンスター1体毎のパラメータの辞書を作成し、リストに格納
        monsters: list[dict[str, str]] = []
        for monster_soup in monster_soups:
            # 各パラメータのタグを取得。要素が欠けている場合は構造変更として扱う。
            name_tag = monster_soup.select_one("span.card_name")
            attribute_tag = monster_soup.select_one("span.box_card_attribute span")
            level_tag = monster_soup.select_one("span.box_card_level_rank.level span")
            type_tag = monster_soup.select_one("span.card_info_species_and_other_item")
            attack_tag = monster_soup.select_one("span.atk_power span")
            defence_tag = monster_soup.select_one("span.def_power span")
            tags = [name_tag, attribute_tag, level_tag, type_tag, attack_tag, defence_tag]
            if any(tag is None for tag in tags):
                raise DeckStructureError(
                    "モンスター情報を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
                )

            name = name_tag.get_text()
            attribute = attribute_tag.get_text()
            level = level_tag.get_text()
            type_ = type_tag.get_text()
            attack = attack_tag.get_text()
            defence = defence_tag.get_text()

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
