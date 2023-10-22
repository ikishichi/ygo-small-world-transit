import pytest

from src.html_parser import HtmlParser


class TestHtmlParser:
    # generate_monsters()正常系テストのデータ
    generate_monsters_normal_test_datas = [
        {
            "note": "正常系_モンスターを1種類以上含む",
            "html": """<html>
<head>




	<meta http-equiv="x-ua-compatible" content="IE=10" >
	<meta http-equiv="x-ua-compatible" content="IE=EmulateIE10" >

	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<meta http-equiv="Content-Language" content="ja">
	<meta http-equiv="Content-Style-Type" content="text/css">
	<meta http-equiv="Content-Script-Type" content="text/javascript">
	<meta http-equiv="imagetoolbar" content="no">
	<meta name="format-detection" content="telephone=no">

	<meta property="og:site_name" content="遊戯王OCGカードデータベース">

	<meta property="og:type" content="product" />
	<meta property="og:locale" content="ja_JP" />

	<meta name="twitter:card" content="summary"/>

	<script type="text/javascript" src="/yugiohdb/ga.js"></script>
	<meta name="copyright" content="KONAMI">
	<link rel="shortcut icon" href="external/image/yugioh.ico">
	<link rel="apple-touch-icon" href="external/image/apple-touch-icon.png">


	


	


	


	<meta name="keywords" content="モンスター2種,遊戯王,デッキ,デュエルモンスターズ,VRAINS,ヴレインズ,禁止,制限,パック,禁止カード,カード,カードリスト,ルール,OCG,コナミ,KONAMI">
	<meta name="description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細">
	<meta property="title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">

	<meta property="og:title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">
	<meta property="og:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202309232316"/>

	<meta property="og:description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細" />

	<meta name="twitter:title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース" />
	<meta name="twitter:description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細" />

	<meta name="twitter:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202309232316" />

	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">



	


	<title>遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</title>



<!--[if lt IE 9]>
	<script type="text/javascript" src="external/html5/js/html5shiv.js"></script>
<![endif]-->
	<script type="text/javascript" src="external/jquery/jquery-3.6.0.js"></script>

	<script type="text/javascript" src="external/jquery/jquery-ui-1.13.1.custom/jquery-ui.js"></script>

	<script type="text/javascript" src="external/js/common.js"></script>

	<script type="text/javascript" src="external/jquery/scrolltopcontrol.js"></script>


<script src="external/js/jquery.autosize.js" type="text/javascript"></script>



	<!--link type="text/css" rel="stylesheet" href="external/jquery/jquery-ui-1.8.16.custom/css/ui-lightness/jquery-ui-1.8.16.custom.css"-->
	<link type="text/css" rel="stylesheet" href="external/jquery/jquery-ui-1.13.1.custom/jquery-ui.css">

	<link type="text/css" rel="stylesheet" href="external/css/common.css?20171030">

	<link rel="stylesheet" type="text/css" href="external/css/MemberDeckDetail.css">



<meta property='og:image' content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&osplang=1&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&app=tournament&request_locale=ja&a=202309232316" />
<meta name='twitter:image' content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&osplang=1&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&app=tournament&request_locale=ja&a=202309232316" />


<script type="text/javascript">
<!--

	$(function(){
		

		$('#dno').val('70');
		$('#dno').change(function() {
			var value = $(this).val();
			
			location.href='/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=' + value + '&request_locale=ja';
		});
		$('#sort').val('1');
		$('#sort').change(function() {
			var value = $(this).val();
		        var str = $(this).val();
		        $(this).parents('form').submit();
		});
		$('.tablink li.'+'2').addClass("now");
		$('#deck_display').val('2');

		$('#deck_display').change(function() {
			var value = $(this).val();
			
			$('#deck_image,#deck_detailtext,#deck_text').hide();

			$('.tablink li').removeClass("now");
			$('.tablink li.'+value).addClass("now");
			switch (value) {
			case '1':
				$('#deck_text').show();
				$("#num_total_m").attr("href", "#monster_list");
				$("#num_total_e").attr("href", "#extra_list");
				$("#num_total_s").attr("href", "#side_list");
				break;
			case '2':
				$('#deck_image').show();
				$("#num_total_m").attr("href", "#main");
				$("#num_total_e").attr("href", "#extra");
				$("#num_total_s").attr("href", "#side");
				break;
			case '3':
				$('#deck_detailtext').show();
				$("#num_total_m").attr("href", "#detailtext_main");
				$("#num_total_e").attr("href", "#detailtext_ext");
				$("#num_total_s").attr("href", "#detailtext_side");

				break;
			}

		});
		$('.tablink li').click(function(){
			$('.tablink li').removeClass("now");
			clm = $(this).attr("class");

			$('#deck_display').val(clm);
			$('#deck_display').trigger('change');
		});


		
		
			
				$('#detailtext_main .mlist_m #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg').show();

				$('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
				$('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
				$('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_m #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ').show();

				$('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
				$('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
				$('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
			
		
		
			
				$('#detailtext_main .mlist_s #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw').show();

				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ').show();

				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_2_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag').show();

				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_3_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ').show();

				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_4_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ').show();

				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_5_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A').show();

				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_6_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg').show();

				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_7_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ').show();

				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
			
		
		
			
				$('#detailtext_main .mlist_t #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A').show();

				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_t #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg').show();

				$('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
				$('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
				$('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_t #card_image_2_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ').show();

				$('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
				$('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
				$('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_t #card_image_3_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA').show();

				$('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
				$('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
				$('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_t #card_image_4_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w').show();

				$('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
				$('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
				$('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
			
		
		
			
				$('#detailtext_ext #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA').show();

				$('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
				$('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
				$('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA').show();

				$('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
				$('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
				$('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_2_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw').show();

				$('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
				$('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
				$('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_3_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw').show();

				$('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
				$('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
				$('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_4_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw').show();

				$('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
				$('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
				$('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_5_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww').show();

				$('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
				$('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
				$('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_6_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA').show();

				$('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
				$('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
				$('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_7_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ').show();

				$('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
				$('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
				$('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_8_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg').show();

				$('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
				$('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
				$('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_9_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ').show();

				$('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
				$('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
				$('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_10_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA').show();

				$('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
				$('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
				$('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
			
		
			
				$('#detailtext_ext #card_image_11_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw').show();

				$('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
				$('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
				$('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
			
		
		
			

				$('#detailtext_side #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA').show();

				$('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
				$('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
				$('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
			
		
			

				$('#detailtext_side #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA').show();

				$('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
				$('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
				$('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
			
		
			

				$('#detailtext_side #card_image_2_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14542&ciid=1&enc=Vkx-oXbBI_oMi6rpDuY3Zg').show();

				$('.card_image_side_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14542&ciid=1&enc=Vkx-oXbBI_oMi6rpDuY3Zg&osplang=1').show();
				$('.card_image_side_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14542&ciid=1&enc=Vkx-oXbBI_oMi6rpDuY3Zg&osplang=1').show();
				$('.card_image_side_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14542&ciid=1&enc=Vkx-oXbBI_oMi6rpDuY3Zg&osplang=1').show();
			
		

		
		$('.deck_list tr.row,.list .t_row').click(function() {
			window.open($('.link_value', this).val());
		});

		$('textarea').autosize();


	});

	
	$(document).ready(function(){
		
		var value = '2';

		$('#deck_image,#deck_detailtext,#deck_text').hide();

		switch (value) {
		case '1':
			$('#deck_text').show();
			$("#num_total_m").attr("href", "#monster_list");
			$("#num_total_e").attr("href", "#extra_list");
			$("#num_total_s").attr("href", "#side_list");
			break;
		case '2':
			$('#deck_image').show();
				$("#num_total_m").attr("href", "#main");
				$("#num_total_e").attr("href", "#extra");
				$("#num_total_s").attr("href", "#side");
			break;
		case '3':
			$('#deck_detailtext').show();
				$("#num_total_m").attr("href", "#detailtext_main");
				$("#num_total_e").attr("href", "#detailtext_ext");
				$("#num_total_s").attr("href", "#detailtext_side");
			break;
		default:
			break;
		}
		
	});

	function DeckDelete(){
		if(window.confirm('このデッキを削除しますか？')){
			location.href = "/yugiohdb/member_deck.action?ope=7&wname=MemberDeck&ytkn=bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja";
		}
	}

	function updateDeckFavorite(){
		var chngeFavoriteCnt = document.getElementById("favoriteCnt");
		var mycount = 1;
		if (deckFavorite.checked) {
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=9&wname=MemberDeck&ytkn=bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			if (false) {
				mycount = 0; //自分が登録済み
			}
			chngeFavoriteCnt.innerHTML = 0 + mycount;
		} else{
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=10&wname=MemberDeck&ytkn=bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			if (true) {
				mycount = 0; //自分が登録済み
			}
			chngeFavoriteCnt.innerHTML = 0 - mycount;

		}
	}
	function updateDeckLikes(){
		var chngelikesCnt = document.getElementById("likesCnt");
		var likesCnt = document.getElementById("deckLikesCnt"); 
		var usrLiksCnt = document.getElementById("usrLikesCnt");
		var chkMaxCnt = document.getElementById("deckLikesUsrCnt");
		if ( Number( chkMaxCnt.value) < 5 ) {
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=11&wname=MemberDeck&ytkn=bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			likesCnt.value = Number(likesCnt.value) + 1;
			chkMaxCnt.value = Number(chkMaxCnt.value) + 1;
			chngelikesCnt.innerHTML = likesCnt.value;
			usrLiksCnt.innerHTML = chkMaxCnt.value;
		} else {
			crearDeckLikes();

			likesCnt.value = Number(likesCnt.value) - 5;
			chngelikesCnt.innerHTML = likesCnt.value;
			chkMaxCnt.value = 0;         
			usrLiksCnt.innerHTML = 0; 
		}
	}
	function crearDeckLikes(){
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=12&wname=MemberDeck&ytkn=bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
	}

//-->
</script>




	

<body class="ja">

<div id="wrapper">
	<header>
		<div id="header_meta">
			<a href="https://www.konami.com/games/jp/ja/" target="_blank"><img src="https://www.yugioh-card.com/ci/logo/konami_logo_normal.png" alt="KONAMI" id="konami" class="ui-draggable"></a>

			
			<nav id="language">
				
				<span  class="hex2_1 orn"><span class="hex2_2">
					日本語
					
					
					
					
					
			 		
			 		
			 		
				</span></span>
				
				<div id="lang_mane">
					<div>
						<p>OCG</p>
						<ul>
							<li><a href="javascript:ChangeLanguage('ja')" class="current">日本語</a></li>
							<li><a href="javascript:ChangeLanguage('ko')" >한글</a></li>
	
							
						</ul>
					</div>
					<div>
						<p>TCG</p>
						<ul>
							<li><a href="javascript:ChangeLanguage('en')" >English</a></li>
							<li><a href="javascript:ChangeLanguage('de')" >Deutsch</a></li>
							<li><a href="javascript:ChangeLanguage('fr')" >Fran&ccedil;ais</a></li>
							<li><a href="javascript:ChangeLanguage('it')" >Italiano</a></li>
							<li><a href="javascript:ChangeLanguage('es')" >Espa&ntilde;ol</a></li>
							<li><a href="javascript:ChangeLanguage('pt')" >Portugues</a></li>
						</ul>
					</div>

				</div>
			</nav>

		</div><!--#header_meta-->


		<div id="header_menu">
			<nav>
				<dl id="menber_menu">
	
	
	
	
					<dd class="rogin">
						<div class="rogin_btn">
							
							<div class="hex2_1 my"><div class="hex2_2"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path  d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"/></svg>ログイン中 <span>[0039904244]</span></div></div>
							
							<a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"/></svg>ログアウト</span></a>
						</div>
					</dd>
	
					<dd class="logo"></dd>
					
					<dd class="forbidden_limited">
						<a class="btn hex pnk"  href="/yugiohdb/forbidden_limited.action">
							<span>
								<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>

								<h3>リミットレギュレーション</h3>
								
							</span>
						</a>
					</dd>
				</dl><!-- #menber_menu -->
				
				<div class="bottom">
					<div id="spnav_btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41.59 31"><defs></defs><path  d="M2.63,0H39a2.64,2.64,0,0,1,2.64,2.63h0A2.63,2.63,0,0,1,39,5.26H2.63A2.63,2.63,0,0,1,0,2.63H0A2.63,2.63,0,0,1,2.63,0Z"/><path  d="M2.63,12.87H39a2.64,2.64,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,18.13H2.63A2.63,2.63,0,0,1,0,15.5H0A2.63,2.63,0,0,1,2.63,12.87Z"/><path d="M2.63,25.74H39a2.63,2.63,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,31H2.63A2.63,2.63,0,0,1,0,28.37H0A2.63,2.63,0,0,1,2.63,25.74Z"/></svg></div>
					


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

				</div>

			</nav>
		</div><!-- #header_menu-->
	</header>
	<div id="spnav">
		<ul class="main_menu">

	
	
	
	
			<li class="rogin my">
				
				<div class="rogin_btn">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path  d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"/></svg>ログイン中
					<span>[0039904244]</span>
				</div>
				
				<a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction">
					<span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"/></svg>ログアウト</span>
				</a>
			</li>
	
		</ul>
		


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

		<div class="close"><span>&#10005;</span>閉じる</div>
	</div>
	<div id="bg">




	<nav id="pan_nav"><div>
		<ul>
			<li><a href="/yugiohdb/">ホーム</a></li><!--
		 --><li>&raquo;</li><!--
		 --><li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li><!--
		 --><li>&raquo;</li><!--
		 --><li>モンスター2種
			
		</li>
		</ul>
		<div class="btn hex orn"><span>?</span></div>
	</div></nav><!--#pan_nav-->
	

	<nav id="title_msg">
		<span>自分のデッキを登録、編集ができます。自分の持っているカードやデッキの管理にご利用ください。<br>公開設定にすると誰からでもデッキ検索できるようになります。大会優勝デッキ/入賞デッキなどのタグやカテゴリーを設定する事で検索されやすくなります。<br>デッキ検索画面で「マイデッキを検索」にチェックを入れて検索すると、どのカードがどのデッキに入っているか調べる事ができます。</span>
	</nav>





<header id="broad_title">
	<div>
		<h1>

			【&ensp;公開中&ensp;】&ensp;

			モンスター2種<br>


			<span class="h1_cardID">[ CARD GAME ID : 0039904244 ]</span>



		</h1>

	</div>
</header>


<div id="main980">
	<article>



		<div id="article_body">
			<input type="hidden" id="wname" name="wname" value="MemberDeck">
			<input type="hidden" id="ytkn" name="ytkn" value="bad43dd5e8b1dee07cadca43034681dfb5c64a1485a2c5280d5b67f009ff0dc0">

			<div id="deck_header" class="box_default">

	


				<textarea class="p_url" type="text" wrap="soft" style="resize: none;" onclick="this.setSelectionRange(0,9999);" readonly>http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja</textarea>



			<div class="box_default_table">



				<dl >


					<dt>
						<span>お気に入り</span>
					</dt>
					<dd class="mark_btn_set star">
						<span class="num" id="favoriteCnt">0</span>
	
						<label class="mark_btn star">
							<input type="checkbox" name="deckFavorite" id="deckFavorite" class="checkbox01-input" onClick="updateDeckFavorite()" >
							<div class="btn hex check orn"><span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.97 98.94"><defs></defs><g ><polygon points="103.97 37.79 70.18 29.63 51.98 0 33.79 29.63 0 37.79 22.55 64.26 19.86 98.94 51.98 85.66 84.11 98.94 81.42 64.26 103.97 37.79"/></g></svg> お気に入り</div>
						</label>
	
					</dd>
				</dl>

	

				<dl class="border-left">
					<dt>
						<span>いいね</span>
					</dt>
					<dd class="mark_btn_set likes">
						<span class="num" id="likesCnt">0</span>
						<span class="likes_my">本人のいいね回数[&nbsp;<span class="num" id="usrLikesCnt">0]</span></span>


	
					</dd>
				</dl>

	

	
				<dl>
					<dt>
						<span>デッキタイプ</span>
					</dt>
					<dd class="text_set">
						<span>マスターデュエル</span>
					</dd>
				</dl>
				<dl class="border-left">
	
	
					<dt>
						<span>デッキスタイル</span>
					</dt>
					<dd class="text_set">
						<span>----</span>
					</dd>
				</dl>




	
	
	

	
	
	

	
				<dl class="tab_mh100">
					<dt>
						<span>コメント</span>
					</dt>
					<dd class="text_set">
						<span class="biko"></span>
					</dd>
				</dl>
	

	
		
				<dl class="tab_mh100">
					<dt>
						<span>デッキコード</span>
					</dt>
					<dd class="a_set">
						
						
							<a class="btn hex orn" href="/yugiohdb/member_deck.action?ope=13&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja" class="black_btn edit orange"><span><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.5.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="cord_00000125587425308771483180000003680755780686006149_"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="66px" height="42px"
	 viewBox="0 0 66 42" style="enable-background:new 0 0 66 42;" xml:space="preserve">
<g id="cord">
	<g>
		<path d="M14,0L0,21l14,21h6L6,21L20,0H14z M52,0h-6l14,21L46,42h6l14-21L52,0z M24,42h5L43,0h-5L24,42z"/>
	</g>
</g>
</svg>
 デッキコードを発行</span></a>
						
					</dd>
				</dl>
		
		
	



	

		
			
			
				<dl class="tab_mh100">
			
					<dt>
						<span>PDF</span>
					</dt>
					<dd class="a_set">
						
						<a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=1&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja" ><span>PDFで印刷</span></a>
						
						<a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=2&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja" ><span>PDFで印刷（名前）</span></a>

					</dd>
				</dl>
		
		
	



			</div>


	
			<div id="bottom_btn_set">
				
				<a class="btn hex " href="/yugiohdb/member_deck.action?ope=8&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja" class="black_btn"><span>デッキをコピー</span></a>

		
				
				<a class="btn hex orn" href="/yugiohdb/member_deck.action?ope=2&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja" class="black_btn edit orange"><span>編集開始</span></a>
		

			</div>

	

			</div>

	



<!--シェア追加-->
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v2.9";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
</script>
<!--シェア追加-->
	<div class="sns_btn">
		<div class="sns">
			
			<iframe src="//platform.twitter.com/widgets/tweet_button.html?url=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202309232316&amp;lang=ja&amp;count=horizontal&amp;hashtags=YugiohDB_JP " scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowTransparency="true"></iframe>

			
			<iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202309232316&amp;send=false&amp;layout=button_count&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;locale=ja_JP" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowTransparency="true"></iframe>

			
			<div class="fb-share-button" data-href="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja&a=202309232316" data-layout="button_count" data-size="small" ></div>

			
			<div class="line-it-button" style="display: none;" data-lang="ja" data-type="share-a" data-url="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja&a=202309232316"></div>
			<script src="https://d.line-scdn.net/r/web/social-plugin/js/thirdparty/loader.min.js" async="async" defer="defer"></script>
		</div>
	</div>



<form  name="form_sort" method="POST" action="/yugiohdb/member_deck.action?ope=1&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja">
	
	<div id="num_total">

		
		<a id="num_total_m" class="navbtn hex btn" href=""><span>
			<h4>メインデッキ合計</h4>
			<div class="hex icon icon_r"><span>40</span></div>
		</span></a>

		
		<a id="num_total_e" class="navbtn hex btn" href=""><span>
			<h4>エクストラデッキ合計</h4>
			<div class="hex icon icon_r"><span>15</span></div>
		</span></a>

		
		<a id="num_total_s" class="navbtn hex btn" href=""><span>
			<h4>サイドデッキ合計</h4>
			<div class="hex icon icon_r"><span>3</span></div>
		</span></a>


	</div>
	


	
	<div class="sort_set">
		<div class="pulldown">

			<span  >
				<select id="sort" name="sort" >
					<option value="1">登録順</option>
					<option value="2">名前順</option>
					<option value="3">レベル／ランク／リンク順</option>
				</select>
			</span>
		</div>
	</div>


	
	<div id="mode_set" class="tablink" >
		<ul>
			<li class="3"><span>テキスト詳細表示</span></li>
			<li class="1"><span>テキスト表示</span></li>
			<li class="2"><span>画像表示</span></li>
		</ul>
		<select id="deck_display" name="deck_display" >
			<option value="3">テキスト詳細表示</option>
			<option value="1">テキスト表示</option>
			<option value="2">画像表示</option>
		</select>
	</div>
</form>


	<div id="deck_text" >
		


			<div id="text_main" class="deck_set">
				<table id="monster_list" class="deck_list">
					<tr>
						<th colspan="3">モンスターカード</th>
						<th class="num">
							<span>6</span>
						</th>
					</tr>
	
	
		
					<tr class=' row' title="夢幻崩界イヴリース">

						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_effect.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>夢幻崩界イヴリース</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13571&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class='limited row' title="【制限カード】 斬機サーキュラー">

						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_effect.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>斬機サーキュラー</span>
		
								<div class="lr_icon fl fl_2">
				
				
									<p>制限カード</p>
									<span>制限カード</span>
				
				
								</div>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=17430&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
		
					<tr>
						<td class="row_num">
							3
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							4
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							5
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							6
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							7
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							8
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
	

				</table><!--#monster_list-->


	
				<table id="spell_list" class="deck_list">

					<tr>
						<th colspan="3">魔法カード</th>
						<th class="num">
							<span>20</span>
						</th>
					</tr>
	
		
					<tr class=' row' title="サイバネット・マイニング">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>サイバネット・マイニング</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14301&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="斬機方程式">
						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>斬機方程式</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14753&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="スモール・ワールド">
						<td class="row_num">
							3
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>スモール・ワールド</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="転生炎獣の聖域">
						<td class="row_num">
							4
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>転生炎獣の聖域</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13938&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class='semi_limited row' title="【準制限カード】 墓穴の指名者">
						<td class="row_num">
							5
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>墓穴の指名者</span>
		
								<div class="lr_icon fl fl_3">
				
				
				
									<p>準制限カード</p>
									<span>準制限カード</span>
				
								</div>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
					<tr class='limited row' title="【制限カード】 抹殺の指名者">
						<td class="row_num">
							6
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>抹殺の指名者</span>
		
								<div class="lr_icon fl fl_2">
				
				
									<p>制限カード</p>
									<span>制限カード</span>
				
				
								</div>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14627&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アームズ・ホール">
						<td class="row_num">
							7
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アームズ・ホール</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アームド・チェンジャー">
						<td class="row_num">
							8
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アームド・チェンジャー</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=6524&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		

				</table><!--#spell_list-->


		
				<table id="trap_list" class="deck_list">

					<tr>
						<th colspan="3">罠カード</th>
						<th class="num">
							<span>14</span>
						</th>
					</tr>
	
		
					<tr class=' row' title="強制脱出装置">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>強制脱出装置</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=5914&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="無限泡影">
						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>無限泡影</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="斬機超階乗">
						<td class="row_num">
							3
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>斬機超階乗</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14755&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="サイバネット・コンフリクト">
						<td class="row_num">
							4
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>サイバネット・コンフリクト</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13878&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="神の警告">
						<td class="row_num">
							5
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>神の警告</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9008&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
		

					<tr>
						<td class="row_num">
							6
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							7
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							8
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
	

				</table><!--#trap_list-->
			</div><!-- .deck_set -->
			<div class="deck_set">

	
				<table id="extra_list" class="deck_list">

					<tr>
						<th colspan="3">エクストラデッキ</th>
						<th class="num">
							<span>15</span>
						</th>
					</tr>

	
		
					<tr class=' row' title="塊斬機ラプラシアン">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_xyz.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>塊斬機ラプラシアン</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14752&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="塊斬機ダランベルシアン">
						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_xyz.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>塊斬機ダランベルシアン</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14800&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="リンク・スパイダー">
						<td class="row_num">
							3
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>リンク・スパイダー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13034&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="転生炎獣ベイルリンクス">
						<td class="row_num">
							4
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>転生炎獣ベイルリンクス</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14249&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="転生炎獣アルミラージ">
						<td class="row_num">
							5
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>転生炎獣アルミラージ</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14338&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="コード・トーカー">
						<td class="row_num">
							6
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>コード・トーカー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13460&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アップデートジャマー">
						<td class="row_num">
							7
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>アップデートジャマー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14122&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="スプラッシュ・メイジ">
						<td class="row_num">
							8
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>スプラッシュ・メイジ</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15034&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="トランスコード・トーカー">
						<td class="row_num">
							9
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>トランスコード・トーカー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13698&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="デコード・トーカー・ヒートソウル">
						<td class="row_num">
							10
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>デコード・トーカー・ヒートソウル</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14962&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="ファイアウォール・ドラゴン">
						<td class="row_num">
							11
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>ファイアウォール・ドラゴン</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13082&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アクセスコード・トーカー">
						<td class="row_num">
							12
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>アクセスコード・トーカー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15032&request_locale=ja">
						</td>
						<td class="num">
							<span>1</span>
						</td>
					</tr>
		
		
	
		
		
					<tr>
						<td class="row_num">
							13
						</td>
						<td colspan="3">&nbsp;</td>
					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							14
						</td>
						<td colspan="3">&nbsp;</td>
					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							15
						</td>
						<td colspan="3">&nbsp;</td>
					</tr>
		
	

	
				</table><!--#extra_list-->




				<table id="side_list" class="deck_list">
					<tr>
						<th colspan="3">サイドデッキ</th>
						<th class="num">
							<span>3</span>
						</th>
					</tr>

	
		
					<tr class=' row' title="塊斬機ダランベルシアン">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_xyz.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>塊斬機ダランベルシアン</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14800&request_locale=ja">
						</td>
						<td class="num">
							<span>
								1
							</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="リングリボー">
						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>リングリボー</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14904&request_locale=ja">
						</td>
						<td class="num">
							<span>
								1
							</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="コード・トーカー・インヴァート">
						<td class="row_num">
							3
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_link.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>コード・トーカー・インヴァート</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14542&request_locale=ja">
						</td>
						<td class="num">
							<span>
								1
							</span>
						</td>
					</tr>
		
		
	
		
		
					<tr>
						<td class="row_num">
							4
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							5
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							6
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							7
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							8
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							9
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							10
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							11
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							12
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							13
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							14
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							15
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	

	
				</table><!--#side_list-->
				<div class="deck_none"></div>

			</div><!-- .deck_set -->
	</div><!-- #deck_text -->




	<div id="deck_detailtext" >
		


	
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
	
	

	
	
			<div class="t_haed">
				<div class="status flex_1"><span>魔法カード</span></div>
				<div class="cards_num_set"><span>20</span></div>
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
									<span class="card_name">サイバネット・マイニング</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14301">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：手札を１枚墓地へ送って発動できる。デッキからレベル４以下のサイバース族モンスター１体を手札に加える。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14301">
						
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
									<span class="card_name">斬機方程式</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14753">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分の墓地の「斬機」モンスター１体を対象として発動できる。そのモンスターを特殊召喚する。この効果で特殊召喚したモンスターの攻撃力はターン終了時まで１０００アップする。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14753">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">3</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_2_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">スモール・ワールド</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="16555">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：手札のモンスター１体を相手に見せる。種族・属性・レベル・攻撃力・守備力の内１つのみが見せたモンスターと同じとなるモンスター１体をデッキから選んで確認し、手札から見せたモンスターを裏側表示で除外する。さらに、種族・属性・レベル・攻撃力・守備力の内１つのみが確認したモンスターと同じとなるモンスター１体をデッキから手札に加え、デッキから確認したモンスターを裏側表示で除外する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=16555">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">4</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_3_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">転生炎獣の聖域</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13938">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		
									<span class="box_card_effect">
										<img class="icon_img" src="external/image/parts/effect/effect_icon_field.png" alt="フィールド" title="フィールド">
										<span>フィールド</span>

										
									</span>
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。<br>①：このカードがフィールドゾーンに存在する限り、自分が「サラマングレイト」LモンスターをL召喚する場合、自分フィールドの同名の「サラマングレイト」Lモンスター１体のみを素材としてL召喚できる。<br>②：自分のモンスターが戦闘を行うダメージ計算時に、１０００LPを払い、自分フィールドのLモンスター１体を対象として発動できる。そのモンスターの攻撃力を０にし、そのモンスターの元々の攻撃力分だけ自分のLPを回復する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13938">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">5</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_4_1" alt="" title="" class="none">
		


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


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">6</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_5_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">抹殺の指名者</span>

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
										<input type="hidden" class="cid" value="14627">
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
									このカード名のカードは１ターンに１枚しか発動できない。①：カード名を１つ宣言して発動できる。宣言したカード１枚をデッキから除外する。ターン終了時まで、この効果で除外したカード及びそのカードと元々のカード名が同じカードの効果は無効化される。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value='2'>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14627">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">7</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_6_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アームズ・ホール</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="7493">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカードを発動するターン、自分は通常召喚できない。①：デッキの一番上のカードを墓地へ送って発動できる。自分のデッキ・墓地から装備魔法カード１枚を選んで手札に加える。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=7493">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">8</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_7_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アームド・チェンジャー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="6524">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		
									<span class="box_card_effect">
										<img class="icon_img" src="external/image/parts/effect/effect_icon_equip.png" alt="装備" title="装備">
										<span>装備</span>

										
									</span>
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									自分の手札から装備魔法カード１枚を墓地に送って発動する。装備モンスターが戦闘によってモンスターを破壊した場合、装備カードのコントローラーは自分の墓地から装備モンスターの攻撃力以下のモンスター１体を手札に加える事ができる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=6524">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->


		
			</div>
	
	
	



	
	
			<div class="t_haed">
				<div class="status flex_1"><span>罠カード</span></div>
				<div class="cards_num_set"><span>14</span></div>
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
									<span class="card_name">強制脱出装置</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="5914">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
										<span>罠</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：フィールドのモンスター１体を対象として発動できる。そのモンスターを持ち主の手札に戻す。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=5914">
						
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


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">3</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_2_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">斬機超階乗</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14755">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
										<span>罠</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分の墓地の「斬機」モンスターを３体まで対象とし、以下の効果から１つを選択して発動できる（同名カードは１枚まで）。<br>●そのモンスターを効果を無効にして特殊召喚し、そのモンスターのみを素材として「斬機」Sモンスター１体をS召喚する。その時のS素材モンスターは墓地へは行かず持ち主のデッキに戻る。<br>●そのモンスターを効果を無効にして特殊召喚し、そのモンスターのみを素材として「斬機」Xモンスター１体をX召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14755">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">4</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_3_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">サイバネット・コンフリクト</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13878">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
										<span>罠</span>
									</span>
		
		
									<span class="box_card_effect">
										<img class="icon_img" src="external/image/parts/effect/effect_icon_counter.png" alt="カウンター" title="カウンター">
										<span>カウンター</span>

										
									</span>
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分フィールドに「コード・トーカー」モンスターが存在し、モンスターの効果・魔法・罠カードが発動した時に発動できる。その発動を無効にし除外する。次のターンの終了時まで、相手はこの効果で除外したカードと元々のカード名が同じカードの効果を発動できない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13878">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">5</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_4_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">神の警告</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="9008">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
										<span>罠</span>
									</span>
		
		
									<span class="box_card_effect">
										<img class="icon_img" src="external/image/parts/effect/effect_icon_counter.png" alt="カウンター" title="カウンター">
										<span>カウンター</span>

										
									</span>
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：２０００LPを払って以下の効果を発動できる。<br>●モンスターを特殊召喚する効果を含む、モンスターの効果・魔法・罠カードが発動した時に発動できる。その発動を無効にし破壊する。<br>●自分または相手がモンスターを召喚・反転召喚・特殊召喚する際に発動できる。それを無効にし、そのモンスターを破壊する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9008">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->


		
			</div>
	
		</div><!-- .list -->

	</div>
	







	
	<div id="detailtext_ext" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>エクストラデッキ</h3>
				<span>15</span>
	
			</div>
		</div>

		<div id="main_m_list" class="list">
			<div class="t_body">
	
				



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
									<span class="card_name">塊斬機ラプラシアン</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14752">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
										<span>地属性</span>
									</span>
		
		

		
		
			
									<span class="box_card_level_rank rank">
										<img class="icon_img" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
										<span>ランク 4</span>
									</span>
			
			
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										エクシーズ／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2000</span>
									</span>


									<span class="def_power"><span>
			
			
										守備力 0
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル４モンスター×３<br>このカード名の①の効果は１ターンに１度しか使用できない。①：このカードがX召喚に成功した場合、このカードのX素材を３つまで取り除き、その数だけ以下の効果から選択して発動できる。<br>●相手の手札をランダムに１枚選んで墓地へ送る。<br>●相手フィールドのモンスター１体を選んで墓地へ送る。<br>●相手フィールドの魔法・罠カード１枚を選んで墓地へ送る。<br>②：自分フィールドの「斬機」カードが効果で破壊される場合、代わりにこのカードのX素材を１つ取り除く事ができる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14752">
						
						<div class="cards_num_set">
							<span>1</span>
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
									<span class="card_name">塊斬機ダランベルシアン</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14800">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
										<span>地属性</span>
									</span>
		
		

		
		
			
									<span class="box_card_level_rank rank">
										<img class="icon_img" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
										<span>ランク 4</span>
									</span>
			
			
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										エクシーズ／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2000</span>
									</span>


									<span class="def_power"><span>
			
			
										守備力 0
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル４モンスター×２体以上<br>このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。①：このカードがX召喚に成功した場合、このカードのX素材を以下の数だけ取り除き、その効果を発動できる。<br>●２つ：デッキから「斬機」カード１枚を手札に加える。<br>●３つ：デッキからレベル４モンスター１体を手札に加える。<br>●４つ：デッキから魔法・罠カード１枚を手札に加える。<br>②：自分フィールドのモンスター１体をリリースして発動できる。自分の手札・墓地からレベル４の「斬機」モンスター１体を選んで特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14800">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">3</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_2_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">リンク・スパイダー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13034">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
										<span>地属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link2.png" alt="リンク" title="リンク">
										<span>リンク 1</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 1000</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									通常モンスター１体<br>①：１ターンに１度、自分メインフェイズに発動できる。手札からレベル４以下の通常モンスター１体をこのカードのリンク先となる自分フィールドに特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13034">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">4</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_3_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">転生炎獣ベイルリンクス</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14249">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
										<span>炎属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link2.png" alt="リンク" title="リンク">
										<span>リンク 1</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 500</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル４以下のサイバース族モンスター１体<br>このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。<br>①：このカードがL召喚した場合に発動できる。デッキから「転生炎獣の聖域」１枚を手札に加える。<br>②：自分フィールドの「サラマングレイト」カードが戦闘・効果で破壊される場合、代わりに墓地のこのカードを除外できる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14249">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">5</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_4_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">転生炎獣アルミラージ</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14338">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
										<span>炎属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link3.png" alt="リンク" title="リンク">
										<span>リンク 1</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 0</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									通常召喚された攻撃力１０００以下のモンスター１体<br>このカード名の②の効果は１ターンに１度しか使用できない。①：このカードをリリースし、自分フィールドのモンスター１体を対象として発動できる。このターン、そのモンスターは相手の効果では破壊されない。この効果は相手ターンでも発動できる。②：このカードが墓地に存在し、通常召喚された自分のモンスターが戦闘で破壊された時に発動できる。このカードを特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14338">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">6</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_5_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">コード・トーカー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13460">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
										<span>闇属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link82.png" alt="リンク" title="リンク">
										<span>リンク 2</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 1300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									効果モンスター２体<br>①：このカードの攻撃力は、このカードのリンク先のモンスターの数×５００アップする。②：このカードのリンク先にモンスターが存在する限り、このカードは戦闘及び相手の効果では破壊されない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13460">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">7</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_6_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アップデートジャマー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14122">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_wind.png" alt="風属性" title="風属性">
										<span>風属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link84.png" alt="リンク" title="リンク">
										<span>リンク 2</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2000</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル２以上のサイバース族モンスター２体<br>①：自分のサイバース族モンスターが戦闘を行うダメージ計算時に１度、発動できる。ダメージステップ終了時まで、このカード以外のフィールドのカードの効果は無効化され、その戦闘のダメージ計算は元々の攻撃力・守備力で行う。その戦闘で相手モンスターが破壊され墓地へ送られた時、相手に１０００ダメージを与える。②：このカードがリンク素材として墓地へ送られた場合に発動できる。このカードをリンク素材としたリンクモンスターはこのターン、１度のバトルフェイズ中に２回攻撃できる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14122">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">8</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_7_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">スプラッシュ・メイジ</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="15034">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_water.png" alt="水属性" title="水属性">
										<span>水属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link93.png" alt="リンク" title="リンク">
										<span>リンク 2</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 1100</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									サイバース族モンスター２体<br>このカード名の効果は１ターンに１度しか使用できない。①：自分の墓地のサイバース族モンスター１体を対象として発動できる。そのモンスターを守備表示で特殊召喚する。この効果で特殊召喚したモンスターの効果は無効化される。この効果の発動後、ターン終了時まで自分はサイバース族モンスターしか特殊召喚できない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15034">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">9</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_8_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">トランスコード・トーカー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13698">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
										<span>地属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link862.png" alt="リンク" title="リンク">
										<span>リンク 3</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									効果モンスター２体以上<br>このカード名の②の効果は１ターンに１度しか使用できない。<br>①：このカードが相互リンク状態の場合、このカード及びこのカードの相互リンク先のモンスターの攻撃力は５００アップし、相手はそれらを効果の対象にできない。<br>②：「トランスコード・トーカー」を除く、自分の墓地のリンク３以下のサイバース族Lモンスター１体を対象として発動できる（この効果を発動するターン、自分はサイバース族モンスターしか特殊召喚できない）。そのモンスターをこのカードのリンク先となる自分フィールドに特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13698">
						
						<div class="cards_num_set">
							<span>2</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">10</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_9_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">デコード・トーカー・ヒートソウル</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14962">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
										<span>炎属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link813.png" alt="リンク" title="リンク">
										<span>リンク 3</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									属性が異なるサイバース族モンスター２体以上<br>このカード名の②の効果は１ターンに１度しか使用できない。①：このカードの攻撃力は、このカードのリンク先のモンスターの数×５００アップする。②：自分・相手ターンに１０００LPを払って発動できる。自分はデッキから１枚ドローする。自分のLPが２０００以下の場合、さらに以下の効果を適用できる。●フィールドのこのカードを除外し、EXデッキから「デコード・トーカー・ヒートソウル」以外のリンク３以下のサイバース族モンスター１体を特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14962">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">11</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_10_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">ファイアウォール・ドラゴン</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13082">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
										<span>光属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link8462.png" alt="リンク" title="リンク">
										<span>リンク 4</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2500</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									モンスター２体以上<br>このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。<br>①：このカードがフィールドに表側表示で存在する限り１度だけ、自分・相手ターンに、このカードの相互リンク先のモンスターの数まで、自分・相手の、フィールド・墓地のモンスターを対象として発動できる。そのモンスターを手札に戻す。<br>②：このカードのリンク先のモンスターが、戦闘で破壊された場合または墓地へ送られた場合に発動できる。手札からサイバース族モンスター１体を特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13082">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">12</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_11_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アクセスコード・トーカー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="15032">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
										<span>闇属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link8462.png" alt="リンク" title="リンク">
										<span>リンク 4</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									効果モンスター２体以上<br>このカードの効果の発動に対して相手は効果を発動できない。①：このカードがリンク召喚に成功した場合、そのリンク素材としたリンクモンスター１体を対象として発動できる。このカードの攻撃力は、そのモンスターのリンクマーカーの数×１０００アップする。②：自分のフィールド・墓地からリンクモンスター１体を除外して発動できる。相手フィールドのカード１枚を選んで破壊する。このターン、自分の「アクセスコード・トーカー」の効果を発動するために同じ属性のモンスターを除外する事はできない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15032">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
			</div>
		</div><!-- #card_list.list -->

	</div>
	






	
	<div id="detailtext_side" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>サイドデッキ</h3>
				<span>3</span>
	
			</div>
		</div>

		<div id="main_m_list" class="list">
			<div class="t_body">
	
				



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
									<span class="card_name">塊斬機ダランベルシアン</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14800">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
										<span>地属性</span>
									</span>
		
		

		
		
			
									<span class="box_card_level_rank rank">
										<img class="icon_img" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
										<span>ランク 4</span>
									</span>
			
			
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										エクシーズ／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 2000</span>
									</span>


									<span class="def_power"><span>
			
			
										守備力 0
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル４モンスター×２体以上<br>このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。①：このカードがX召喚に成功した場合、このカードのX素材を以下の数だけ取り除き、その効果を発動できる。<br>●２つ：デッキから「斬機」カード１枚を手札に加える。<br>●３つ：デッキからレベル４モンスター１体を手札に加える。<br>●４つ：デッキから魔法・罠カード１枚を手札に加える。<br>②：自分フィールドのモンスター１体をリリースして発動できる。自分の手札・墓地からレベル４の「斬機」モンスター１体を選んで特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14800">
						
						<div class="cards_num_set">
							<span>1</span>
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
									<span class="card_name">リングリボー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14904">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
										<span>闇属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link1.png" alt="リンク" title="リンク">
										<span>リンク 1</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									レベル４以下のサイバース族モンスター１体<br>このカード名の①②の効果はそれぞれ１ターンに１度しか使用できない。①：相手が罠カードを発動した時、このカードをリリースして発動できる。その効果を無効にし除外する。②：このカードが墓地に存在する場合、EXデッキから特殊召喚された自分フィールドの「＠イグニスター」モンスター１体をリリースして発動できる。このカードを特殊召喚する。この効果は相手ターンでも発動できる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14904">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">3</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_2_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">コード・トーカー・インヴァート</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14542">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
										<span>光属性</span>
									</span>
		
		

		
									<span class="box_card_linkmarker">
										<img class="icon_img" src="external/image/parts/link_pc/link46.png" alt="リンク" title="リンク">
										<span>リンク 2</span>
									
									</span>
		
		

		
									<span class="card_info_species_and_other_item"><span>
										【
										サイバース族
			
										／
										リンク／効果
			
			
			
										】
									</span></span>

									<span class="atk_power">
										<span>攻撃力 1300</span>
									</span>


									<span class="def_power"><span>
			
										守備力 - 
			
			
									</span></span>
		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									サイバース族モンスター２体<br>このカード名の効果は１ターンに１度しか使用できない。①：このカードがリンク召喚に成功した場合に発動できる。手札からサイバース族モンスター１体をこのカードのリンク先となる自分フィールドに特殊召喚する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14542">
						
						<div class="cards_num_set">
							<span>1</span>
						</div>
						</div><!-- .t_row c_normal -->


	
			</div>
		</div><!-- #card_list.list -->

	</div>
	
	</div>




			<div id="deck_image">

		



	<div id="main" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>メインデッキ</h3>
				<span>40</span>
			</div>
		</div>

		
		<div class="image_set">
	
	
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13571&request_locale=ja" title="夢幻崩界イヴリース" class="none">

				
					
					
						<span >
						<img class="card_image_monster_0_1" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13571&request_locale=ja" title="夢幻崩界イヴリース" class="none">

				
				
					
					
						<span >
						<img class="card_image_monster_0_1" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13571&request_locale=ja" title="夢幻崩界イヴリース" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_monster_0_1" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17430&request_locale=ja" title="【制限カード】 斬機サーキュラー" class="none">

				
					
					
						<span class=" limited">
						<img class="card_image_monster_1_1" alt="斬機サーキュラー" title="斬機サーキュラー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17430&request_locale=ja" title="【制限カード】 斬機サーキュラー" class="none">

				
				
					
					
						<span class=" limited">
						<img class="card_image_monster_1_1" alt="斬機サーキュラー" title="斬機サーキュラー" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		

			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17430&request_locale=ja" title="【制限カード】 斬機サーキュラー" class="none">

				
				
				
					
					
						<span class=" limited">
						<img class="card_image_monster_1_1" alt="斬機サーキュラー" title="斬機サーキュラー" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	

	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14301&request_locale=ja" title="サイバネット・マイニング" class="none">
				
					
					
						<span >
						<img class="card_image_spell_0_1" alt="サイバネット・マイニング" title="サイバネット・マイニング" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14301&request_locale=ja" title="サイバネット・マイニング" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_0_1" alt="サイバネット・マイニング" title="サイバネット・マイニング" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14301&request_locale=ja" title="サイバネット・マイニング" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_0_1" alt="サイバネット・マイニング" title="サイバネット・マイニング" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14753&request_locale=ja" title="斬機方程式" class="none">
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="斬機方程式" title="斬機方程式" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14753&request_locale=ja" title="斬機方程式" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="斬機方程式" title="斬機方程式" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14753&request_locale=ja" title="斬機方程式" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="斬機方程式" title="斬機方程式" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja" title="スモール・ワールド" class="none">
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="スモール・ワールド" title="スモール・ワールド" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja" title="スモール・ワールド" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="スモール・ワールド" title="スモール・ワールド" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16555&request_locale=ja" title="スモール・ワールド" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="スモール・ワールド" title="スモール・ワールド" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13938&request_locale=ja" title="転生炎獣の聖域" class="none">
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="転生炎獣の聖域" title="転生炎獣の聖域" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13938&request_locale=ja" title="転生炎獣の聖域" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="転生炎獣の聖域" title="転生炎獣の聖域" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13938&request_locale=ja" title="転生炎獣の聖域" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="転生炎獣の聖域" title="転生炎獣の聖域" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja" title="【準制限カード】 墓穴の指名者" class="none">
				
					
					
						<span class=" semi_limited">
						<img class="card_image_spell_4_1" alt="墓穴の指名者" title="墓穴の指名者" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja" title="【準制限カード】 墓穴の指名者" class="none">
				
				
					
					
						<span class=" semi_limited">
						<img class="card_image_spell_4_1" alt="墓穴の指名者" title="墓穴の指名者" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14627&request_locale=ja" title="【制限カード】 抹殺の指名者" class="none">
				
					
					
						<span class=" limited">
						<img class="card_image_spell_5_1" alt="抹殺の指名者" title="抹殺の指名者" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=6524&request_locale=ja" title="アームド・チェンジャー" class="none">
				
					
					
						<span >
						<img class="card_image_spell_7_1" alt="アームド・チェンジャー" title="アームド・チェンジャー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=6524&request_locale=ja" title="アームド・チェンジャー" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_7_1" alt="アームド・チェンジャー" title="アームド・チェンジャー" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	

	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5914&request_locale=ja" title="強制脱出装置" class="none">

				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="強制脱出装置" title="強制脱出装置" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5914&request_locale=ja" title="強制脱出装置" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="強制脱出装置" title="強制脱出装置" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5914&request_locale=ja" title="強制脱出装置" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="強制脱出装置" title="強制脱出装置" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
					
					
						<span >
						<img class="card_image_trap_1_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_1_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_trap_1_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14755&request_locale=ja" title="斬機超階乗" class="none">

				
					
					
						<span >
						<img class="card_image_trap_2_1" alt="斬機超階乗" title="斬機超階乗" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14755&request_locale=ja" title="斬機超階乗" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_2_1" alt="斬機超階乗" title="斬機超階乗" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14755&request_locale=ja" title="斬機超階乗" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_trap_2_1" alt="斬機超階乗" title="斬機超階乗" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13878&request_locale=ja" title="サイバネット・コンフリクト" class="none">

				
					
					
						<span >
						<img class="card_image_trap_3_1" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13878&request_locale=ja" title="サイバネット・コンフリクト" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_3_1" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13878&request_locale=ja" title="サイバネット・コンフリクト" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_trap_3_1" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9008&request_locale=ja" title="神の警告" class="none">

				
					
					
						<span >
						<img class="card_image_trap_4_1" alt="神の警告" title="神の警告" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9008&request_locale=ja" title="神の警告" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_4_1" alt="神の警告" title="神の警告" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	

		</div>

	</div><!--#main-->

<!-- -->

	<div id="extra" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>エクストラデッキ</h3>
				<span>15</span>
			</div>
		</div>

		<div class="image_set">
	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14752&request_locale=ja" title="塊斬機ラプラシアン" class="none">
				
					
					
						<span >

						<img class="card_image_extra_0_1" alt="塊斬機ラプラシアン" title="塊斬機ラプラシアン" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14800&request_locale=ja" title="塊斬機ダランベルシアン" class="none">
				
					
					
						<span >

						<img class="card_image_extra_1_1" alt="塊斬機ダランベルシアン" title="塊斬機ダランベルシアン" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13034&request_locale=ja" title="リンク・スパイダー" class="none">
				
					
					
						<span >

						<img class="card_image_extra_2_1" alt="リンク・スパイダー" title="リンク・スパイダー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14249&request_locale=ja" title="転生炎獣ベイルリンクス" class="none">
				
					
					
						<span >

						<img class="card_image_extra_3_1" alt="転生炎獣ベイルリンクス" title="転生炎獣ベイルリンクス" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14249&request_locale=ja" title="転生炎獣ベイルリンクス" class="none">
				
				
					
					
						<span >

						<img class="card_image_extra_3_1" alt="転生炎獣ベイルリンクス" title="転生炎獣ベイルリンクス" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14338&request_locale=ja" title="転生炎獣アルミラージ" class="none">
				
					
					
						<span >

						<img class="card_image_extra_4_1" alt="転生炎獣アルミラージ" title="転生炎獣アルミラージ" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13460&request_locale=ja" title="コード・トーカー" class="none">
				
					
					
						<span >

						<img class="card_image_extra_5_1" alt="コード・トーカー" title="コード・トーカー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14122&request_locale=ja" title="アップデートジャマー" class="none">
				
					
					
						<span >

						<img class="card_image_extra_6_1" alt="アップデートジャマー" title="アップデートジャマー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15034&request_locale=ja" title="スプラッシュ・メイジ" class="none">
				
					
					
						<span >

						<img class="card_image_extra_7_1" alt="スプラッシュ・メイジ" title="スプラッシュ・メイジ" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15034&request_locale=ja" title="スプラッシュ・メイジ" class="none">
				
				
					
					
						<span >

						<img class="card_image_extra_7_1" alt="スプラッシュ・メイジ" title="スプラッシュ・メイジ" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13698&request_locale=ja" title="トランスコード・トーカー" class="none">
				
					
					
						<span >

						<img class="card_image_extra_8_1" alt="トランスコード・トーカー" title="トランスコード・トーカー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13698&request_locale=ja" title="トランスコード・トーカー" class="none">
				
				
					
					
						<span >

						<img class="card_image_extra_8_1" alt="トランスコード・トーカー" title="トランスコード・トーカー" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14962&request_locale=ja" title="デコード・トーカー・ヒートソウル" class="none">
				
					
					
						<span >

						<img class="card_image_extra_9_1" alt="デコード・トーカー・ヒートソウル" title="デコード・トーカー・ヒートソウル" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13082&request_locale=ja" title="ファイアウォール・ドラゴン" class="none">
				
					
					
						<span >

						<img class="card_image_extra_10_1" alt="ファイアウォール・ドラゴン" title="ファイアウォール・ドラゴン" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15032&request_locale=ja" title="アクセスコード・トーカー" class="none">
				
					
					
						<span >

						<img class="card_image_extra_11_1" alt="アクセスコード・トーカー" title="アクセスコード・トーカー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		</div>

	</div><!--#extra-->




	<div id="side" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>サイドデッキ</h3>
				<span>3</span>
			</div>
		</div>

		<div class="image_set">
	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14800&request_locale=ja" title="塊斬機ダランベルシアン" class="none">
				
					
					
						<span >
						<img class="card_image_side_0_1" alt="塊斬機ダランベルシアン" title="塊斬機ダランベルシアン" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14904&request_locale=ja" title="リングリボー" class="none">
				
					
					
						<span >
						<img class="card_image_side_1_1" alt="リングリボー" title="リングリボー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14542&request_locale=ja" title="コード・トーカー・インヴァート" class="none">
				
					
					
						<span >
						<img class="card_image_side_2_1" alt="コード・トーカー・インヴァート" title="コード・トーカー・インヴァート" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
	
		</div>

	</div><!--#side-->


			</div>


	
			<div id="btnarea_cd">
				
				<a onClick="return DeckDelete()" class="btn hex red"><span>デッキを削除</span></a>
			</div>
	

		</div><!--#article_body-->

	</article>






	</div><!--#bg--></div><!--#main980-->

	

	
		<nav id="title_top_msg" class="nav_home"><div class="in_bg">
			<div class="title_btn">
				<span class="title">遊戯王 OCG デュエルモンスターズ カードデータベースとは</span>
				<div class="batu"><span>&and;</span></div>
			</div>
			<div class="in">
				<div class="in_btn">
					<p>遊戯王 オフィシャルカードゲーム デュエルモンスターズの公式サイトです。<br>全ての遊戯王OCGカードを検索したり、詳細なルールや禁止・制限カードを参照する事ができます。<br>また、自分が持っているカードやデッキをマイデッキに登録して管理したり、公開されているデッキレシピを検索して自分のデッキ構築の参考にする事ができます。</p>
					<a class="btn" href="https://www.yugioh-card.com/japan/howto/" target="_blank">
						<img src="external/image/ja/logo_ocgtcg.png" />
						<span>遊び方はこちら</span>
					</a>
				</div>


				<div id="nav_bottom">
					
					<a class="top_main_card_search" href="/yugiohdb/card_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg></span>
							<h3>カード検索</h3>
						</div>
						<div class="tex_bottom">
							遊戯王OCGの全てのカードを検索することができます。カードの詳細画面から、そのカードを使用したデッキ検索をすることができます。公開日よりカード検索ができるようになります。
						</div>
					</a>

					
					<a class="top_main_cardlist" href="/yugiohdb/card_list.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg></span>
							<h3>カードリスト</h3>
						</div>
						<div class="tex_bottom">
							遊戯王OCGカードを、収録べつ(商品/特典など)に閲覧することができます。<br>商品の公開日より最新情報として掲載しています。
						</div>
					</a>

					
					<a class="top_main_decks" href="/yugiohdb/deck_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg></span>
							<h3>デッキ検索</h3>
						</div>
						<div class="tex_bottom">
							公開されているデッキを検索することができます。<br>大会優勝デッキ/大会入賞デッキの検索や、特定カードを使用しているデッキの検索ができます。
						</div>
					</a>


					
		
					<a class="top_trends" href="/yugiohdb/trends_search.action?ope=1">
			
			
						<div class="tex_top">
							<span class="icon"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg></span>
							<h3>トレンド</h3>
						</div>
						<div class="tex_bottom">
							新たに制作されたデッキや、大会で使用されたデッキを元に算出されたランキングです<br>現在注目されているデッキの傾向をチェックすることができます。
						</div>
					</a>

					
						
						
						
						
					<a class="top_main_my menu_my_decks" class="main" href="/yugiohdb/member_deck.action?ope=4&cgid=c8525f77e0268f9b1ba9110a8a05bc35">
						
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg></span>
							<h3>マイデッキ</h3>

						</div>
						<div class="tex_bottom">
							デッキレシピの登録や登録したデッキを他のユーザに公開できます(ハーフデッキやデュエルリンクスのデッキも登録できます)。自分のデッキやカードの管理の使用にもおすすめの機能です。
						</div>
					</a>

					
						
						
						
						
					<a class="top_main_my my_cardlist" href="/yugiohdb/member_have_want_card.action">
						
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg></span>
							<h3>マイカードリスト</h3>
						</div>
						<div class="tex_bottom">
							自分の持っているカードや欲しいカードをリストとして管理することができます。ログイン後にカード詳細画面から追加できます。
						</div>
					</a>



				

					
					<a class="top_main_q_a" href="/yugiohdb/faq_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg></span>
							<h3>Ｑ＆Ａ</h3>

						</div>
						<div class="tex_bottom">
							遊戯王カードゲーム事務局によせられた質問と回答をカード名などで検索ができます。最新カードのルール等も随時更新しています。
						</div>
					</a>
				
					
					<a class="top_main_forbidden" href="/yugiohdb/forbidden_limited.action">
						<div class="tex_top">
							<span class="icon"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
</span>
							<h3>
								<span>リミットレギュレーション</span>
							</h3>

						</div>
						<div class="tex_bottom">
							公式大会で使用が禁止されている禁止カードや枚数制限がある制限カード・準制限カードをまとめたリストです。
							<span class="history"></span>
						</div>
					</a>

				</div>
			</div>



		</div></nav>
	
	<footer id="footer">
		<div id="content_copyright">&copy;スタジオ・ダイス／集英社・テレビ東京・KONAMI</div>

		<div id="cdb_link_set"><a class="link_ocg" href="//www.yugioh-card.com/japan/" target="_blank">遊戯王公式サイト</a> <a class="link_neuron" href="//www.konami.com/yugioh/neuron/ja/" target="_blank">遊戯王ニューロン</a> <a class="link_cgn" href="//cardgame-network.konami.net/" target="_blank">KONAMI CARD GAME NETWORK</a> <a class="link_kst" href="http://www.konamistyle.jp/" target="_blank">コナミスタイル</a> <a class="link_kfs" href="https://www.konami.com/games/card/friendly_shop/" target="_blank">コナミ フレンドリーショップ</a> <a class="link_rushdb" href="https://www.db.yugioh-card.com/rushdb/" target="_blank">遊戯王ラッシュデュエルカードデータベース</a> <a class="link_tiktok" href="https://www.tiktok.com/@yugioh_cardgame_official?is_from_webapp=1&sender_device=pc" target="_blank">「遊戯王カードゲーム」公式TikTok</a></div>
		<div id="footer_menu">
			


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

		</div>
		<div id="footer_meta">
			<nav>
				<ul>
					<li><a href="http://www.yugioh-card.com/japan/support/" target="_blank">お問い合わせ</a></li>
					<li><a href="https://www.konami.com/siteinfo/ja/" target="_blank">サイトポリシー</a></li>
					<li><a href="https://legal.konami.com/games/privacy-jp/ja/" target="_blank">個人情報等保護方針</a></li>
				
					<li>
						<!-- OneTrust Cookie 設定ボタンの始点 -->
						<button id="ot-sdk-btn" class="ot-sdk-show-settings">Cookie 設定</button>
						<!-- OneTrust Cookie 設定ボタンの終点 -->
					</li>
				</ul>
			</nav>
			<small>&copy;2023 Konami Digital Entertainment</small>

		</div>
	</footer>
	<nav id="footer_icon">
		<div>
				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.35 28.26"><defs></defs><path  d="M13.44,23.3,2.21,21.64,3.93,10l3.52.52a11.1,11.1,0,0,1,.63-3.12l-5-.74-3,20.27,14,2.06,1.08-7.32a12.7,12.7,0,0,1-1.33-.53Zm-1.76-14,5.14.76-1.11,7.48a6.7,6.7,0,0,0,1.69.5L19.12,6.39,14,5.63a7,7,0,0,0-2.37,3.69ZM26.17,20l-.66.4L24.66,19a10,10,0,1,0-2.23,1.3l.85,1.44-.67.4,4.25,7.2,3.57-2.11Zm-3.73-2.21A7.82,7.82,0,1,1,25.2,7.1a7.83,7.83,0,0,1-2.76,10.71Z" transform="translate(-0.08 -1.07)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 33.07 29.79"><defs></defs><path d="M128.74,4.57l-1.11,13.66-1-.08,1.63,5.31-3.2,1,3.66.3,1.94-23.71L121.15.28l1.17,3.79ZM120.44,0,104.77,4.79l7,22.75,15.67-4.8Zm-9.06,21-4-13.11L120,4l4,13.1ZM131.13,5l-.31,3.78,4.33,1.43-4.3,13-1.18-.39-.25,3.06-7.08-.58-2.89.88,10.93,3.61,7.46-22.58Z" transform="translate(-104.77)"/></svg><h3>カードリスト</h3></a>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 35.46 28.79"><defs></defs><path d="M452,16.6a11,11,0,0,1-1.39-7.34l-1.65.26V29l8.35-1.73V21.19A10.91,10.91,0,0,1,452,16.6ZM451.16,7l-4.78-.4-8.07,1-.18.61V19l10.09,1.74V9.52l.38-.73,2.12-.32A9.87,9.87,0,0,1,451.16,7ZM439,27.26,448.22,29V21.17L439,19.6Zm30.21-7.13-.69.4-.85-1.45a10.22,10.22,0,1,0-2.23,1.33l.86,1.46-.68.41L470,29.61l3.64-2.14Zm-3.77-2.27a8,8,0,1,1,2.78-11l0,.06A8,8,0,0,1,465.44,17.86Zm1-12-9.12-.75a7.16,7.16,0,0,0-2.07,9.51.83.83,0,0,1,.08.12V8.51l.51-1,10.67-1.63ZM456.25,15.92a7.14,7.14,0,0,0,10.09.27,7,7,0,0,0,.85-1V6.8L456.25,8.51Z" transform="translate(-438.13 -0.82)"/></svg><h3>デッキ検索</h3></a>
					</li>
				
					<li class="menu_trends">
				
						<a href="/yugiohdb/trends_search.action?ope=1">
				
				
							<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.32"><defs></defs><g ><g ><path  d="M11.92,36.35l10.8,1.97v-7.46l-10.8-1.8v7.29Zm11.88,1.95l8.64-.96V14.78l-8.64,.96v22.56Zm-1.82-25.73l-11.14,1.01v14.04l11.88,1.98V14.66l6.25-.69-6.99-1.4ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg>
							<h3>トレンド</h3>
						</a>
					</li>


				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.73 27.45"><defs></defs><path  d="M370.6,22.79A1.66,1.66,0,1,0,369,21.12v0A1.65,1.65,0,0,0,370.6,22.79Zm-10.11-5.65a1,1,0,0,0,.75-.63,1.82,1.82,0,0,0,.09-.8,2,2,0,0,1,0-.59,2.8,2.8,0,0,1,.2-.62,2.88,2.88,0,0,1,3.08-1.37,3.8,3.8,0,0,1,1.5.85,3.47,3.47,0,0,1,1,1.87,2,2,0,0,1,0,.69,3.28,3.28,0,0,1-.21.86A5.07,5.07,0,0,1,365,19.07c-.28.18-1,.52-1.11.81s.11.68.22.93l.95,2.1c.09.21.27.8.61.74a1.57,1.57,0,0,0,.54-.29c.18-.13.48-.25.57-.46a.6.6,0,0,0,0-.49,2.71,2.71,0,0,0-.21-.37c-.13-.21-.25-.42-.37-.63s-.3-.37-.15-.59a2.13,2.13,0,0,1,.65-.42l.42-.29a4.71,4.71,0,0,0,1.6-1.91,6.46,6.46,0,0,0,.36-1.21,4.79,4.79,0,0,0-.44-3,5.11,5.11,0,0,0-3.53-2.49,8.79,8.79,0,0,0-1.14-.11h-.58a10.28,10.28,0,0,0-1.08.21,4.51,4.51,0,0,0-2.93,2.87c-.28.72-.55,2,.12,2.46a1,1,0,0,0,.94.19Zm1.19-11.25H369l.09-.14a4.42,4.42,0,0,1,1.07-1,6.55,6.55,0,0,1,6.18-.87,6.31,6.31,0,0,1,2.37,1.57V1.76H360.21v10.4a4.46,4.46,0,0,1,1.47-1Zm17.9,2.2a6,6,0,0,0-6-4,5.86,5.86,0,0,0-3.45,1.41,3.37,3.37,0,0,0-.69.67,1.62,1.62,0,0,0-.3,1.57,1.21,1.21,0,0,0,.83.66c1.13.29,1.51-.82,2-1.39a2.14,2.14,0,0,1,.58-.46,2.75,2.75,0,0,1,.79-.33,3.64,3.64,0,0,1,4.29,3.19,3.87,3.87,0,0,1-.06,1.44,3.19,3.19,0,0,1-1.89,2.43,7.33,7.33,0,0,1-3.42.12,1.09,1.09,0,0,0-1.09.27,4.34,4.34,0,0,0-.27,1.13l-.51,2.53c-.11.47-.22.91.29,1h.62c1.29.21,1-.77,1.15-1.7.07-.4-.05-.73.28-.87a2,2,0,0,1,.9,0,5,5,0,0,0,1.44,0,7.09,7.09,0,0,0,1.21-.28A5.71,5.71,0,0,0,379,13.35,7.49,7.49,0,0,0,379.58,8.09ZM365.72,25.43A1.47,1.47,0,1,0,367.19,24a1.47,1.47,0,0,0-1.47,1.48Zm11.47-3.29h-4.6a2.22,2.22,0,0,1-4,0h-1.24a3.25,3.25,0,0,1,.11.42,1.26,1.26,0,0,1-.13.63,1.22,1.22,0,0,1-.2.25h0a2,2,0,1,1-2,2,2,2,0,0,1,.42-1.24.93.93,0,0,1-.29-.05c-.4-.13-.6-.64-.76-1l-.45-1h-2.44V16.91a1.65,1.65,0,0,1-1.47.87V29.21H378.6V14.76a5,5,0,0,1-1.47,1.06Z" transform="translate(-359.09 -1.76)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="25.3px" height="27.7px" viewBox="0 0 25.3 27.7" style="enable-background:new 0 0 25.3 27.7;"
	 xml:space="preserve">
<path d="M25.3,13.7L25.3,13.7C25.3,13.7,25.3,13.7,25.3,13.7c0-7-5.7-12.7-12.6-12.7C5.7,1,0,6.7,0,13.6s5.7,12.6,12.6,12.6
	C19.6,26.3,25.2,20.7,25.3,13.7z M3,13.7c0-2.1,0.7-4.1,2-5.8l13.1,13.7c-1.6,1.1-3.5,1.7-5.5,1.7C7.3,23.3,3,19,3,13.7L3,13.7z
	 M12.6,4c2.1,0,4.1,0.7,5.8,2c4.2,3.2,5.1,9.3,1.8,13.5L7.2,5.7C8.8,4.6,10.7,4,12.6,4L12.6,4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->
		</div>
	</nav>
</div><!--wrapper-->
<noscript>JavaScript を有効にしてください</noscript>

</body>
</html>""",
            "expected": [
                {'name': '夢幻崩界イヴリース', 'attribute': '闇属性', 'type': '【サイバース族', 'level': 'レベル2',
                 'attack': '攻撃力0', 'defence': '守備力0'},
                {'name': '斬機サーキュラー', 'attribute': '光属性', 'type': '【サイバース族', 'level': 'レベル4',
                 'attack': '攻撃力1500', 'defence': '守備力1500'}
            ]
        }
    ]

    @pytest.mark.parametrize("test_data", generate_monsters_normal_test_datas)
    def test_generate_monsters_normal(self, test_data):
        """
        generate_monsters()正常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        actual = parser.generate_monsters()

        # 検証
        assert actual == test_data["expected"], test_data["note"]

    # generate_monsters()異常系のテストデータ
    generate_monsters_exception_test_datas = [
        {
            "note": "異常系_魔法罠のみ",
            "html": """<html>
<head>




	<meta http-equiv="x-ua-compatible" content="IE=10" >
	<meta http-equiv="x-ua-compatible" content="IE=EmulateIE10" >

	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<meta http-equiv="Content-Language" content="ja">
	<meta http-equiv="Content-Style-Type" content="text/css">
	<meta http-equiv="Content-Script-Type" content="text/javascript">
	<meta http-equiv="imagetoolbar" content="no">
	<meta name="format-detection" content="telephone=no">

	<meta property="og:site_name" content="遊戯王OCGカードデータベース">

	<meta property="og:type" content="product" />
	<meta property="og:locale" content="ja_JP" />

	<meta name="twitter:card" content="summary"/>

	<script type="text/javascript" src="/yugiohdb/ga.js"></script>
	<meta name="copyright" content="KONAMI">
	<link rel="shortcut icon" href="external/image/yugioh.ico">
	<link rel="apple-touch-icon" href="external/image/apple-touch-icon.png">


	


	


	


	<meta name="keywords" content="デッキ_魔法罠だけの場合,遊戯王,デッキ,デュエルモンスターズ,VRAINS,ヴレインズ,禁止,制限,パック,禁止カード,カード,カードリスト,ルール,OCG,コナミ,KONAMI">
	<meta name="description" content="デッキ_魔法罠だけの場合 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細">
	<meta property="title" content="デッキ_魔法罠だけの場合 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">

	<meta property="og:title" content="デッキ_魔法罠だけの場合 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">
	<meta property="og:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D60%26request_locale%3Dja%26a%3D202309232322"/>

	<meta property="og:description" content="デッキ_魔法罠だけの場合 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細" />

	<meta name="twitter:title" content="デッキ_魔法罠だけの場合 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース" />
	<meta name="twitter:description" content="デッキ_魔法罠だけの場合 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細" />

	<meta name="twitter:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D60%26request_locale%3Dja%26a%3D202309232322" />

	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">



	


	<title>遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</title>



<!--[if lt IE 9]>
	<script type="text/javascript" src="external/html5/js/html5shiv.js"></script>
<![endif]-->
	<script type="text/javascript" src="external/jquery/jquery-3.6.0.js"></script>

	<script type="text/javascript" src="external/jquery/jquery-ui-1.13.1.custom/jquery-ui.js"></script>

	<script type="text/javascript" src="external/js/common.js"></script>

	<script type="text/javascript" src="external/jquery/scrolltopcontrol.js"></script>


<script src="external/js/jquery.autosize.js" type="text/javascript"></script>



	<!--link type="text/css" rel="stylesheet" href="external/jquery/jquery-ui-1.8.16.custom/css/ui-lightness/jquery-ui-1.8.16.custom.css"-->
	<link type="text/css" rel="stylesheet" href="external/jquery/jquery-ui-1.13.1.custom/jquery-ui.css">

	<link type="text/css" rel="stylesheet" href="external/css/common.css?20171030">

	<link rel="stylesheet" type="text/css" href="external/css/MemberDeckDetail.css">



<meta property='og:image' content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&osplang=1&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&app=tournament&request_locale=ja&a=202309232322" />
<meta name='twitter:image' content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&osplang=1&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&app=tournament&request_locale=ja&a=202309232322" />


<script type="text/javascript">
<!--

	$(function(){
		

		$('#dno').val('60');
		$('#dno').change(function() {
			var value = $(this).val();
			
			location.href='/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=' + value + '&request_locale=ja';
		});
		$('#sort').val('1');
		$('#sort').change(function() {
			var value = $(this).val();
		        var str = $(this).val();
		        $(this).parents('form').submit();
		});
		$('.tablink li.'+'2').addClass("now");
		$('#deck_display').val('2');

		$('#deck_display').change(function() {
			var value = $(this).val();
			
			$('#deck_image,#deck_detailtext,#deck_text').hide();

			$('.tablink li').removeClass("now");
			$('.tablink li.'+value).addClass("now");
			switch (value) {
			case '1':
				$('#deck_text').show();
				$("#num_total_m").attr("href", "#monster_list");
				$("#num_total_e").attr("href", "#extra_list");
				$("#num_total_s").attr("href", "#side_list");
				break;
			case '2':
				$('#deck_image').show();
				$("#num_total_m").attr("href", "#main");
				$("#num_total_e").attr("href", "#extra");
				$("#num_total_s").attr("href", "#side");
				break;
			case '3':
				$('#deck_detailtext').show();
				$("#num_total_m").attr("href", "#detailtext_main");
				$("#num_total_e").attr("href", "#detailtext_ext");
				$("#num_total_s").attr("href", "#detailtext_side");

				break;
			}

		});
		$('.tablink li').click(function(){
			$('.tablink li').removeClass("now");
			clm = $(this).attr("class");

			$('#deck_display').val(clm);
			$('#deck_display').trigger('change');
		});


		
		
		
			
				$('#detailtext_main .mlist_s #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ').show();

				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
				$('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_1_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=5983&ciid=1&enc=FCGYKAMF6_MLjYHGzfJ2nw').show();

				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5983&ciid=1&enc=FCGYKAMF6_MLjYHGzfJ2nw&osplang=1').show();
				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5983&ciid=1&enc=FCGYKAMF6_MLjYHGzfJ2nw&osplang=1').show();
				$('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5983&ciid=1&enc=FCGYKAMF6_MLjYHGzfJ2nw&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_2_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=9927&ciid=1&enc=qXnulx7zt_pG0jzpd11_bA').show();

				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9927&ciid=1&enc=qXnulx7zt_pG0jzpd11_bA&osplang=1').show();
				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9927&ciid=1&enc=qXnulx7zt_pG0jzpd11_bA&osplang=1').show();
				$('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9927&ciid=1&enc=qXnulx7zt_pG0jzpd11_bA&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_3_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg').show();

				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
				$('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_4_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=15743&ciid=1&enc=bpL87NOfT1ZP0zXEM81zyA').show();

				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15743&ciid=1&enc=bpL87NOfT1ZP0zXEM81zyA&osplang=1').show();
				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15743&ciid=1&enc=bpL87NOfT1ZP0zXEM81zyA&osplang=1').show();
				$('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15743&ciid=1&enc=bpL87NOfT1ZP0zXEM81zyA&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_5_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=6673&ciid=1&enc=o6_eVgSf346o5xlVY3NHCA').show();

				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6673&ciid=1&enc=o6_eVgSf346o5xlVY3NHCA&osplang=1').show();
				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6673&ciid=1&enc=o6_eVgSf346o5xlVY3NHCA&osplang=1').show();
				$('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6673&ciid=1&enc=o6_eVgSf346o5xlVY3NHCA&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_6_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=10008&ciid=1&enc=PdthRktXcr_H9DVsmA4Nbg').show();

				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=10008&ciid=1&enc=PdthRktXcr_H9DVsmA4Nbg&osplang=1').show();
				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=10008&ciid=1&enc=PdthRktXcr_H9DVsmA4Nbg&osplang=1').show();
				$('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=10008&ciid=1&enc=PdthRktXcr_H9DVsmA4Nbg&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_7_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13827&ciid=1&enc=ueOq0_FHqskeTX7fYuEn4A').show();

				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13827&ciid=1&enc=ueOq0_FHqskeTX7fYuEn4A&osplang=1').show();
				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13827&ciid=1&enc=ueOq0_FHqskeTX7fYuEn4A&osplang=1').show();
				$('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13827&ciid=1&enc=ueOq0_FHqskeTX7fYuEn4A&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_8_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=15042&ciid=1&enc=vgBb6Y7Jxg8eJkUacRe7SA').show();

				$('.card_image_spell_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15042&ciid=1&enc=vgBb6Y7Jxg8eJkUacRe7SA&osplang=1').show();
				$('.card_image_spell_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15042&ciid=1&enc=vgBb6Y7Jxg8eJkUacRe7SA&osplang=1').show();
				$('.card_image_spell_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15042&ciid=1&enc=vgBb6Y7Jxg8eJkUacRe7SA&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_9_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=16418&ciid=1&enc=WcNoKqz2xM6DA21ih0Lu4A').show();

				$('.card_image_spell_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16418&ciid=1&enc=WcNoKqz2xM6DA21ih0Lu4A&osplang=1').show();
				$('.card_image_spell_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16418&ciid=1&enc=WcNoKqz2xM6DA21ih0Lu4A&osplang=1').show();
				$('.card_image_spell_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16418&ciid=1&enc=WcNoKqz2xM6DA21ih0Lu4A&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_10_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=14862&ciid=1&enc=ypCAZCSZQ3YlJ21WZbjQTQ').show();

				$('.card_image_spell_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14862&ciid=1&enc=ypCAZCSZQ3YlJ21WZbjQTQ&osplang=1').show();
				$('.card_image_spell_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14862&ciid=1&enc=ypCAZCSZQ3YlJ21WZbjQTQ&osplang=1').show();
				$('.card_image_spell_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14862&ciid=1&enc=ypCAZCSZQ3YlJ21WZbjQTQ&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_11_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=17264&ciid=1&enc=gj1rwVJQHhlmiiFv7Ln_Ig').show();

				$('.card_image_spell_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17264&ciid=1&enc=gj1rwVJQHhlmiiFv7Ln_Ig&osplang=1').show();
				$('.card_image_spell_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17264&ciid=1&enc=gj1rwVJQHhlmiiFv7Ln_Ig&osplang=1').show();
				$('.card_image_spell_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17264&ciid=1&enc=gj1rwVJQHhlmiiFv7Ln_Ig&osplang=1').show();
			
		
			
				$('#detailtext_main .mlist_s #card_image_12_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=9665&ciid=1&enc=VGfsmqiLXu1BvVJy00cr_w').show();

				$('.card_image_spell_12_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9665&ciid=1&enc=VGfsmqiLXu1BvVJy00cr_w&osplang=1').show();
				$('.card_image_spell_12_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9665&ciid=1&enc=VGfsmqiLXu1BvVJy00cr_w&osplang=1').show();
				$('.card_image_spell_12_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9665&ciid=1&enc=VGfsmqiLXu1BvVJy00cr_w&osplang=1').show();
			
		
		
			
				$('#detailtext_main .mlist_t #card_image_0_1').attr('src', '/yugiohdb/get_image.action?type=1&osplang=1&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg').show();

				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
				$('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
			
		
		
		

		
		$('.deck_list tr.row,.list .t_row').click(function() {
			window.open($('.link_value', this).val());
		});

		$('textarea').autosize();


	});

	
	$(document).ready(function(){
		
		var value = '2';

		$('#deck_image,#deck_detailtext,#deck_text').hide();

		switch (value) {
		case '1':
			$('#deck_text').show();
			$("#num_total_m").attr("href", "#monster_list");
			$("#num_total_e").attr("href", "#extra_list");
			$("#num_total_s").attr("href", "#side_list");
			break;
		case '2':
			$('#deck_image').show();
				$("#num_total_m").attr("href", "#main");
				$("#num_total_e").attr("href", "#extra");
				$("#num_total_s").attr("href", "#side");
			break;
		case '3':
			$('#deck_detailtext').show();
				$("#num_total_m").attr("href", "#detailtext_main");
				$("#num_total_e").attr("href", "#detailtext_ext");
				$("#num_total_s").attr("href", "#detailtext_side");
			break;
		default:
			break;
		}
		
	});

	function DeckDelete(){
		if(window.confirm('このデッキを削除しますか？')){
			location.href = "/yugiohdb/member_deck.action?ope=7&wname=MemberDeck&ytkn=530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja";
		}
	}

	function updateDeckFavorite(){
		var chngeFavoriteCnt = document.getElementById("favoriteCnt");
		var mycount = 1;
		if (deckFavorite.checked) {
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=9&wname=MemberDeck&ytkn=530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			if (false) {
				mycount = 0; //自分が登録済み
			}
			chngeFavoriteCnt.innerHTML = 0 + mycount;
		} else{
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=10&wname=MemberDeck&ytkn=530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			if (true) {
				mycount = 0; //自分が登録済み
			}
			chngeFavoriteCnt.innerHTML = 0 - mycount;

		}
	}
	function updateDeckLikes(){
		var chngelikesCnt = document.getElementById("likesCnt");
		var likesCnt = document.getElementById("deckLikesCnt"); 
		var usrLiksCnt = document.getElementById("usrLikesCnt");
		var chkMaxCnt = document.getElementById("deckLikesUsrCnt");
		if ( Number( chkMaxCnt.value) < 5 ) {
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=11&wname=MemberDeck&ytkn=530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
			likesCnt.value = Number(likesCnt.value) + 1;
			chkMaxCnt.value = Number(chkMaxCnt.value) + 1;
			chngelikesCnt.innerHTML = likesCnt.value;
			usrLiksCnt.innerHTML = chkMaxCnt.value;
		} else {
			crearDeckLikes();

			likesCnt.value = Number(likesCnt.value) - 5;
			chngelikesCnt.innerHTML = likesCnt.value;
			chkMaxCnt.value = 0;         
			usrLiksCnt.innerHTML = 0; 
		}
	}
	function crearDeckLikes(){
			$.ajax({
				type: 'get',
				url: '/yugiohdb/member_deck.action?ope=12&wname=MemberDeck&ytkn=530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja',
				success: function() {
				},
				error: function(xhr, status, error) {
				}
			});
	}

//-->
</script>




	

<body class="ja">

<div id="wrapper">
	<header>
		<div id="header_meta">
			<a href="https://www.konami.com/games/jp/ja/" target="_blank"><img src="https://www.yugioh-card.com/ci/logo/konami_logo_normal.png" alt="KONAMI" id="konami" class="ui-draggable"></a>

			
			<nav id="language">
				
				<span  class="hex2_1 orn"><span class="hex2_2">
					日本語
					
					
					
					
					
			 		
			 		
			 		
				</span></span>
				
				<div id="lang_mane">
					<div>
						<p>OCG</p>
						<ul>
							<li><a href="javascript:ChangeLanguage('ja')" class="current">日本語</a></li>
							<li><a href="javascript:ChangeLanguage('ko')" >한글</a></li>
	
							
						</ul>
					</div>
					<div>
						<p>TCG</p>
						<ul>
							<li><a href="javascript:ChangeLanguage('en')" >English</a></li>
							<li><a href="javascript:ChangeLanguage('de')" >Deutsch</a></li>
							<li><a href="javascript:ChangeLanguage('fr')" >Fran&ccedil;ais</a></li>
							<li><a href="javascript:ChangeLanguage('it')" >Italiano</a></li>
							<li><a href="javascript:ChangeLanguage('es')" >Espa&ntilde;ol</a></li>
							<li><a href="javascript:ChangeLanguage('pt')" >Portugues</a></li>
						</ul>
					</div>

				</div>
			</nav>

		</div><!--#header_meta-->


		<div id="header_menu">
			<nav>
				<dl id="menber_menu">
	
	
	
	
					<dd class="rogin">
						<div class="rogin_btn">
							
							<div class="hex2_1 my"><div class="hex2_2"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path  d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"/></svg>ログイン中 <span>[0039904244]</span></div></div>
							
							<a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"/></svg>ログアウト</span></a>
						</div>
					</dd>
	
					<dd class="logo"></dd>
					
					<dd class="forbidden_limited">
						<a class="btn hex pnk"  href="/yugiohdb/forbidden_limited.action">
							<span>
								<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>

								<h3>リミットレギュレーション</h3>
								
							</span>
						</a>
					</dd>
				</dl><!-- #menber_menu -->
				
				<div class="bottom">
					<div id="spnav_btn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41.59 31"><defs></defs><path  d="M2.63,0H39a2.64,2.64,0,0,1,2.64,2.63h0A2.63,2.63,0,0,1,39,5.26H2.63A2.63,2.63,0,0,1,0,2.63H0A2.63,2.63,0,0,1,2.63,0Z"/><path  d="M2.63,12.87H39a2.64,2.64,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,18.13H2.63A2.63,2.63,0,0,1,0,15.5H0A2.63,2.63,0,0,1,2.63,12.87Z"/><path d="M2.63,25.74H39a2.63,2.63,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,31H2.63A2.63,2.63,0,0,1,0,28.37H0A2.63,2.63,0,0,1,2.63,25.74Z"/></svg></div>
					


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

				</div>

			</nav>
		</div><!-- #header_menu-->
	</header>
	<div id="spnav">
		<ul class="main_menu">

	
	
	
	
			<li class="rogin my">
				
				<div class="rogin_btn">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path  d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"/></svg>ログイン中
					<span>[0039904244]</span>
				</div>
				
				<a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction">
					<span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"/></svg>ログアウト</span>
				</a>
			</li>
	
		</ul>
		


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

		<div class="close"><span>&#10005;</span>閉じる</div>
	</div>
	<div id="bg">




	<nav id="pan_nav"><div>
		<ul>
			<li><a href="/yugiohdb/">ホーム</a></li><!--
		 --><li>&raquo;</li><!--
		 --><li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li><!--
		 --><li>&raquo;</li><!--
		 --><li>デッキ_魔法罠だけの場合
			
		</li>
		</ul>
		<div class="btn hex orn"><span>?</span></div>
	</div></nav><!--#pan_nav-->
	

	<nav id="title_msg">
		<span>自分のデッキを登録、編集ができます。自分の持っているカードやデッキの管理にご利用ください。<br>公開設定にすると誰からでもデッキ検索できるようになります。大会優勝デッキ/入賞デッキなどのタグやカテゴリーを設定する事で検索されやすくなります。<br>デッキ検索画面で「マイデッキを検索」にチェックを入れて検索すると、どのカードがどのデッキに入っているか調べる事ができます。</span>
	</nav>





<header id="broad_title">
	<div>
		<h1>

			【&ensp;公開中&ensp;】&ensp;

			デッキ_魔法罠だけの場合<br>


			<span class="h1_cardID">[ CARD GAME ID : 0039904244 ]</span>



		</h1>

	</div>
</header>


<div id="main980">
	<article>



		<div id="article_body">
			<input type="hidden" id="wname" name="wname" value="MemberDeck">
			<input type="hidden" id="ytkn" name="ytkn" value="530ebe52dc2e5f16b9552773908b3b9ea868b8266730c7fc29b2ad854c9ef60e">

			<div id="deck_header" class="box_default">

	


				<textarea class="p_url" type="text" wrap="soft" style="resize: none;" onclick="this.setSelectionRange(0,9999);" readonly>http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja</textarea>



			<div class="box_default_table">



				<dl >


					<dt>
						<span>お気に入り</span>
					</dt>
					<dd class="mark_btn_set star">
						<span class="num" id="favoriteCnt">0</span>
	
						<label class="mark_btn star">
							<input type="checkbox" name="deckFavorite" id="deckFavorite" class="checkbox01-input" onClick="updateDeckFavorite()" >
							<div class="btn hex check orn"><span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.97 98.94"><defs></defs><g ><polygon points="103.97 37.79 70.18 29.63 51.98 0 33.79 29.63 0 37.79 22.55 64.26 19.86 98.94 51.98 85.66 84.11 98.94 81.42 64.26 103.97 37.79"/></g></svg> お気に入り</div>
						</label>
	
					</dd>
				</dl>

	

				<dl class="border-left">
					<dt>
						<span>いいね</span>
					</dt>
					<dd class="mark_btn_set likes">
						<span class="num" id="likesCnt">0</span>
						<span class="likes_my">本人のいいね回数[&nbsp;<span class="num" id="usrLikesCnt">0]</span></span>


	
					</dd>
				</dl>

	

	
				<dl>
					<dt>
						<span>デッキタイプ</span>
					</dt>
					<dd class="text_set">
						<span>OCG（マスタールール）</span>
					</dd>
				</dl>
				<dl class="border-left">
	
	
					<dt>
						<span>デッキスタイル</span>
					</dt>
					<dd class="text_set">
						<span>----</span>
					</dd>
				</dl>




	
	
	

	
	
	

	
				<dl class="tab_mh100">
					<dt>
						<span>コメント</span>
					</dt>
					<dd class="text_set">
						<span class="biko"></span>
					</dd>
				</dl>
	

	
		
				<dl class="tab_mh100">
					<dt>
						<span>デッキコード</span>
					</dt>
					<dd class="a_set">
						
						
							<a class="btn hex orn" href="/yugiohdb/member_deck.action?ope=13&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja" class="black_btn edit orange"><span><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.5.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="cord_00000125587425308771483180000003680755780686006149_"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="66px" height="42px"
	 viewBox="0 0 66 42" style="enable-background:new 0 0 66 42;" xml:space="preserve">
<g id="cord">
	<g>
		<path d="M14,0L0,21l14,21h6L6,21L20,0H14z M52,0h-6l14,21L46,42h6l14-21L52,0z M24,42h5L43,0h-5L24,42z"/>
	</g>
</g>
</svg>
 デッキコードを発行</span></a>
						
					</dd>
				</dl>
		
		
	



	

		
			
			
				<dl class="tab_mh100">
			
					<dt>
						<span>PDF</span>
					</dt>
					<dd class="a_set">
						
						<a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=1&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja" ><span>PDFで印刷</span></a>
						
						<a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=2&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja" ><span>PDFで印刷（名前）</span></a>

					</dd>
				</dl>
		
		
	



			</div>


	
			<div id="bottom_btn_set">
				
				<a class="btn hex " href="/yugiohdb/member_deck.action?ope=8&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja" class="black_btn"><span>デッキをコピー</span></a>

		
				
				<a class="btn hex orn" href="/yugiohdb/member_deck.action?ope=2&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja" class="black_btn edit orange"><span>編集開始</span></a>
		

			</div>

	

			</div>

	



<!--シェア追加-->
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v2.9";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
</script>
<!--シェア追加-->
	<div class="sns_btn">
		<div class="sns">
			
			<iframe src="//platform.twitter.com/widgets/tweet_button.html?url=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D60%26request_locale%3Dja%26a%3D202309232322&amp;lang=ja&amp;count=horizontal&amp;hashtags=YugiohDB_JP " scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowTransparency="true"></iframe>

			
			<iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D60%26request_locale%3Dja%26a%3D202309232322&amp;send=false&amp;layout=button_count&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;locale=ja_JP" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowTransparency="true"></iframe>

			
			<div class="fb-share-button" data-href="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja&a=202309232322" data-layout="button_count" data-size="small" ></div>

			
			<div class="line-it-button" style="display: none;" data-lang="ja" data-type="share-a" data-url="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja&a=202309232322"></div>
			<script src="https://d.line-scdn.net/r/web/social-plugin/js/thirdparty/loader.min.js" async="async" defer="defer"></script>
		</div>
	</div>



<form  name="form_sort" method="POST" action="/yugiohdb/member_deck.action?ope=1&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=60&request_locale=ja">
	
	<div id="num_total">

		
		<a id="num_total_m" class="navbtn hex btn" href=""><span>
			<h4>メインデッキ合計</h4>
			<div class="hex icon icon_r"><span>40</span></div>
		</span></a>

		
		<a id="num_total_e" class="navbtn hex btn" href=""><span>
			<h4>エクストラデッキ合計</h4>
			<div class="hex icon icon_r"><span>0</span></div>
		</span></a>

		
		<a id="num_total_s" class="navbtn hex btn" href=""><span>
			<h4>サイドデッキ合計</h4>
			<div class="hex icon icon_r"><span>0</span></div>
		</span></a>


	</div>
	


	
	<div class="sort_set">
		<div class="pulldown">

			<span  >
				<select id="sort" name="sort" >
					<option value="1">登録順</option>
					<option value="2">名前順</option>
					<option value="3">レベル／ランク／リンク順</option>
				</select>
			</span>
		</div>
	</div>


	
	<div id="mode_set" class="tablink" >
		<ul>
			<li class="3"><span>テキスト詳細表示</span></li>
			<li class="1"><span>テキスト表示</span></li>
			<li class="2"><span>画像表示</span></li>
		</ul>
		<select id="deck_display" name="deck_display" >
			<option value="3">テキスト詳細表示</option>
			<option value="1">テキスト表示</option>
			<option value="2">画像表示</option>
		</select>
	</div>
</form>


	<div id="deck_text" >
		


			<div id="text_main" class="deck_set">
				<table id="monster_list" class="deck_list">
					<tr>
						<th colspan="3">モンスターカード</th>
						<th class="num">
							<span>0</span>
						</th>
					</tr>
	
	
		
		
					<tr>
						<td class="row_num">
							1
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							2
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							3
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							4
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							5
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							6
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							7
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							8
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							9
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							10
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							11
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							12
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
		
		
					<tr>
						<td class="row_num">
							13
						</td>
						<td colspan="3">&nbsp;</td>

					</tr>
		
	
	

				</table><!--#monster_list-->


	
				<table id="spell_list" class="deck_list">

					<tr>
						<th colspan="3">魔法カード</th>
						<th class="num">
							<span>37</span>
						</th>
					</tr>
	
		
					<tr class='semi_limited row' title="【準制限カード】 墓穴の指名者">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>墓穴の指名者</span>
		
								<div class="lr_icon fl fl_3">
				
				
				
									<p>準制限カード</p>
									<span>準制限カード</span>
				
								</div>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アースクエイク">
						<td class="row_num">
							2
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アースクエイク</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=5983&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アーマーブラスト">
						<td class="row_num">
							3
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アーマーブラスト</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9927&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アームズ・ホール">
						<td class="row_num">
							4
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アームズ・ホール</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="武装竜の襲雷">
						<td class="row_num">
							5
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>武装竜の襲雷</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15743&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="R－ライトジャスティス">
						<td class="row_num">
							6
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>R－ライトジャスティス</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=6673&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アイアンコール">
						<td class="row_num">
							7
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アイアンコール</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=10008&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アイアンドロー">
						<td class="row_num">
							8
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アイアンドロー</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13827&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="Ai－コンタクト">
						<td class="row_num">
							9
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>Ai－コンタクト</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15042&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アイス・ミラー">
						<td class="row_num">
							10
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アイス・ミラー</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=16418&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="Aiラブ融合">
						<td class="row_num">
							11
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>Aiラブ融合</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14862&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="青い涙の天使">
						<td class="row_num">
							12
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>青い涙の天使</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=17264&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
					<tr class=' row' title="アクア・ジェット">
						<td class="row_num">
							13
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_spell.png">
			
			
						</td>
						<td class="card_name">
							
							<div class="icon">
								<span>アクア・ジェット</span>
		
							</div>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9665&request_locale=ja">
						</td>
						<td class="num">
							<span>2</span>
						</td>
					</tr>
		
		
	
		

				</table><!--#spell_list-->


		
				<table id="trap_list" class="deck_list">

					<tr>
						<th colspan="3">罠カード</th>
						<th class="num">
							<span>3</span>
						</th>
					</tr>
	
		
					<tr class=' row' title="無限泡影">
						<td class="row_num">
							1
						</td>
						<td class="c_img">
			
							<img src="external/image/parts/card/card_icon_trap.png">
			
			
						</td>
						<td class="card_name">
							<div class="icon">
								<span>無限泡影</span>
		
							</div>
							
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja">
						</td>
						<td class="num">
							<span>3</span>
						</td>
					</tr>
		
		
	
		
		

					<tr>
						<td class="row_num">
							2
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							3
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							4
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							5
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							6
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							7
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							8
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							9
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							10
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							11
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							12
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
		
		

					<tr>
						<td class="row_num">
							13
						</td>
						<td  colspan="3">&nbsp;</td>
					</tr>
		
	
	

				</table><!--#trap_list-->
			</div><!-- .deck_set -->
			<div class="deck_set">

	
				<table id="extra_list" class="deck_list">

					<tr>
						<th colspan="3">エクストラデッキ</th>
						<th class="num">
							<span>0</span>
						</th>
					</tr>

	
				</table><!--#extra_list-->




				<table id="side_list" class="deck_list">
					<tr>
						<th colspan="3">サイドデッキ</th>
						<th class="num">
							<span>0</span>
						</th>
					</tr>

	
				</table><!--#side_list-->
				<div class="deck_none"></div>

			</div><!-- .deck_set -->
	</div><!-- #deck_text -->




	<div id="deck_detailtext" >
		


	
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
									<span class="card_name">アースクエイク</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="5983">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									フィールド上に表側表示で存在するモンスターを全て守備表示にする。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=5983">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">3</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_2_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アーマーブラスト</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="9927">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									自分フィールド上の「甲虫装機」と名のついたカード１枚と相手フィールド上に表側表示で存在するカード２枚を選択して発動する。選択したカードを破壊する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9927">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">4</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_3_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アームズ・ホール</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="7493">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカードを発動するターン、自分は通常召喚できない。①：デッキの一番上のカードを墓地へ送って発動できる。自分のデッキ・墓地から装備魔法カード１枚を選んで手札に加える。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=7493">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">5</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_4_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">武装竜の襲雷</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="15743">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できず、このカードを発動するターン、自分はドラゴン族モンスターしか特殊召喚できない。①：自分フィールドの「アームド・ドラゴン」モンスター１体を対象として発動できる。その同名モンスター１体を自分のデッキ・墓地から選び、手札に加えるか召喚条件を無視して特殊召喚する。この効果で特殊召喚したモンスターは直接攻撃できない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15743">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">6</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_5_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">R－ライトジャスティス</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="6673">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：自分フィールドの「E・HERO」カードの数だけ、フィールドの魔法・罠カードを選んで破壊する。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=6673">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">7</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_6_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アイアンコール</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="10008">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：自分フィールドに機械族モンスターが存在する場合、自分の墓地のレベル４以下の機械族モンスター１体を対象として発動できる。その機械族モンスターを特殊召喚する。この効果で特殊召喚したモンスターの効果は無効化され、エンドフェイズに破壊される。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=10008">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">8</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_7_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アイアンドロー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="13827">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分フィールドのモンスターが機械族の効果モンスター２体のみの場合に発動できる。自分はデッキから２枚ドローする。このカードの発動後、ターン終了時まで自分は１回しかモンスターを特殊召喚できない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=13827">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">9</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_8_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">Ai－コンタクト</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="15042">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分のフィールドゾーンに「イグニスターAiランド」が存在する場合、手札の「イグニスターAiランド」１枚を相手に見せて発動できる。見せたカードをデッキの一番下に戻し、自分はデッキから３枚ドローする。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=15042">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">10</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_9_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アイス・ミラー</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="16418">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：自分フィールドのレベル３以下の水属性モンスター１体を対象として発動できる。その同名モンスター１体をデッキから特殊召喚する。この効果で特殊召喚したモンスターが自分フィールドに表側表示で存在する限り、自分はEXデッキからモンスターを特殊召喚できない。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=16418">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">11</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_10_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">Aiラブ融合</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="14862">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名のカードは１ターンに１枚しか発動できない。①：自分の手札・フィールドから、サイバース族の融合モンスターカードによって決められた融合素材モンスターを墓地へ送り、その融合モンスター１体をEXデッキから融合召喚する。自分の「＠イグニスター」モンスターを融合素材とする場合、相手フィールドのリンクモンスターも１体まで融合素材とする事ができる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=14862">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">12</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_11_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">青い涙の天使</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="17264">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									このカード名の①②の効果は１ターンに１度、いずれか１つしか使用できない。①：フィールドの表側表示モンスター１体を対象として発動できる。そのモンスターのコントローラーから見て相手は、自身の手札の数×２００ダメージを受ける。その後、対象のモンスターの効果をターン終了時まで無効にする。②：自分または相手が効果ダメージを受けた場合、墓地のこのカードを除外して発動できる。手札・デッキから通常罠カード１枚を選んで自分フィールドにセットする。手札からセットした場合、そのカードはセットしたターンでも発動できる。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=17264">
						
						<div class="cards_num_set">
							<span>3</span>
						</div>
						</div><!-- .t_row c_normal -->


		
				



						<div class="t_row c_normal">
		
							<div class="card_count">
								<span class="row_num">13</span>
							</div>
		

							<div class="box_card_img">
		
		
								<img id="card_image_12_1" alt="" title="" class="none">
		


							</div>
						<div class="flex_1">
							<dl>
								<dd class="box_card_name flex_1 top_set">
									<span class="card_ruby"></span>
									<span class="card_name">アクア・ジェット</span>

								</dd>


								<dd class="icon top_set top_b_none">
		
		
								</dd>


								<dd class="remove_btn top_set">
									<a href="javascript:void(0);" class="btn hex red"  title="このカードをリストから削除">
										<span>X</span>
										<input type="hidden" class="lang" value="ja">
										<input type="hidden" class="cid" value="9665">
									</a>
								</dd>
								<dd class="box_card_spec flex_1">
		
									<span class="box_card_attribute">
										<img class="icon_img" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
										<span>魔法</span>
									</span>
		
		

		
		

		

								</dd>
		
		
								<dd class="box_card_text c_text flex_1">
									①：自分フィールドの魚族・海竜族・水族モンスター１体を対象として発動できる。そのモンスターの攻撃力は１０００アップする。
								</dd>
		
		





							</dl>
						</div>
								<input type="hidden" class="cnm" value=''>
								<input type="hidden" class="fltype" value=''>
							<input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&cid=9665">
						
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
	







	
	<div id="detailtext_ext" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>エクストラデッキ</h3>
				<span>0</span>
	
			</div>
		</div>

	</div>
	






	
	<div id="detailtext_side" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>サイドデッキ</h3>
				<span>0</span>
	
			</div>
		</div>

	</div>
	
	</div>




			<div id="deck_image">

		



	<div id="main" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>メインデッキ</h3>
				<span>40</span>
			</div>
		</div>

		
		<div class="image_set">
	
	

	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja" title="【準制限カード】 墓穴の指名者" class="none">
				
					
					
						<span class=" semi_limited">
						<img class="card_image_spell_0_1" alt="墓穴の指名者" title="墓穴の指名者" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13619&request_locale=ja" title="【準制限カード】 墓穴の指名者" class="none">
				
				
					
					
						<span class=" semi_limited">
						<img class="card_image_spell_0_1" alt="墓穴の指名者" title="墓穴の指名者" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5983&request_locale=ja" title="アースクエイク" class="none">
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="アースクエイク" title="アースクエイク" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5983&request_locale=ja" title="アースクエイク" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="アースクエイク" title="アースクエイク" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=5983&request_locale=ja" title="アースクエイク" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_1_1" alt="アースクエイク" title="アースクエイク" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9927&request_locale=ja" title="アーマーブラスト" class="none">
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="アーマーブラスト" title="アーマーブラスト" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9927&request_locale=ja" title="アーマーブラスト" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="アーマーブラスト" title="アーマーブラスト" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9927&request_locale=ja" title="アーマーブラスト" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_2_1" alt="アーマーブラスト" title="アーマーブラスト" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=7493&request_locale=ja" title="アームズ・ホール" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_3_1" alt="アームズ・ホール" title="アームズ・ホール" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15743&request_locale=ja" title="武装竜の襲雷" class="none">
				
					
					
						<span >
						<img class="card_image_spell_4_1" alt="武装竜の襲雷" title="武装竜の襲雷" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15743&request_locale=ja" title="武装竜の襲雷" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_4_1" alt="武装竜の襲雷" title="武装竜の襲雷" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15743&request_locale=ja" title="武装竜の襲雷" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_4_1" alt="武装竜の襲雷" title="武装竜の襲雷" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=6673&request_locale=ja" title="R－ライトジャスティス" class="none">
				
					
					
						<span >
						<img class="card_image_spell_5_1" alt="R－ライトジャスティス" title="R－ライトジャスティス" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=6673&request_locale=ja" title="R－ライトジャスティス" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_5_1" alt="R－ライトジャスティス" title="R－ライトジャスティス" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=6673&request_locale=ja" title="R－ライトジャスティス" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_5_1" alt="R－ライトジャスティス" title="R－ライトジャスティス" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=10008&request_locale=ja" title="アイアンコール" class="none">
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アイアンコール" title="アイアンコール" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=10008&request_locale=ja" title="アイアンコール" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アイアンコール" title="アイアンコール" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=10008&request_locale=ja" title="アイアンコール" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_6_1" alt="アイアンコール" title="アイアンコール" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13827&request_locale=ja" title="アイアンドロー" class="none">
				
					
					
						<span >
						<img class="card_image_spell_7_1" alt="アイアンドロー" title="アイアンドロー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13827&request_locale=ja" title="アイアンドロー" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_7_1" alt="アイアンドロー" title="アイアンドロー" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13827&request_locale=ja" title="アイアンドロー" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_7_1" alt="アイアンドロー" title="アイアンドロー" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15042&request_locale=ja" title="Ai－コンタクト" class="none">
				
					
					
						<span >
						<img class="card_image_spell_8_1" alt="Ai－コンタクト" title="Ai－コンタクト" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15042&request_locale=ja" title="Ai－コンタクト" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_8_1" alt="Ai－コンタクト" title="Ai－コンタクト" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=15042&request_locale=ja" title="Ai－コンタクト" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_8_1" alt="Ai－コンタクト" title="Ai－コンタクト" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16418&request_locale=ja" title="アイス・ミラー" class="none">
				
					
					
						<span >
						<img class="card_image_spell_9_1" alt="アイス・ミラー" title="アイス・ミラー" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16418&request_locale=ja" title="アイス・ミラー" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_9_1" alt="アイス・ミラー" title="アイス・ミラー" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=16418&request_locale=ja" title="アイス・ミラー" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_9_1" alt="アイス・ミラー" title="アイス・ミラー" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14862&request_locale=ja" title="Aiラブ融合" class="none">
				
					
					
						<span >
						<img class="card_image_spell_10_1" alt="Aiラブ融合" title="Aiラブ融合" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14862&request_locale=ja" title="Aiラブ融合" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_10_1" alt="Aiラブ融合" title="Aiラブ融合" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=14862&request_locale=ja" title="Aiラブ融合" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_10_1" alt="Aiラブ融合" title="Aiラブ融合" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17264&request_locale=ja" title="青い涙の天使" class="none">
				
					
					
						<span >
						<img class="card_image_spell_11_1" alt="青い涙の天使" title="青い涙の天使" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17264&request_locale=ja" title="青い涙の天使" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_11_1" alt="青い涙の天使" title="青い涙の天使" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=17264&request_locale=ja" title="青い涙の天使" class="none">
				
				
				
					
					
						<span >
						<img class="card_image_spell_11_1" alt="青い涙の天使" title="青い涙の天使" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9665&request_locale=ja" title="アクア・ジェット" class="none">
				
					
					
						<span >
						<img class="card_image_spell_12_1" alt="アクア・ジェット" title="アクア・ジェット" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=9665&request_locale=ja" title="アクア・ジェット" class="none">
				
				
					
					
						<span >
						<img class="card_image_spell_12_1" alt="アクア・ジェット" title="アクア・ジェット" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
	

	
	
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
				
			</a>
			
		
			
			
			<a target="_blank" href="/yugiohdb/card_search.action?ope=2&cid=13631&request_locale=ja" title="無限泡影" class="none">

				
				
				
					
					
						<span >
						<img class="card_image_trap_0_1" alt="無限泡影" title="無限泡影" class="none">
						<div><span></span></div></span>
					
				
			</a>
			
		
	

		</div>

	</div><!--#main-->

<!-- -->

	<div id="extra" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>エクストラデッキ</h3>
				<span>0</span>
			</div>
		</div>

	</div><!--#extra-->




	<div id="side" class="card_set">
		<div class="subcatergory">
			<div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path  d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"/></svg></span></div>
			<div class="top">
				<h3>サイドデッキ</h3>
				<span>0</span>
			</div>
		</div>

	</div><!--#side-->


			</div>


	
			<div id="btnarea_cd">
				
				<a onClick="return DeckDelete()" class="btn hex red"><span>デッキを削除</span></a>
			</div>
	

		</div><!--#article_body-->

	</article>






	</div><!--#bg--></div><!--#main980-->

	

	
		<nav id="title_top_msg" class="nav_home"><div class="in_bg">
			<div class="title_btn">
				<span class="title">遊戯王 OCG デュエルモンスターズ カードデータベースとは</span>
				<div class="batu"><span>&and;</span></div>
			</div>
			<div class="in">
				<div class="in_btn">
					<p>遊戯王 オフィシャルカードゲーム デュエルモンスターズの公式サイトです。<br>全ての遊戯王OCGカードを検索したり、詳細なルールや禁止・制限カードを参照する事ができます。<br>また、自分が持っているカードやデッキをマイデッキに登録して管理したり、公開されているデッキレシピを検索して自分のデッキ構築の参考にする事ができます。</p>
					<a class="btn" href="https://www.yugioh-card.com/japan/howto/" target="_blank">
						<img src="external/image/ja/logo_ocgtcg.png" />
						<span>遊び方はこちら</span>
					</a>
				</div>


				<div id="nav_bottom">
					
					<a class="top_main_card_search" href="/yugiohdb/card_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg></span>
							<h3>カード検索</h3>
						</div>
						<div class="tex_bottom">
							遊戯王OCGの全てのカードを検索することができます。カードの詳細画面から、そのカードを使用したデッキ検索をすることができます。公開日よりカード検索ができるようになります。
						</div>
					</a>

					
					<a class="top_main_cardlist" href="/yugiohdb/card_list.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg></span>
							<h3>カードリスト</h3>
						</div>
						<div class="tex_bottom">
							遊戯王OCGカードを、収録べつ(商品/特典など)に閲覧することができます。<br>商品の公開日より最新情報として掲載しています。
						</div>
					</a>

					
					<a class="top_main_decks" href="/yugiohdb/deck_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg></span>
							<h3>デッキ検索</h3>
						</div>
						<div class="tex_bottom">
							公開されているデッキを検索することができます。<br>大会優勝デッキ/大会入賞デッキの検索や、特定カードを使用しているデッキの検索ができます。
						</div>
					</a>


					
		
					<a class="top_trends" href="/yugiohdb/trends_search.action?ope=1">
			
			
						<div class="tex_top">
							<span class="icon"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg></span>
							<h3>トレンド</h3>
						</div>
						<div class="tex_bottom">
							新たに制作されたデッキや、大会で使用されたデッキを元に算出されたランキングです<br>現在注目されているデッキの傾向をチェックすることができます。
						</div>
					</a>

					
						
						
						
						
					<a class="top_main_my menu_my_decks" class="main" href="/yugiohdb/member_deck.action?ope=4&cgid=c8525f77e0268f9b1ba9110a8a05bc35">
						
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg></span>
							<h3>マイデッキ</h3>

						</div>
						<div class="tex_bottom">
							デッキレシピの登録や登録したデッキを他のユーザに公開できます(ハーフデッキやデュエルリンクスのデッキも登録できます)。自分のデッキやカードの管理の使用にもおすすめの機能です。
						</div>
					</a>

					
						
						
						
						
					<a class="top_main_my my_cardlist" href="/yugiohdb/member_have_want_card.action">
						
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg></span>
							<h3>マイカードリスト</h3>
						</div>
						<div class="tex_bottom">
							自分の持っているカードや欲しいカードをリストとして管理することができます。ログイン後にカード詳細画面から追加できます。
						</div>
					</a>



				

					
					<a class="top_main_q_a" href="/yugiohdb/faq_search.action">
						<div class="tex_top">
							<span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg></span>
							<h3>Ｑ＆Ａ</h3>

						</div>
						<div class="tex_bottom">
							遊戯王カードゲーム事務局によせられた質問と回答をカード名などで検索ができます。最新カードのルール等も随時更新しています。
						</div>
					</a>
				
					
					<a class="top_main_forbidden" href="/yugiohdb/forbidden_limited.action">
						<div class="tex_top">
							<span class="icon"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
</span>
							<h3>
								<span>リミットレギュレーション</span>
							</h3>

						</div>
						<div class="tex_bottom">
							公式大会で使用が禁止されている禁止カードや枚数制限がある制限カード・準制限カードをまとめたリストです。
							<span class="history"></span>
						</div>
					</a>

				</div>
			</div>



		</div></nav>
	
	<footer id="footer">
		<div id="content_copyright">&copy;スタジオ・ダイス／集英社・テレビ東京・KONAMI</div>

		<div id="cdb_link_set"><a class="link_ocg" href="//www.yugioh-card.com/japan/" target="_blank">遊戯王公式サイト</a> <a class="link_neuron" href="//www.konami.com/yugioh/neuron/ja/" target="_blank">遊戯王ニューロン</a> <a class="link_cgn" href="//cardgame-network.konami.net/" target="_blank">KONAMI CARD GAME NETWORK</a> <a class="link_kst" href="http://www.konamistyle.jp/" target="_blank">コナミスタイル</a> <a class="link_kfs" href="https://www.konami.com/games/card/friendly_shop/" target="_blank">コナミ フレンドリーショップ</a> <a class="link_rushdb" href="https://www.db.yugioh-card.com/rushdb/" target="_blank">遊戯王ラッシュデュエルカードデータベース</a> <a class="link_tiktok" href="https://www.tiktok.com/@yugioh_cardgame_official?is_from_webapp=1&sender_device=pc" target="_blank">「遊戯王カードゲーム」公式TikTok</a></div>
		<div id="footer_menu">
			


				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action?wname=CardSearch"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"/></svg><h3>カードリスト</h3></a>
						<ul>
							<li><a href="/yugiohdb/card_list.action?clm=3&wname=CardSearch">公開日の新しい順</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=1&wname=CardSearch">一般商品</a></li>
							<li><a href="/yugiohdb/card_list.action?clm=2&wname=CardSearch">特典・同梱系</a></li>
				
							<li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
				
						</ul>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action?wname=MemberDeck"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path  d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"/></svg><h3>デッキ検索</h3></a>
					</li>
				</ul>
					
					<div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

				<ul class="main_menu">

					
			

					<li class="menu_trends sab_menu">
						<a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g  ><g ><path  d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg><h3>トレンド</h3></a>
						<ul>
							
							<li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
							
							<li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
						</ul>
					</li>
			
			



	
	
	
	
				

					
					<li class="my menu_my_decks sab_menu">
						<a class="main" href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path  d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"/></svg><h3>マイデッキ</h3></a>
						<ul>
							<li><a href="/yugiohdb/member_deck.action?ope=4&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
							<li><a href="/yugiohdb/member_deck.action?ope=21&wname=MemberDeck&cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
						</ul>
					</li>

					
					<li class="my menu_my_cardlist sab_menu">
						<a class="main" href="/yugiohdb/member_have_want_card.action?wname=MyCard"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"/></svg><h3>マイカードリスト</h3></a>
						<ul >
							<li><a href="member_have_want_card.action?ope=1&wname=MyCard">持っているカードリスト</a></li>
							<li><a href="member_have_want_card.action?ope=2&wname=MyCard">欲しいカードリスト</a></li>
						</ul>
					</li>
	

				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path  d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="30px" height="35.3px" viewBox="0 0 30 35.3" style="enable-background:new 0 0 30 35.3;" xml:space="preserve">
<path d="M25.9,18.2L25.9,18.2z M14.8,32.8c0.1,0,0.1,0,0.2,0c8.3,0,15-6.7,15-15c0-8.2-6.6-14.9-14.8-15C6.9,2.7,0.1,9.4,0,17.7
	C-0.1,25.9,6.5,32.7,14.8,32.8L14.8,32.8z M2.3,17.8c0-2.8,0.9-5.5,2.7-7.7l17.6,17.4c-2.1,1.7-4.8,2.6-7.5,2.6
	C8.1,30.3,2.4,24.8,2.3,17.8L2.3,17.8z M14.8,5.4c6.9,0,12.5,5.5,12.5,12.4c0,2.9-1,5.7-2.8,7.9L6.8,8.2C9.1,6.3,11.9,5.4,14.8,5.4
	L14.8,5.4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->

		</div>
		<div id="footer_meta">
			<nav>
				<ul>
					<li><a href="http://www.yugioh-card.com/japan/support/" target="_blank">お問い合わせ</a></li>
					<li><a href="https://www.konami.com/siteinfo/ja/" target="_blank">サイトポリシー</a></li>
					<li><a href="https://legal.konami.com/games/privacy-jp/ja/" target="_blank">個人情報等保護方針</a></li>
				
					<li>
						<!-- OneTrust Cookie 設定ボタンの始点 -->
						<button id="ot-sdk-btn" class="ot-sdk-show-settings">Cookie 設定</button>
						<!-- OneTrust Cookie 設定ボタンの終点 -->
					</li>
				</ul>
			</nav>
			<small>&copy;2023 Konami Digital Entertainment</small>

		</div>
	</footer>
	<nav id="footer_icon">
		<div>
				<ul class="main_menu">
					
					<li class="menu_top"><a href="/yugiohdb/"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"/></svg><h3>Top</h3></a></li>

					
					<li class="menu_card_search">
						<a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.35 28.26"><defs></defs><path  d="M13.44,23.3,2.21,21.64,3.93,10l3.52.52a11.1,11.1,0,0,1,.63-3.12l-5-.74-3,20.27,14,2.06,1.08-7.32a12.7,12.7,0,0,1-1.33-.53Zm-1.76-14,5.14.76-1.11,7.48a6.7,6.7,0,0,0,1.69.5L19.12,6.39,14,5.63a7,7,0,0,0-2.37,3.69ZM26.17,20l-.66.4L24.66,19a10,10,0,1,0-2.23,1.3l.85,1.44-.67.4,4.25,7.2,3.57-2.11Zm-3.73-2.21A7.82,7.82,0,1,1,25.2,7.1a7.83,7.83,0,0,1-2.76,10.71Z" transform="translate(-0.08 -1.07)"/></svg><h3>カード検索</h3></a>

					</li>

					
					<li class="menu_cardlist sab_menu">
						<a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 33.07 29.79"><defs></defs><path d="M128.74,4.57l-1.11,13.66-1-.08,1.63,5.31-3.2,1,3.66.3,1.94-23.71L121.15.28l1.17,3.79ZM120.44,0,104.77,4.79l7,22.75,15.67-4.8Zm-9.06,21-4-13.11L120,4l4,13.1ZM131.13,5l-.31,3.78,4.33,1.43-4.3,13-1.18-.39-.25,3.06-7.08-.58-2.89.88,10.93,3.61,7.46-22.58Z" transform="translate(-104.77)"/></svg><h3>カードリスト</h3></a>
					</li>

					
					<li class="menu_decks">
						<a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 35.46 28.79"><defs></defs><path d="M452,16.6a11,11,0,0,1-1.39-7.34l-1.65.26V29l8.35-1.73V21.19A10.91,10.91,0,0,1,452,16.6ZM451.16,7l-4.78-.4-8.07,1-.18.61V19l10.09,1.74V9.52l.38-.73,2.12-.32A9.87,9.87,0,0,1,451.16,7ZM439,27.26,448.22,29V21.17L439,19.6Zm30.21-7.13-.69.4-.85-1.45a10.22,10.22,0,1,0-2.23,1.33l.86,1.46-.68.41L470,29.61l3.64-2.14Zm-3.77-2.27a8,8,0,1,1,2.78-11l0,.06A8,8,0,0,1,465.44,17.86Zm1-12-9.12-.75a7.16,7.16,0,0,0-2.07,9.51.83.83,0,0,1,.08.12V8.51l.51-1,10.67-1.63ZM456.25,15.92a7.14,7.14,0,0,0,10.09.27,7,7,0,0,0,.85-1V6.8L456.25,8.51Z" transform="translate(-438.13 -0.82)"/></svg><h3>デッキ検索</h3></a>
					</li>
				
					<li class="menu_trends">
				
						<a href="/yugiohdb/trends_search.action?ope=1">
				
				
							<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.32"><defs></defs><g ><g ><path  d="M11.92,36.35l10.8,1.97v-7.46l-10.8-1.8v7.29Zm11.88,1.95l8.64-.96V14.78l-8.64,.96v22.56Zm-1.82-25.73l-11.14,1.01v14.04l11.88,1.98V14.66l6.25-.69-6.99-1.4ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"/></g></g></svg>
							<h3>トレンド</h3>
						</a>
					</li>


				

					
					<li class="menu_q_a">
						<a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.73 27.45"><defs></defs><path  d="M370.6,22.79A1.66,1.66,0,1,0,369,21.12v0A1.65,1.65,0,0,0,370.6,22.79Zm-10.11-5.65a1,1,0,0,0,.75-.63,1.82,1.82,0,0,0,.09-.8,2,2,0,0,1,0-.59,2.8,2.8,0,0,1,.2-.62,2.88,2.88,0,0,1,3.08-1.37,3.8,3.8,0,0,1,1.5.85,3.47,3.47,0,0,1,1,1.87,2,2,0,0,1,0,.69,3.28,3.28,0,0,1-.21.86A5.07,5.07,0,0,1,365,19.07c-.28.18-1,.52-1.11.81s.11.68.22.93l.95,2.1c.09.21.27.8.61.74a1.57,1.57,0,0,0,.54-.29c.18-.13.48-.25.57-.46a.6.6,0,0,0,0-.49,2.71,2.71,0,0,0-.21-.37c-.13-.21-.25-.42-.37-.63s-.3-.37-.15-.59a2.13,2.13,0,0,1,.65-.42l.42-.29a4.71,4.71,0,0,0,1.6-1.91,6.46,6.46,0,0,0,.36-1.21,4.79,4.79,0,0,0-.44-3,5.11,5.11,0,0,0-3.53-2.49,8.79,8.79,0,0,0-1.14-.11h-.58a10.28,10.28,0,0,0-1.08.21,4.51,4.51,0,0,0-2.93,2.87c-.28.72-.55,2,.12,2.46a1,1,0,0,0,.94.19Zm1.19-11.25H369l.09-.14a4.42,4.42,0,0,1,1.07-1,6.55,6.55,0,0,1,6.18-.87,6.31,6.31,0,0,1,2.37,1.57V1.76H360.21v10.4a4.46,4.46,0,0,1,1.47-1Zm17.9,2.2a6,6,0,0,0-6-4,5.86,5.86,0,0,0-3.45,1.41,3.37,3.37,0,0,0-.69.67,1.62,1.62,0,0,0-.3,1.57,1.21,1.21,0,0,0,.83.66c1.13.29,1.51-.82,2-1.39a2.14,2.14,0,0,1,.58-.46,2.75,2.75,0,0,1,.79-.33,3.64,3.64,0,0,1,4.29,3.19,3.87,3.87,0,0,1-.06,1.44,3.19,3.19,0,0,1-1.89,2.43,7.33,7.33,0,0,1-3.42.12,1.09,1.09,0,0,0-1.09.27,4.34,4.34,0,0,0-.27,1.13l-.51,2.53c-.11.47-.22.91.29,1h.62c1.29.21,1-.77,1.15-1.7.07-.4-.05-.73.28-.87a2,2,0,0,1,.9,0,5,5,0,0,0,1.44,0,7.09,7.09,0,0,0,1.21-.28A5.71,5.71,0,0,0,379,13.35,7.49,7.49,0,0,0,379.58,8.09ZM365.72,25.43A1.47,1.47,0,1,0,367.19,24a1.47,1.47,0,0,0-1.47,1.48Zm11.47-3.29h-4.6a2.22,2.22,0,0,1-4,0h-1.24a3.25,3.25,0,0,1,.11.42,1.26,1.26,0,0,1-.13.63,1.22,1.22,0,0,1-.2.25h0a2,2,0,1,1-2,2,2,2,0,0,1,.42-1.24.93.93,0,0,1-.29-.05c-.4-.13-.6-.64-.76-1l-.45-1h-2.44V16.91a1.65,1.65,0,0,1-1.47.87V29.21H378.6V14.76a5,5,0,0,1-1.47,1.06Z" transform="translate(-359.09 -1.76)"/></svg><h3>Ｑ＆Ａ</h3></a>
					</li>
				
					
					<li class="menu_forbidden">
						<a href="/yugiohdb/forbidden_limited.action"><?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.6.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="レイヤー_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="25.3px" height="27.7px" viewBox="0 0 25.3 27.7" style="enable-background:new 0 0 25.3 27.7;"
	 xml:space="preserve">
<path d="M25.3,13.7L25.3,13.7C25.3,13.7,25.3,13.7,25.3,13.7c0-7-5.7-12.7-12.6-12.7C5.7,1,0,6.7,0,13.6s5.7,12.6,12.6,12.6
	C19.6,26.3,25.2,20.7,25.3,13.7z M3,13.7c0-2.1,0.7-4.1,2-5.8l13.1,13.7c-1.6,1.1-3.5,1.7-5.5,1.7C7.3,23.3,3,19,3,13.7L3,13.7z
	 M12.6,4c2.1,0,4.1,0.7,5.8,2c4.2,3.2,5.1,9.3,1.8,13.5L7.2,5.7C8.8,4.6,10.7,4,12.6,4L12.6,4z"/>
</svg>
<h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br />レギュレーション</span></h3></a>
					</li>
					<li class="menu_btn_pagetop"><a href="#"><?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path  d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"/></svg></a></li>

				</ul><!--#main_menu-->
		</div>
	</nav>
</div><!--wrapper-->
<noscript>JavaScript を有効にしてください</noscript>

</body>
</html>""",
            "err_msg": "メインデッキのモンスター情報が正しく取得できませんでした。"
        }
    ]

    @pytest.mark.parametrize("test_data", generate_monsters_exception_test_datas)
    def test_generate_monsters_exception(self, test_data):
        """
        generate_monsters()異常系のテスト
        """
        # 準備
        parser = HtmlParser(test_data["html"])

        # 実行
        with pytest.raises(AttributeError) as e:
            parser.generate_monsters()

        # 検証
        assert str(e.value) == test_data["err_msg"], test_data["note"]
