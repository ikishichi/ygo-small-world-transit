import pytest

from src.html_parser import DeckStructureError, HtmlParser, NoMonsterError


MONSTER_HTML = """<div id="detailtext_main">
  <div class="mlist_m t_body">
    <div class="extra t_row c_normal">
      <span class="card_name">テストモンスター</span>
      <span class="box_card_attribute"><span>光属性</span></span>
      <span class="box_card_level_rank level"><span>レベル 4</span></span>
      <span class="card_info_species_and_other_item">【戦士族／通常】</span>
      <span class="atk_power"><span>攻撃力 1500</span></span>
      <span class="def_power"><span>守備力 1200</span></span>
    </div>
  </div>
</div>"""


class TestHtmlParser:
    # get_deck_name()正常系テストのデータ
    get_deck_name_normal_test_data = [
        {
            "title": "正常系_デッキ名取得",
            "html": """<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <meta name="description" content="テストデッキ/ ">
                </head></html>""",
            "expected": "テストデッキ"
        }
    ]

    @pytest.mark.parametrize("test_data", get_deck_name_normal_test_data)
    def test_get_deck_name_normal(self, test_data):
        """
        get_deck_name()正常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        actual = parser.get_deck_name()

        # 検証
        assert actual == test_data["expected"], test_data["title"]

    # get_deck_name()異常系テストのデータ
    get_deck_name_exception_test_data = [
        {
            "title": "異常系_デッキ名取得",
            "html": """<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <meta name="TEST" content="テストデッキ/ ">
                </head></html>""",
            "err_msg": "デッキ名を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
        }
    ]

    @pytest.mark.parametrize("test_data", get_deck_name_exception_test_data)
    def test_get_deck_name_exception(self, test_data):
        """
        get_deck_name()異常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        with pytest.raises(AttributeError) as e:
            parser.get_deck_name()

        # 検証
        assert str(e.value) == test_data["err_msg"], test_data["title"]

    # generate_monsters()正常系テストのデータ
    generate_monsters_normal_test_data = [
        {
            "title": "正常系_モンスターを1種類以上含む",
            "html": """<html>
<head>
	<div id="detailtext_main" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>メインデッキ</h3>
				<span>40</span>
	
			</div>
		</div>

		<div id="main_m_list" class="list">
	
			<div class="t_haed">
				<div class="status flex_1"><span>モンスターカード</span></div>
				<div class="cards_num_set"><span>6</span></div>
			</div>
			<div class="t_body mlist_m">
		
				
				
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">1</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_0_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">夢幻崩界イヴリース</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13571">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
										<span>闇属性</span>
									</span>
		
		

		
		
			
			
									<span class="box_card_level_rank level">
										<img class="icon_img" src="external/image/parts/icon_level.png" alt="レベル" title="レベル">
										<span>レベル 2</span>
									</span>
			
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 0</span>
									</span>


									<span class="def_power"><span>
			
			
										守備力 0
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名の③の効果は１ターンに１度しか使用できない。①：このカードが召喚に成功した時、自分の墓地のリンクモンスター１体を対象として発動できる。そのモンスターの攻撃力を０にし、効果を無効にして、このカードとリンク状態となるように自分フィールドに特殊召喚する。②：このカードがモンスターゾーンに存在する限り、このカードのコントローラーはリンクモンスターしか特殊召喚できない。③：このカードが自分フィールドから墓地へ送られた場合に発動できる。このカードを相手フィールドに守備表示で特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13571">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				
				
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">2</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_1_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">斬機サーキュラー</span>

								</dd>


								<dd class="icon top_set ">
		
									<div class="lr_icon fl fl_2">
				
				
										<p>制限カード</p>
										<span>制限カード</span>
				
				
									</div>
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="17430">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
										<span>光属性</span>
									</span>
		
		

		
		
			
			
									<span class="box_card_level_rank level">
										<img class="icon_img" src="external/image/parts/icon_level.png" alt="レベル" title="レベル">
										<span>レベル 4</span>
									</span>
			
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 1500</span>
									</span>


									<span class="def_power"><span>
			
			
										守備力 1500
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。①：デッキから「斬機サーキュラー」以外の「斬機」モンスター１体を墓地へ送って発動できる。このカードを手札から特殊召喚する。この効果の発動後、ターン終了時まで自分はモンスター１体でしか攻撃できない。②：このカードが既にモンスターゾーンに存在する状態で、自分フィールドに他の「斬機」モンスターが召喚・特殊召喚された場合に発動できる。デッキから「斬機」魔法・罠カード１枚を手札に加える。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value='2'>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=17430">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
			</div>
		</div><!-- .list -->

	</div>
</head>
</html>""",
            "expected": [
                {'name': '夢幻崩界イヴリース', 'attribute': '闇属性', 'type': 'サイバース族', 'level': 'レベル2',
                 'attack': '攻撃力0', 'defence': '守備力0'},
                {'name': '斬機サーキュラー', 'attribute': '光属性', 'type': 'サイバース族', 'level': 'レベル4',
                 'attack': '攻撃力1500', 'defence': '守備力1500'}
            ]
        }
    ]

    @pytest.mark.parametrize("test_data", generate_monsters_normal_test_data)
    def test_generate_monsters_normal(self, test_data):
        """
        generate_monsters()正常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        actual = parser.generate_monsters()

        # 検証
        assert actual == test_data["expected"], test_data["title"]

    # generate_monsters()異常系のテストデータ
    generate_monsters_exception_test_data = [
        {
            "title": "異常系_魔法罠のみ",
            "html": """<html>
<head>
	<div id="detailtext_main" class="card_set">
		<div id="main_m_list" class="list">
	
	

	
	
			<div class="t_haed">
				<div class="status flex_1"><span>魔法カード</span></div>
				<div class="cards_num_set"><span>37</span></div>
			</div>
			<div class="t_body mlist_s">
		
				



					<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">1</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_0_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">墓穴の指名者</span>

								</dd>


								<dd class="icon top_set ">
		
									<div class="lr_icon fl fl_3">
				
				
				
										<p>準制限カード</p>
										<span>準制限カード</span>
				
									</div>
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13619">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		
									<span class="box_card_effect">
										<img class="icon_img" src="external/image/parts/effect/effect_icon_quickplay.png" alt="速攻" title="速攻">
										<span>速攻</span>

										
									</span>
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：相手の墓地のモンスター１体を対象として発動できる。そのモンスターを除外する。次のターンの終了時まで、この効果で除外したモンスター及びそのモンスターと元々のカード名が同じモンスターの効果は無効化される。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value='3'>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13619">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->
			</div>
	
	
	



	
	
			<div class="t_haed">
				<div class="status flex_1"><span>罠カード</span></div>
				<div class="cards_num_set"><span>3</span></div>
			</div>
			<div class="t_body mlist_t">
		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">1</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_0_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">無限泡影</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13631">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
										<span>罠</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									自分フィールドにカードが存在しない場合、このカードの発動は手札からもできる。<br>①：相手フィールドの表側表示モンスター１体を対象として発動できる。そのモンスターの効果をターン終了時まで無効にする。セットされていたこのカードを発動した場合、さらにこのターン、このカードと同じ縦列の他の魔法・罠カードの効果は無効化される。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13631">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
			</div>
	
		</div><!-- .list -->

	</div>
</head>
</html>""",
            "err_msg": "モンスター情報を読み取れませんでした。遊戯王DBのHTML構造が変更された可能性があります。"
        }
    ]

    @pytest.mark.parametrize("test_data", generate_monsters_exception_test_data)
    def test_generate_monsters_exception(self, test_data):
        """
        generate_monsters()異常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        with pytest.raises(DeckStructureError) as e:
            parser.generate_monsters()

        # 検証
        assert str(e.value) == test_data["err_msg"], test_data["title"]

    def test_generate_monsters_accepts_reordered_classes(self):
        """DB側のクラス順序や追加クラスが変わってもカードを解析する。"""
        parser = HtmlParser(MONSTER_HTML)

        assert parser.generate_monsters() == [{
            "name": "テストモンスター",
            "attribute": "光属性",
            "type": "戦士族",
            "level": "レベル4",
            "attack": "攻撃力1500",
            "defence": "守備力1200",
        }]

    @pytest.mark.parametrize("species_text", [
        "【戦士族／通常】", "戦士族／通常", "【戦士族】",
        "\n\t【 戦士族 ／ 効果 】\n",
    ])
    def test_generate_monsters_removes_species_brackets(self, species_text):
        """種族から表示用の括弧を除き、括弧がない形式も受け付ける。"""
        html = MONSTER_HTML.replace("【戦士族／通常】", species_text)

        assert HtmlParser(html).generate_monsters()[0]["type"] == "戦士族"

    @pytest.mark.parametrize("missing_class", [
        "card_name", "box_card_attribute", "box_card_level_rank level",
        "card_info_species_and_other_item", "atk_power", "def_power",
    ])
    def test_generate_monsters_reports_missing_card_field_as_structure_change(self, missing_class):
        """必要なカード項目が欠落した場合は構造変更として識別する。"""
        html = MONSTER_HTML.replace(f'class="{missing_class}"', 'class="unexpected"')

        with pytest.raises(DeckStructureError, match="HTML構造が変更"):
            HtmlParser(html).generate_monsters()

    def test_generate_monsters_reports_changed_row_class_as_structure_change(self):
        html = MONSTER_HTML.replace('class="extra t_row c_normal"', 'class="extra card_row"')

        with pytest.raises(DeckStructureError, match="HTML構造が変更"):
            HtmlParser(html).generate_monsters()

    @pytest.mark.parametrize("html", [
        '<html></html>',
        '<div id="detailtext_main"><div class="t_body mlist_s"></div></div>',
        '<div id="detailtext_main"><div class="t_body mlist_m"></div></div>',
    ])
    def test_generate_monsters_distinguishes_missing_structure_from_empty_monsters(self, html):
        parser = HtmlParser(html)

        if 'class="t_body mlist_m"' not in html:
            with pytest.raises(DeckStructureError):
                parser.generate_monsters()
        else:
            with pytest.raises(NoMonsterError, match="モンスターが見つかりません"):
                parser.generate_monsters()

    @pytest.mark.parametrize("other_list", ["mlist_s", "mlist_t"])
    def test_changed_monster_list_with_other_cards_is_structure_error(self, other_list):
        """魔法・罠の一覧が残っても、モンスター領域の欠落は構造変更とする。"""
        html = MONSTER_HTML.replace("mlist_m", "changed_monsters").replace(
            '</div>\n</div>',
            f'</div><div class="t_body {other_list}"></div>\n</div>',
        )

        with pytest.raises(DeckStructureError, match="HTML構造が変更"):
            HtmlParser(html).generate_monsters()

    @pytest.mark.parametrize("content", [
        '<div class="card_row"><span class="renamed_card">モンスター</span></div>',
        "モンスター情報",
    ], ids=["unknown_elements", "text_only"])
    def test_unknown_monster_content_is_structure_error(self, content):
        """旧クラスが残っていなくても、空でない領域は構造変更とする。"""
        html = (
            '<div id="detailtext_main"><div class="t_body mlist_m">'
            + content + '</div></div>'
        )

        with pytest.raises(DeckStructureError, match="HTML構造が変更"):
            HtmlParser(html).generate_monsters()

    @pytest.mark.parametrize("content", ["", " \n\t ", "<!-- empty -->"])
    def test_empty_monster_region_remains_no_monster(self, content):
        """空白やコメントだけのモンスター領域は従来の分類を維持する。"""
        html = (
            '<div id="detailtext_main"><div class="t_body mlist_m">'
            + content + '</div></div>'
        )

        with pytest.raises(NoMonsterError, match="モンスターが見つかりません"):
            HtmlParser(html).generate_monsters()
