import pytest
from src.html_parser import HtmlParser


@pytest.fixture
def fixture_2monsters_html():
    html = """<html><head>




  <meta http-equiv="x-ua-compatible" content="IE=10">
  <meta http-equiv="x-ua-compatible" content="IE=EmulateIE10">

  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <meta http-equiv="Content-Language" content="ja">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <meta http-equiv="Content-Script-Type" content="text/javascript">
  <meta http-equiv="imagetoolbar" content="no">

  <meta property="og:site_name" content="遊戯王OCGカードデータベース">

  <meta property="og:type" content="product">
  <meta property="og:locale" content="ja_JP">

  <meta name="twitter:card" content="summary">

  <script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-DSVT4C66K4&amp;l=dataLayer&amp;cx=c"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script id="facebook-jssdk" src="//connect.facebook.net/ja_JP/sdk.js#xfbml=1&amp;version=v2.9"></script><script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-PWR3GWF"></script><script type="text/javascript" src="/yugiohdb/ga.js"></script>
  <meta name="copyright" content="KONAMI">
  <link rel="shortcut icon" href="external/image/yugioh.ico">
  <link rel="apple-touch-icon" href="external/image/apple-touch-icon.png">


  


  


  


  <meta name="keywords" content="モンスター2種,遊戯王,デッキ,デュエルモンスターズ,VRAINS,ヴレインズ,禁止,制限,パック,禁止カード,カード,カードリスト,ルール,OCG,コナミ,KONAMI">
  <meta name="description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細">
  <meta property="title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">

  <meta property="og:title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">
  <meta property="og:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202306110137">

  <meta property="og:description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細">

  <meta name="twitter:title" content="モンスター2種 | 遊戯王 デッキレシピ 詳細 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース">
  <meta name="twitter:description" content="モンスター2種 | 遊戯王 オフィシャルカードゲーム デュエルモンスターズ カードデータベース　デッキ詳細">

  <meta name="twitter:url" content="http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202306110137">

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



<meta property="og:image" content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&amp;osplang=1&amp;cid=13571&amp;ciid=1&amp;enc=4Mp-kHZoU5G8AmEG5-_lBg&amp;app=tournament&amp;request_locale=ja&amp;a=202306110137">
<meta name="twitter:image" content="https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=1&amp;osplang=1&amp;cid=13571&amp;ciid=1&amp;enc=4Mp-kHZoU5G8AmEG5-_lBg&amp;app=tournament&amp;request_locale=ja&amp;a=202306110137">


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

    
    
        $('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
        $('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
        $('.card_image_monster_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13571&ciid=1&enc=4Mp-kHZoU5G8AmEG5-_lBg&osplang=1').show();
    
        $('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
        $('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
        $('.card_image_monster_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=17430&ciid=1&enc=QF5Ab2yaHTaaC0wF6ydPiQ&osplang=1').show();
    
    
      
        $('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
        $('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
        $('.card_image_spell_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14301&ciid=1&enc=eKqWv3RZUlLbRgj2UIOcEw&osplang=1').show();
      
    
      
        $('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
        $('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
        $('.card_image_spell_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14753&ciid=1&enc=hEVU1Z6Vxzh7k3daV-CWlQ&osplang=1').show();
      
    
      
        $('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
        $('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
        $('.card_image_spell_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=16555&ciid=1&enc=iVMSFkScU-fjDqNLnPehag&osplang=1').show();
      
    
      
        $('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
        $('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
        $('.card_image_spell_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13938&ciid=1&enc=skW_u1Fh9fSjERjVP3R9pQ&osplang=1').show();
      
    
      
        $('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
        $('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
        $('.card_image_spell_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13619&ciid=1&enc=diw-7xfIox8Qjat1B7yuOQ&osplang=1').show();
      
    
      
        $('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
        $('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
        $('.card_image_spell_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14627&ciid=1&enc=zKQ4xQyAG_Gqp9XOrwth_A&osplang=1').show();
      
    
      
        $('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
        $('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
        $('.card_image_spell_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=7493&ciid=1&enc=lE4aw0FCFXSt3sdyZSo5Bg&osplang=1').show();
      
    
      
        $('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
        $('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
        $('.card_image_spell_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=6524&ciid=1&enc=o1shmrowuYfBP5yde57ynQ&osplang=1').show();
      
    
    
      
        $('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
        $('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
        $('.card_image_trap_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=5914&ciid=1&enc=KXIN7gIpf-qauKs9iEtt2A&osplang=1').show();
      
    
      
        $('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
        $('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
        $('.card_image_trap_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13631&ciid=1&enc=GNP_kIy6vDlGQ3wGgRb3wg&osplang=1').show();
      
    
      
        $('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
        $('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
        $('.card_image_trap_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14755&ciid=1&enc=-8Likk9Nlg-63giBwYaogQ&osplang=1').show();
      
    
      
        $('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
        $('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
        $('.card_image_trap_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13878&ciid=1&enc=tHtWCS9qQ21aY_eKHBVAiA&osplang=1').show();
      
    
      
        $('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
        $('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
        $('.card_image_trap_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=9008&ciid=1&enc=YoWuM7VNM10h5Zp4J74p_w&osplang=1').show();
      
    
    
      
        $('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
        $('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
        $('.card_image_extra_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14752&ciid=1&enc=MyVu56tUC4oxGA7fZQTeHA&osplang=1').show();
      
    
      
        $('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
        $('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
        $('.card_image_extra_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
      
    
      
        $('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
        $('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
        $('.card_image_extra_2_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13034&ciid=1&enc=BBMQTHLvAxC72VC8PbGTvw&osplang=1').show();
      
    
      
        $('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
        $('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
        $('.card_image_extra_3_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14249&ciid=1&enc=qmd0pcUnBQXTPIXsGVjlZw&osplang=1').show();
      
    
      
        $('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
        $('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
        $('.card_image_extra_4_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14338&ciid=1&enc=MO4r0tjPhynLtnfy68AVaw&osplang=1').show();
      
    
      
        $('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
        $('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
        $('.card_image_extra_5_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13460&ciid=1&enc=r51L46PP0F1Hhn5XbdIkww&osplang=1').show();
      
    
      
        $('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
        $('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
        $('.card_image_extra_6_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14122&ciid=1&enc=UjSpu_jmocbM1pvH3TrgsA&osplang=1').show();
      
    
      
        $('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
        $('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
        $('.card_image_extra_7_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15034&ciid=1&enc=J3jhN5NFlU0H8mJSSFvWYQ&osplang=1').show();
      
    
      
        $('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
        $('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
        $('.card_image_extra_8_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13698&ciid=1&enc=3LsccTlxzA4ckR1VHhE5rg&osplang=1').show();
      
    
      
        $('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
        $('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
        $('.card_image_extra_9_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14962&ciid=1&enc=OlNxTfT7jJQZosZo-2SkhQ&osplang=1').show();
      
    
      
        $('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
        $('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
        $('.card_image_extra_10_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=13082&ciid=1&enc=voYX8-89zJtbQv82-9LugA&osplang=1').show();
      
    
      
        $('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
        $('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
        $('.card_image_extra_11_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=15032&ciid=1&enc=w7j6BmFBc2iOiY0--hPaUw&osplang=1').show();
      
    
    
      
        $('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
        $('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
        $('.card_image_side_0_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14800&ciid=1&enc=u_nVY2UkC0dUvcFYh23FhA&osplang=1').show();
      
    
      
        $('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
        $('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
        $('.card_image_side_1_1').attr('src', '/yugiohdb/get_image.action?type=1&lang=ja&cid=14904&ciid=1&enc=F6fcPMqoCYfgnIXO0G1lHA&osplang=1').show();
      
    
      
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
      location.href = "/yugiohdb/member_deck.action?ope=7&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja";
    }
  }

  function updateDeckFavorite(){
    var chngeFavoriteCnt = document.getElementById("favoriteCnt");
    var mycount = 1;
    if (deckFavorite.checked) {
      $.ajax({
        type: 'get',
        url: '/yugiohdb/member_deck.action?ope=9&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
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
        url: '/yugiohdb/member_deck.action?ope=10&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
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
        url: '/yugiohdb/member_deck.action?ope=11&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
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
        url: '/yugiohdb/member_deck.action?ope=12&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=70&request_locale=ja',
        success: function() {
        },
        error: function(xhr, status, error) {
        }
      });
  }

//-->
</script>




  

<script src="https://cdn-apac.onetrust.com/scripttemplates/202211.2.0/otBannerSdk.js" async="" type="text/javascript"></script><style id="onetrust-style">#onetrust-banner-sdk{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}#onetrust-banner-sdk .onetrust-vendors-list-handler{cursor:pointer;color:#1f96db;font-size:inherit;font-weight:bold;text-decoration:none;margin-left:5px}#onetrust-banner-sdk .onetrust-vendors-list-handler:hover{color:#1f96db}#onetrust-banner-sdk:focus{outline:2px solid #000;outline-offset:-2px}#onetrust-banner-sdk a:focus{outline:2px solid #000}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{outline-offset:1px}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{height:64px;width:64px}#onetrust-banner-sdk .ot-close-icon,#onetrust-pc-sdk .ot-close-icon,#ot-sync-ntfy .ot-close-icon{background-size:contain;background-repeat:no-repeat;background-position:center;height:12px;width:12px}#onetrust-banner-sdk .powered-by-logo,#onetrust-banner-sdk .ot-pc-footer-logo a,#onetrust-pc-sdk .powered-by-logo,#onetrust-pc-sdk .ot-pc-footer-logo a,#ot-sync-ntfy .powered-by-logo,#ot-sync-ntfy .ot-pc-footer-logo a{background-size:contain;background-repeat:no-repeat;background-position:center;height:25px;width:152px;display:block;text-decoration:none;font-size:0.75em}#onetrust-banner-sdk .powered-by-logo:hover,#onetrust-banner-sdk .ot-pc-footer-logo a:hover,#onetrust-pc-sdk .powered-by-logo:hover,#onetrust-pc-sdk .ot-pc-footer-logo a:hover,#ot-sync-ntfy .powered-by-logo:hover,#ot-sync-ntfy .ot-pc-footer-logo a:hover{color:#565656}#onetrust-banner-sdk h3 *,#onetrust-banner-sdk h4 *,#onetrust-banner-sdk h6 *,#onetrust-banner-sdk button *,#onetrust-banner-sdk a[data-parent-id] *,#onetrust-pc-sdk h3 *,#onetrust-pc-sdk h4 *,#onetrust-pc-sdk h6 *,#onetrust-pc-sdk button *,#onetrust-pc-sdk a[data-parent-id] *,#ot-sync-ntfy h3 *,#ot-sync-ntfy h4 *,#ot-sync-ntfy h6 *,#ot-sync-ntfy button *,#ot-sync-ntfy a[data-parent-id] *{font-size:inherit;font-weight:inherit;color:inherit}#onetrust-banner-sdk .ot-hide,#onetrust-pc-sdk .ot-hide,#ot-sync-ntfy .ot-hide{display:none !important}#onetrust-banner-sdk button.ot-link-btn:hover,#onetrust-pc-sdk button.ot-link-btn:hover,#ot-sync-ntfy button.ot-link-btn:hover{text-decoration:underline;opacity:1}#onetrust-pc-sdk .ot-sdk-row .ot-sdk-column{padding:0}#onetrust-pc-sdk .ot-sdk-container{padding-right:0}#onetrust-pc-sdk .ot-sdk-row{flex-direction:initial;width:100%}#onetrust-pc-sdk [type="checkbox"]:checked,#onetrust-pc-sdk [type="checkbox"]:not(:checked){pointer-events:initial}#onetrust-pc-sdk [type="checkbox"]:disabled+label::before,#onetrust-pc-sdk [type="checkbox"]:disabled+label:after,#onetrust-pc-sdk [type="checkbox"]:disabled+label{pointer-events:none;opacity:0.7}#onetrust-pc-sdk #vendor-list-content{transform:translate3d(0, 0, 0)}#onetrust-pc-sdk li input[type="checkbox"]{z-index:1}#onetrust-pc-sdk li .ot-checkbox label{z-index:2}#onetrust-pc-sdk li .ot-checkbox input[type="checkbox"]{height:auto;width:auto}#onetrust-pc-sdk li .host-title a,#onetrust-pc-sdk li .ot-host-name a,#onetrust-pc-sdk li .accordion-text,#onetrust-pc-sdk li .ot-acc-txt{z-index:2;position:relative}#onetrust-pc-sdk input{margin:3px 0.1ex}#onetrust-pc-sdk .pc-logo,#onetrust-pc-sdk .ot-pc-logo{height:60px;width:180px;background-position:center;background-size:contain;background-repeat:no-repeat;display:inline-flex;justify-content:center;align-items:center}#onetrust-pc-sdk .pc-logo img,#onetrust-pc-sdk .ot-pc-logo img{max-height:100%;max-width:100%}#onetrust-pc-sdk .screen-reader-only,#onetrust-pc-sdk .ot-scrn-rdr,.ot-sdk-cookie-policy .screen-reader-only,.ot-sdk-cookie-policy .ot-scrn-rdr{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}#onetrust-pc-sdk.ot-fade-in,.onetrust-pc-dark-filter.ot-fade-in,#onetrust-banner-sdk.ot-fade-in{animation-name:onetrust-fade-in;animation-duration:400ms;animation-timing-function:ease-in-out}#onetrust-pc-sdk.ot-hide{display:none !important}.onetrust-pc-dark-filter.ot-hide{display:none !important}#ot-sdk-btn.ot-sdk-show-settings,#ot-sdk-btn.optanon-show-settings{color:#68b631;border:1px solid #68b631;height:auto;white-space:normal;word-wrap:break-word;padding:0.8em 2em;font-size:0.8em;line-height:1.2;cursor:pointer;-moz-transition:0.1s ease;-o-transition:0.1s ease;-webkit-transition:1s ease;transition:0.1s ease}#ot-sdk-btn.ot-sdk-show-settings:hover,#ot-sdk-btn.optanon-show-settings:hover{color:#fff;background-color:#68b631}.onetrust-pc-dark-filter{background:rgba(0,0,0,0.5);z-index:2147483646;width:100%;height:100%;overflow:hidden;position:fixed;top:0;bottom:0;left:0}@keyframes onetrust-fade-in{0%{opacity:0}100%{opacity:1}}.ot-cookie-label{text-decoration:underline}@media only screen and (min-width: 426px) and (max-width: 896px) and (orientation: landscape){#onetrust-pc-sdk p{font-size:0.75em}}#onetrust-banner-sdk .banner-option-input:focus+label{outline:1px solid #000;outline-style:auto}.category-vendors-list-handler+a:focus,.category-vendors-list-handler+a:focus-visible{outline:2px solid #000}#onetrust-pc-sdk .ot-userid-title{margin-top:10px}#onetrust-pc-sdk .ot-userid-title>span,#onetrust-pc-sdk .ot-userid-timestamp>span{font-weight:700}#onetrust-pc-sdk .ot-userid-desc{font-style:italic}#onetrust-pc-sdk .ot-host-desc a{pointer-events:initial}#onetrust-pc-sdk .ot-ven-hdr>p a{position:relative;z-index:2;pointer-events:initial}#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info a{margin-right:auto}#onetrust-pc-sdk .ot-pc-footer-logo img{width:136px;height:16px}#onetrust-banner-sdk .ot-optout-signal,#onetrust-pc-sdk .ot-optout-signal{border:1px solid #32ae88;border-radius:3px;padding:5px;margin-bottom:10px;background-color:#f9fffa;font-size:0.85rem;line-height:2}#onetrust-banner-sdk .ot-optout-signal .ot-optout-icon,#onetrust-pc-sdk .ot-optout-signal .ot-optout-icon{display:inline;margin-right:5px}#onetrust-banner-sdk .ot-optout-signal svg,#onetrust-pc-sdk .ot-optout-signal svg{height:20px;width:30px;transform:scale(0.5)}#onetrust-banner-sdk .ot-optout-signal svg path,#onetrust-pc-sdk .ot-optout-signal svg path{fill:#32ae88}
#onetrust-banner-sdk,#onetrust-pc-sdk,#ot-sdk-cookie-policy,#ot-sync-ntfy{font-size:16px}#onetrust-banner-sdk *,#onetrust-banner-sdk ::after,#onetrust-banner-sdk ::before,#onetrust-pc-sdk *,#onetrust-pc-sdk ::after,#onetrust-pc-sdk ::before,#ot-sdk-cookie-policy *,#ot-sdk-cookie-policy ::after,#ot-sdk-cookie-policy ::before,#ot-sync-ntfy *,#ot-sync-ntfy ::after,#ot-sync-ntfy ::before{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}#onetrust-banner-sdk div,#onetrust-banner-sdk span,#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-banner-sdk p,#onetrust-banner-sdk img,#onetrust-banner-sdk svg,#onetrust-banner-sdk button,#onetrust-banner-sdk section,#onetrust-banner-sdk a,#onetrust-banner-sdk label,#onetrust-banner-sdk input,#onetrust-banner-sdk ul,#onetrust-banner-sdk li,#onetrust-banner-sdk nav,#onetrust-banner-sdk table,#onetrust-banner-sdk thead,#onetrust-banner-sdk tr,#onetrust-banner-sdk td,#onetrust-banner-sdk tbody,#onetrust-banner-sdk .ot-main-content,#onetrust-banner-sdk .ot-toggle,#onetrust-banner-sdk #ot-content,#onetrust-banner-sdk #ot-pc-content,#onetrust-banner-sdk .checkbox,#onetrust-pc-sdk div,#onetrust-pc-sdk span,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#onetrust-pc-sdk p,#onetrust-pc-sdk img,#onetrust-pc-sdk svg,#onetrust-pc-sdk button,#onetrust-pc-sdk section,#onetrust-pc-sdk a,#onetrust-pc-sdk label,#onetrust-pc-sdk input,#onetrust-pc-sdk ul,#onetrust-pc-sdk li,#onetrust-pc-sdk nav,#onetrust-pc-sdk table,#onetrust-pc-sdk thead,#onetrust-pc-sdk tr,#onetrust-pc-sdk td,#onetrust-pc-sdk tbody,#onetrust-pc-sdk .ot-main-content,#onetrust-pc-sdk .ot-toggle,#onetrust-pc-sdk #ot-content,#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk .checkbox,#ot-sdk-cookie-policy div,#ot-sdk-cookie-policy span,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy p,#ot-sdk-cookie-policy img,#ot-sdk-cookie-policy svg,#ot-sdk-cookie-policy button,#ot-sdk-cookie-policy section,#ot-sdk-cookie-policy a,#ot-sdk-cookie-policy label,#ot-sdk-cookie-policy input,#ot-sdk-cookie-policy ul,#ot-sdk-cookie-policy li,#ot-sdk-cookie-policy nav,#ot-sdk-cookie-policy table,#ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy tr,#ot-sdk-cookie-policy td,#ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy .ot-main-content,#ot-sdk-cookie-policy .ot-toggle,#ot-sdk-cookie-policy #ot-content,#ot-sdk-cookie-policy #ot-pc-content,#ot-sdk-cookie-policy .checkbox,#ot-sync-ntfy div,#ot-sync-ntfy span,#ot-sync-ntfy h1,#ot-sync-ntfy h2,#ot-sync-ntfy h3,#ot-sync-ntfy h4,#ot-sync-ntfy h5,#ot-sync-ntfy h6,#ot-sync-ntfy p,#ot-sync-ntfy img,#ot-sync-ntfy svg,#ot-sync-ntfy button,#ot-sync-ntfy section,#ot-sync-ntfy a,#ot-sync-ntfy label,#ot-sync-ntfy input,#ot-sync-ntfy ul,#ot-sync-ntfy li,#ot-sync-ntfy nav,#ot-sync-ntfy table,#ot-sync-ntfy thead,#ot-sync-ntfy tr,#ot-sync-ntfy td,#ot-sync-ntfy tbody,#ot-sync-ntfy .ot-main-content,#ot-sync-ntfy .ot-toggle,#ot-sync-ntfy #ot-content,#ot-sync-ntfy #ot-pc-content,#ot-sync-ntfy .checkbox{font-family:inherit;font-weight:normal;-webkit-font-smoothing:auto;letter-spacing:normal;line-height:normal;padding:0;margin:0;height:auto;min-height:0;max-height:none;width:auto;min-width:0;max-width:none;border-radius:0;border:none;clear:none;float:none;position:static;bottom:auto;left:auto;right:auto;top:auto;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;white-space:normal;background:none;overflow:visible;vertical-align:baseline;visibility:visible;z-index:auto;box-shadow:none}#onetrust-banner-sdk label:before,#onetrust-banner-sdk label:after,#onetrust-banner-sdk .checkbox:after,#onetrust-banner-sdk .checkbox:before,#onetrust-pc-sdk label:before,#onetrust-pc-sdk label:after,#onetrust-pc-sdk .checkbox:after,#onetrust-pc-sdk .checkbox:before,#ot-sdk-cookie-policy label:before,#ot-sdk-cookie-policy label:after,#ot-sdk-cookie-policy .checkbox:after,#ot-sdk-cookie-policy .checkbox:before,#ot-sync-ntfy label:before,#ot-sync-ntfy label:after,#ot-sync-ntfy .checkbox:after,#ot-sync-ntfy .checkbox:before{content:"";content:none}
#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{position:relative;width:100%;max-width:100%;margin:0 auto;padding:0 20px;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{width:100%;float:left;box-sizing:border-box;padding:0;display:initial}@media (min-width: 400px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:90%;padding:0}}@media (min-width: 550px){#onetrust-banner-sdk .ot-sdk-container,#onetrust-pc-sdk .ot-sdk-container,#ot-sdk-cookie-policy .ot-sdk-container{width:100%}#onetrust-banner-sdk .ot-sdk-column,#onetrust-banner-sdk .ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-column,#onetrust-pc-sdk .ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-column,#ot-sdk-cookie-policy .ot-sdk-columns{margin-left:4%}#onetrust-banner-sdk .ot-sdk-column:first-child,#onetrust-banner-sdk .ot-sdk-columns:first-child,#onetrust-pc-sdk .ot-sdk-column:first-child,#onetrust-pc-sdk .ot-sdk-columns:first-child,#ot-sdk-cookie-policy .ot-sdk-column:first-child,#ot-sdk-cookie-policy .ot-sdk-columns:first-child{margin-left:0}#onetrust-banner-sdk .ot-sdk-two.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-two.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-two.ot-sdk-columns{width:13.3333333333%}#onetrust-banner-sdk .ot-sdk-three.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-three.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-three.ot-sdk-columns{width:22%}#onetrust-banner-sdk .ot-sdk-four.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-four.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-four.ot-sdk-columns{width:30.6666666667%}#onetrust-banner-sdk .ot-sdk-eight.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eight.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eight.ot-sdk-columns{width:65.3333333333%}#onetrust-banner-sdk .ot-sdk-nine.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-nine.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-nine.ot-sdk-columns{width:74%}#onetrust-banner-sdk .ot-sdk-ten.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-ten.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-ten.ot-sdk-columns{width:82.6666666667%}#onetrust-banner-sdk .ot-sdk-eleven.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-eleven.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-eleven.ot-sdk-columns{width:91.3333333333%}#onetrust-banner-sdk .ot-sdk-twelve.ot-sdk-columns,#onetrust-pc-sdk .ot-sdk-twelve.ot-sdk-columns,#ot-sdk-cookie-policy .ot-sdk-twelve.ot-sdk-columns{width:100%;margin-left:0}}#onetrust-banner-sdk h1,#onetrust-banner-sdk h2,#onetrust-banner-sdk h3,#onetrust-banner-sdk h4,#onetrust-banner-sdk h5,#onetrust-banner-sdk h6,#onetrust-pc-sdk h1,#onetrust-pc-sdk h2,#onetrust-pc-sdk h3,#onetrust-pc-sdk h4,#onetrust-pc-sdk h5,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h1,#ot-sdk-cookie-policy h2,#ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy h5,#ot-sdk-cookie-policy h6{margin-top:0;font-weight:600;font-family:inherit}#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem;line-height:1.2}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem;line-height:1.25}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem;line-height:1.3}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem;line-height:1.35}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem;line-height:1.5}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem;line-height:1.6}@media (min-width: 550px){#onetrust-banner-sdk h1,#onetrust-pc-sdk h1,#ot-sdk-cookie-policy h1{font-size:1.5rem}#onetrust-banner-sdk h2,#onetrust-pc-sdk h2,#ot-sdk-cookie-policy h2{font-size:1.5rem}#onetrust-banner-sdk h3,#onetrust-pc-sdk h3,#ot-sdk-cookie-policy h3{font-size:1.5rem}#onetrust-banner-sdk h4,#onetrust-pc-sdk h4,#ot-sdk-cookie-policy h4{font-size:1.5rem}#onetrust-banner-sdk h5,#onetrust-pc-sdk h5,#ot-sdk-cookie-policy h5{font-size:1.5rem}#onetrust-banner-sdk h6,#onetrust-pc-sdk h6,#ot-sdk-cookie-policy h6{font-size:1.5rem}}#onetrust-banner-sdk p,#onetrust-pc-sdk p,#ot-sdk-cookie-policy p{margin:0 0 1em 0;font-family:inherit;line-height:normal}#onetrust-banner-sdk a,#onetrust-pc-sdk a,#ot-sdk-cookie-policy a{color:#565656;text-decoration:underline}#onetrust-banner-sdk a:hover,#onetrust-pc-sdk a:hover,#ot-sdk-cookie-policy a:hover{color:#565656;text-decoration:none}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-button,#onetrust-banner-sdk button,#onetrust-pc-sdk .ot-sdk-button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy .ot-sdk-button,#ot-sdk-cookie-policy button{display:inline-block;height:38px;padding:0 30px;color:#555;text-align:center;font-size:0.9em;font-weight:400;line-height:38px;letter-spacing:0.01em;text-decoration:none;white-space:nowrap;background-color:transparent;border-radius:2px;border:1px solid #bbb;cursor:pointer;box-sizing:border-box}#onetrust-banner-sdk .ot-sdk-button:hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#onetrust-pc-sdk .ot-sdk-button:hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus,#ot-sdk-cookie-policy .ot-sdk-button:hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):hover,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:not(.ot-link-btn):focus{color:#333;border-color:#888;opacity:0.7}#onetrust-banner-sdk .ot-sdk-button:focus,#onetrust-banner-sdk :not(.ot-leg-btn-container)>button:focus,#onetrust-pc-sdk .ot-sdk-button:focus,#onetrust-pc-sdk :not(.ot-leg-btn-container)>button:focus,#ot-sdk-cookie-policy .ot-sdk-button:focus,#ot-sdk-cookie-policy :not(.ot-leg-btn-container)>button:focus{outline:2px solid #000}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-banner-sdk button.ot-sdk-button-primary,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary,#onetrust-pc-sdk button.ot-sdk-button-primary,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary,#ot-sdk-cookie-policy button.ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary{color:#fff;background-color:#33c3f0;border-color:#33c3f0}#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-banner-sdk button.ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-banner-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-banner-sdk button.ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-banner-sdk input[type="button"].ot-sdk-button-primary:focus,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:hover,#onetrust-pc-sdk button.ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:hover,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:hover,#onetrust-pc-sdk .ot-sdk-button.ot-sdk-button-primary:focus,#onetrust-pc-sdk button.ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="submit"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="reset"].ot-sdk-button-primary:focus,#onetrust-pc-sdk input[type="button"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy button.ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:hover,#ot-sdk-cookie-policy .ot-sdk-button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy button.ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="submit"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="reset"].ot-sdk-button-primary:focus,#ot-sdk-cookie-policy input[type="button"].ot-sdk-button-primary:focus{color:#fff;background-color:#1eaedb;border-color:#1eaedb}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{height:38px;padding:6px 10px;background-color:#fff;border:1px solid #d1d1d1;border-radius:4px;box-shadow:none;box-sizing:border-box}#onetrust-banner-sdk input[type="text"],#onetrust-pc-sdk input[type="text"],#ot-sdk-cookie-policy input[type="text"]{-webkit-appearance:none;-moz-appearance:none;appearance:none}#onetrust-banner-sdk input[type="text"]:focus,#onetrust-pc-sdk input[type="text"]:focus,#ot-sdk-cookie-policy input[type="text"]:focus{border:1px solid #000;outline:0}#onetrust-banner-sdk label,#onetrust-pc-sdk label,#ot-sdk-cookie-policy label{display:block;margin-bottom:0.5rem;font-weight:600}#onetrust-banner-sdk input[type="checkbox"],#onetrust-pc-sdk input[type="checkbox"],#ot-sdk-cookie-policy input[type="checkbox"]{display:inline}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{list-style:circle inside}#onetrust-banner-sdk ul,#onetrust-pc-sdk ul,#ot-sdk-cookie-policy ul{padding-left:0;margin-top:0}#onetrust-banner-sdk ul ul,#onetrust-pc-sdk ul ul,#ot-sdk-cookie-policy ul ul{margin:1.5rem 0 1.5rem 3rem;font-size:90%}#onetrust-banner-sdk li,#onetrust-pc-sdk li,#ot-sdk-cookie-policy li{margin-bottom:1rem}#onetrust-banner-sdk th,#onetrust-banner-sdk td,#onetrust-pc-sdk th,#onetrust-pc-sdk td,#ot-sdk-cookie-policy th,#ot-sdk-cookie-policy td{padding:12px 15px;text-align:left;border-bottom:1px solid #e1e1e1}#onetrust-banner-sdk button,#onetrust-pc-sdk button,#ot-sdk-cookie-policy button{margin-bottom:1rem;font-family:inherit}#onetrust-banner-sdk .ot-sdk-container:after,#onetrust-banner-sdk .ot-sdk-row:after,#onetrust-pc-sdk .ot-sdk-container:after,#onetrust-pc-sdk .ot-sdk-row:after,#ot-sdk-cookie-policy .ot-sdk-container:after,#ot-sdk-cookie-policy .ot-sdk-row:after{content:"";display:table;clear:both}#onetrust-banner-sdk .ot-sdk-row,#onetrust-pc-sdk .ot-sdk-row,#ot-sdk-cookie-policy .ot-sdk-row{margin:0;max-width:none;display:block}
#onetrust-banner-sdk{box-shadow:0 0 18px rgba(0,0,0,.2)}#onetrust-banner-sdk.otFlat{position:fixed;z-index:2147483645;bottom:0;right:0;left:0;background-color:#fff;max-height:90%;overflow-x:hidden;overflow-y:auto}#onetrust-banner-sdk.otFlat.top{top:0px;bottom:auto}#onetrust-banner-sdk.otRelFont{font-size:1rem}#onetrust-banner-sdk>.ot-sdk-container{overflow:hidden}#onetrust-banner-sdk::-webkit-scrollbar{width:11px}#onetrust-banner-sdk::-webkit-scrollbar-thumb{border-radius:10px;background:#c1c1c1}#onetrust-banner-sdk{scrollbar-arrow-color:#c1c1c1;scrollbar-darkshadow-color:#c1c1c1;scrollbar-face-color:#c1c1c1;scrollbar-shadow-color:#c1c1c1}#onetrust-banner-sdk #onetrust-policy{margin:1.25em 0 .625em 2em;overflow:hidden}#onetrust-banner-sdk #onetrust-policy .ot-gv-list-handler{float:left;font-size:.82em;padding:0;margin-bottom:0;border:0;line-height:normal;height:auto;width:auto}#onetrust-banner-sdk #onetrust-policy-title{font-size:1.2em;line-height:1.3;margin-bottom:10px}#onetrust-banner-sdk #onetrust-policy-text{clear:both;text-align:left;font-size:.88em;line-height:1.4}#onetrust-banner-sdk #onetrust-policy-text *{font-size:inherit;line-height:inherit}#onetrust-banner-sdk #onetrust-policy-text a{font-weight:bold;margin-left:5px}#onetrust-banner-sdk #onetrust-policy-title,#onetrust-banner-sdk #onetrust-policy-text{color:dimgray;float:left}#onetrust-banner-sdk #onetrust-button-group-parent{min-height:1px;text-align:center}#onetrust-banner-sdk #onetrust-button-group{display:inline-block}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{background-color:#68b631;color:#fff;border-color:#68b631;margin-right:1em;min-width:125px;height:auto;white-space:normal;word-break:break-word;word-wrap:break-word;padding:12px 10px;line-height:1.2;font-size:.813em;font-weight:600}#onetrust-banner-sdk #onetrust-pc-btn-handler.cookie-setting-link{background-color:#fff;border:none;color:#68b631;text-decoration:underline;padding-left:0;padding-right:0}#onetrust-banner-sdk .onetrust-close-btn-ui{width:44px;height:44px;background-size:12px;border:none;position:relative;margin:auto;padding:0}#onetrust-banner-sdk .banner_logo{display:none}#onetrust-banner-sdk.ot-bnr-w-logo .ot-bnr-logo{position:absolute;top:50%;transform:translateY(-50%);left:0px}#onetrust-banner-sdk.ot-bnr-w-logo #onetrust-policy{margin-left:65px}#onetrust-banner-sdk .ot-b-addl-desc{clear:both;float:left;display:block}#onetrust-banner-sdk #banner-options{float:left;display:table;margin-right:0;margin-left:1em;width:calc(100% - 1em)}#onetrust-banner-sdk .banner-option-input{cursor:pointer;width:auto;height:auto;border:none;padding:0;padding-right:3px;margin:0 0 10px;font-size:.82em;line-height:1.4}#onetrust-banner-sdk .banner-option-input *{pointer-events:none;font-size:inherit;line-height:inherit}#onetrust-banner-sdk .banner-option-input[aria-expanded=true]~.banner-option-details{display:block;height:auto}#onetrust-banner-sdk .banner-option-input[aria-expanded=true] .ot-arrow-container{transform:rotate(90deg)}#onetrust-banner-sdk .banner-option{margin-bottom:12px;margin-left:0;border:none;float:left;padding:0}#onetrust-banner-sdk .banner-option:first-child{padding-left:2px}#onetrust-banner-sdk .banner-option:not(:first-child){padding:0;border:none}#onetrust-banner-sdk .banner-option-header{cursor:pointer;display:inline-block}#onetrust-banner-sdk .banner-option-header :first-child{color:dimgray;font-weight:bold;float:left}#onetrust-banner-sdk .banner-option-header .ot-arrow-container{display:inline-block;border-top:6px solid transparent;border-bottom:6px solid transparent;border-left:6px solid dimgray;margin-left:10px;vertical-align:middle}#onetrust-banner-sdk .banner-option-details{display:none;font-size:.83em;line-height:1.5;padding:10px 0px 5px 10px;margin-right:10px;height:0px}#onetrust-banner-sdk .banner-option-details *{font-size:inherit;line-height:inherit;color:dimgray}#onetrust-banner-sdk .ot-arrow-container,#onetrust-banner-sdk .banner-option-details{transition:all 300ms ease-in 0s;-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s}#onetrust-banner-sdk .ot-dpd-container{float:left}#onetrust-banner-sdk .ot-dpd-title{margin-bottom:10px}#onetrust-banner-sdk .ot-dpd-title,#onetrust-banner-sdk .ot-dpd-desc{font-size:.88em;line-height:1.4;color:dimgray}#onetrust-banner-sdk .ot-dpd-title *,#onetrust-banner-sdk .ot-dpd-desc *{font-size:inherit;line-height:inherit}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text *{margin-bottom:0}#onetrust-banner-sdk.ot-iab-2 .onetrust-vendors-list-handler{display:block;margin-left:0;margin-top:5px;clear:both;margin-bottom:0;padding:0;border:0;height:auto;width:auto}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group button{display:block}#onetrust-banner-sdk.ot-close-btn-link{padding-top:25px}#onetrust-banner-sdk.ot-close-btn-link #onetrust-close-btn-container{top:15px;transform:none;right:15px}#onetrust-banner-sdk.ot-close-btn-link #onetrust-close-btn-container button{padding:0;white-space:pre-wrap;border:none;height:auto;line-height:1.5;text-decoration:underline;font-size:.69em}#onetrust-banner-sdk #onetrust-policy-text,#onetrust-banner-sdk .ot-dpd-desc,#onetrust-banner-sdk .ot-b-addl-desc{font-size:.813em;line-height:1.5}#onetrust-banner-sdk .ot-dpd-desc{margin-bottom:10px}#onetrust-banner-sdk .ot-dpd-desc>.ot-b-addl-desc{margin-top:10px;margin-bottom:10px;font-size:1em}@media only screen and (max-width: 425px){#onetrust-banner-sdk #onetrust-close-btn-container{position:absolute;top:6px;right:2px}#onetrust-banner-sdk #onetrust-policy{margin-left:0;margin-top:3em}#onetrust-banner-sdk #onetrust-button-group{display:block}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{width:100%}#onetrust-banner-sdk .onetrust-close-btn-ui{top:auto;transform:none}#onetrust-banner-sdk #onetrust-policy-title{display:inline;float:none}#onetrust-banner-sdk #banner-options{margin:0;padding:0;width:100%}}@media only screen and (min-width: 426px)and (max-width: 896px){#onetrust-banner-sdk #onetrust-close-btn-container{position:absolute;top:0;right:0}#onetrust-banner-sdk #onetrust-policy{margin-left:1em;margin-right:1em}#onetrust-banner-sdk .onetrust-close-btn-ui{top:10px;right:10px}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:95%}#onetrust-banner-sdk.ot-iab-2 #onetrust-group-container{width:100%}#onetrust-banner-sdk.ot-bnr-w-logo #onetrust-button-group-parent{padding-left:50px}#onetrust-banner-sdk #onetrust-button-group-parent{width:100%;position:relative;margin-left:0}#onetrust-banner-sdk #onetrust-button-group button{display:inline-block}#onetrust-banner-sdk #onetrust-button-group{margin-right:0;text-align:center}#onetrust-banner-sdk .has-reject-all-button #onetrust-pc-btn-handler{float:left}#onetrust-banner-sdk .has-reject-all-button #onetrust-reject-all-handler,#onetrust-banner-sdk .has-reject-all-button #onetrust-accept-btn-handler{float:right}#onetrust-banner-sdk .has-reject-all-button #onetrust-button-group{width:calc(100% - 2em);margin-right:0}#onetrust-banner-sdk .has-reject-all-button #onetrust-pc-btn-handler.cookie-setting-link{padding-left:0px;text-align:left}#onetrust-banner-sdk.ot-buttons-fw .ot-sdk-three button{width:100%;text-align:center}#onetrust-banner-sdk.ot-buttons-fw #onetrust-button-group-parent button{float:none}#onetrust-banner-sdk.ot-buttons-fw #onetrust-pc-btn-handler.cookie-setting-link{text-align:center}}@media only screen and (min-width: 550px){#onetrust-banner-sdk .banner-option:not(:first-child){border-left:1px solid #d8d8d8;padding-left:25px}}@media only screen and (min-width: 425px)and (max-width: 550px){#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group,#onetrust-banner-sdk.ot-iab-2 #onetrust-policy,#onetrust-banner-sdk.ot-iab-2 .banner-option{width:100%}}@media only screen and (min-width: 769px){#onetrust-banner-sdk #onetrust-button-group{margin-right:30%}#onetrust-banner-sdk #banner-options{margin-left:2em;margin-right:5em;margin-bottom:1.25em;width:calc(100% - 7em)}}@media only screen and (min-width: 897px)and (max-width: 1023px){#onetrust-banner-sdk.vertical-align-content #onetrust-button-group-parent{position:absolute;top:50%;left:75%;transform:translateY(-50%)}#onetrust-banner-sdk #onetrust-close-btn-container{top:50%;margin:auto;transform:translate(-50%, -50%);position:absolute;padding:0;right:0}#onetrust-banner-sdk #onetrust-close-btn-container button{position:relative;margin:0;right:-22px;top:2px}}@media only screen and (min-width: 1024px){#onetrust-banner-sdk #onetrust-close-btn-container{top:50%;margin:auto;transform:translate(-50%, -50%);position:absolute;right:0}#onetrust-banner-sdk #onetrust-close-btn-container button{right:-12px}#onetrust-banner-sdk #onetrust-policy{margin-left:2em}#onetrust-banner-sdk.vertical-align-content #onetrust-button-group-parent{position:absolute;top:50%;left:60%;transform:translateY(-50%)}#onetrust-banner-sdk .ot-optout-signal{width:50%}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-title{width:50%}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text,#onetrust-banner-sdk.ot-iab-2 :not(.ot-dpd-desc)>.ot-b-addl-desc{margin-bottom:1em;width:50%;border-right:1px solid #d8d8d8;padding-right:1rem}#onetrust-banner-sdk.ot-iab-2 #onetrust-policy-text{margin-bottom:0;padding-bottom:1em}#onetrust-banner-sdk.ot-iab-2 :not(.ot-dpd-desc)>.ot-b-addl-desc{margin-bottom:0;padding-bottom:1em}#onetrust-banner-sdk.ot-iab-2 .ot-dpd-container{width:45%;padding-left:1rem;display:inline-block;float:none}#onetrust-banner-sdk.ot-iab-2 .ot-dpd-title{line-height:1.7}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group-parent{left:auto;right:4%;margin-left:0}#onetrust-banner-sdk.ot-iab-2 #onetrust-button-group button{display:block}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-button-group-parent{margin:auto;width:30%}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:60%}#onetrust-banner-sdk #onetrust-button-group{margin-right:auto}#onetrust-banner-sdk #onetrust-accept-btn-handler,#onetrust-banner-sdk #onetrust-reject-all-handler,#onetrust-banner-sdk #onetrust-pc-btn-handler{margin-top:1em}}@media only screen and (min-width: 890px){#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group-parent{padding-left:3%;padding-right:4%;margin-left:0}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group{margin-right:0;margin-top:1.25em;width:100%}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group button{width:100%;margin-bottom:5px;margin-top:5px}#onetrust-banner-sdk.ot-buttons-fw:not(.ot-iab-2) #onetrust-button-group button:last-of-type{margin-bottom:20px}}@media only screen and (min-width: 1280px){#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-group-container{width:55%}#onetrust-banner-sdk:not(.ot-iab-2) #onetrust-button-group-parent{width:44%;padding-left:2%;padding-right:2%}#onetrust-banner-sdk:not(.ot-iab-2).vertical-align-content #onetrust-button-group-parent{position:absolute;left:55%}}
        #onetrust-consent-sdk #onetrust-banner-sdk {background-color: #666666;}
            #onetrust-consent-sdk #onetrust-policy-title,
                    #onetrust-consent-sdk #onetrust-policy-text,
                    #onetrust-consent-sdk .ot-b-addl-desc,
                    #onetrust-consent-sdk .ot-dpd-desc,
                    #onetrust-consent-sdk .ot-dpd-title,
                    #onetrust-consent-sdk #onetrust-policy-text *:not(.onetrust-vendors-list-handler),
                    #onetrust-consent-sdk .ot-dpd-desc *:not(.onetrust-vendors-list-handler),
                    #onetrust-consent-sdk #onetrust-banner-sdk #banner-options *,
                    #onetrust-banner-sdk .ot-cat-header,
                    #onetrust-banner-sdk .ot-optout-signal
                    {
                        color: #ffffff;
                    }
            #onetrust-consent-sdk #onetrust-banner-sdk .banner-option-details {
                    background-color: #666666;}
             #onetrust-consent-sdk #onetrust-banner-sdk a[href],
                    #onetrust-consent-sdk #onetrust-banner-sdk a[href] font,
                    #onetrust-consent-sdk #onetrust-banner-sdk .ot-link-btn
                        {
                            color: #ffffff;
                        }#onetrust-consent-sdk #onetrust-accept-btn-handler,
                         #onetrust-banner-sdk #onetrust-reject-all-handler {
                            background-color: #b70014;border-color: #b70014;
                color: #ffffff;
            }
            #onetrust-consent-sdk #onetrust-banner-sdk *:focus,
            #onetrust-consent-sdk #onetrust-banner-sdk:focus {
               outline-color: #777777;
               outline-width: 1px;
            }
            #onetrust-consent-sdk #onetrust-pc-btn-handler,
            #onetrust-consent-sdk #onetrust-pc-btn-handler.cookie-setting-link {
                color: #ffffff; border-color: #ffffff;
                background-color:
                #666666;
            }#onetrust-consent-sdk #onetrust-banner-sdk { background-color: rgba(0,0,0,0.6);}#onetrust-pc-sdk.otPcCenter{overflow:hidden;position:fixed;margin:0 auto;top:5%;right:0;left:0;width:40%;max-width:575px;min-width:575px;border-radius:2.5px;z-index:2147483647;background-color:#fff;-webkit-box-shadow:0px 2px 10px -3px #999;-moz-box-shadow:0px 2px 10px -3px #999;box-shadow:0px 2px 10px -3px #999}#onetrust-pc-sdk.otPcCenter[dir=rtl]{right:0;left:0}#onetrust-pc-sdk.otRelFont{font-size:1rem}#onetrust-pc-sdk .ot-optout-signal{margin-top:.625rem}#onetrust-pc-sdk #ot-addtl-venlst .ot-arw-cntr,#onetrust-pc-sdk #ot-addtl-venlst .ot-plus-minus,#onetrust-pc-sdk .ot-hide-tgl{visibility:hidden}#onetrust-pc-sdk #ot-addtl-venlst .ot-arw-cntr *,#onetrust-pc-sdk #ot-addtl-venlst .ot-plus-minus *,#onetrust-pc-sdk .ot-hide-tgl *{visibility:hidden}#onetrust-pc-sdk #ot-gn-venlst .ot-ven-item .ot-acc-hdr{min-height:40px}#onetrust-pc-sdk .ot-pc-header{height:39px;padding:10px 0 10px 30px;border-bottom:1px solid #e9e9e9}#onetrust-pc-sdk #ot-pc-title,#onetrust-pc-sdk #ot-category-title,#onetrust-pc-sdk .ot-cat-header,#onetrust-pc-sdk #ot-lst-title,#onetrust-pc-sdk .ot-ven-hdr .ot-ven-name,#onetrust-pc-sdk .ot-always-active{font-weight:bold;color:dimgray}#onetrust-pc-sdk .ot-always-active-group .ot-cat-header{width:55%;font-weight:700}#onetrust-pc-sdk .ot-cat-item p{clear:both;float:left;margin-top:10px;margin-bottom:5px;line-height:1.5;font-size:.812em;color:dimgray}#onetrust-pc-sdk .ot-close-icon{height:44px;width:44px;background-size:10px}#onetrust-pc-sdk #ot-pc-title{float:left;font-size:1em;line-height:1.5;margin-bottom:10px;margin-top:10px;width:100%}#onetrust-pc-sdk #accept-recommended-btn-handler{margin-right:10px;margin-bottom:25px;outline-offset:-1px}#onetrust-pc-sdk #ot-pc-desc{clear:both;width:100%;font-size:.812em;line-height:1.5;margin-bottom:25px}#onetrust-pc-sdk #ot-pc-desc a{margin-left:5px}#onetrust-pc-sdk #ot-pc-desc *{font-size:inherit;line-height:inherit}#onetrust-pc-sdk #ot-pc-desc ul li{padding:10px 0px}#onetrust-pc-sdk a{color:#656565;cursor:pointer}#onetrust-pc-sdk a:hover{color:#3860be}#onetrust-pc-sdk label{margin-bottom:0}#onetrust-pc-sdk #vdr-lst-dsc{font-size:.812em;line-height:1.5;padding:10px 15px 5px 15px}#onetrust-pc-sdk button{max-width:394px;padding:12px 30px;line-height:1;word-break:break-word;word-wrap:break-word;white-space:normal;font-weight:bold;height:auto}#onetrust-pc-sdk .ot-link-btn{padding:0;margin-bottom:0;border:0;font-weight:normal;line-height:normal;width:auto;height:auto}#onetrust-pc-sdk #ot-pc-content{position:absolute;overflow-y:scroll;padding-left:0px;padding-right:30px;top:60px;bottom:110px;margin:1px 3px 0 30px;width:calc(100% - 63px)}#onetrust-pc-sdk .ot-vs-list .ot-always-active,#onetrust-pc-sdk .ot-cat-grp .ot-always-active{float:right;clear:none;color:#3860be;margin:0;font-size:.813em;line-height:1.3}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar-track{margin-right:20px}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar{width:11px}#onetrust-pc-sdk .ot-pc-scrollbar::-webkit-scrollbar-thumb{border-radius:10px;background:#d8d8d8}#onetrust-pc-sdk input[type=checkbox]:focus+.ot-acc-hdr{outline:#000 1px solid}#onetrust-pc-sdk .ot-pc-scrollbar{scrollbar-arrow-color:#d8d8d8;scrollbar-darkshadow-color:#d8d8d8;scrollbar-face-color:#d8d8d8;scrollbar-shadow-color:#d8d8d8}#onetrust-pc-sdk .save-preference-btn-handler{margin-right:20px}#onetrust-pc-sdk .ot-pc-refuse-all-handler{margin-right:10px}#onetrust-pc-sdk #ot-pc-desc .privacy-notice-link{margin-left:0;margin-right:8px}#onetrust-pc-sdk #ot-pc-desc .ot-imprint-handler{margin-left:0;margin-right:8px}#onetrust-pc-sdk .ot-subgrp-cntr{display:inline-block;clear:both;width:100%;padding-top:15px}#onetrust-pc-sdk .ot-switch+.ot-subgrp-cntr{padding-top:10px}#onetrust-pc-sdk ul.ot-subgrps{margin:0;font-size:initial}#onetrust-pc-sdk ul.ot-subgrps li p,#onetrust-pc-sdk ul.ot-subgrps li h5{font-size:.813em;line-height:1.4;color:dimgray}#onetrust-pc-sdk ul.ot-subgrps .ot-switch{min-height:auto}#onetrust-pc-sdk ul.ot-subgrps .ot-switch-nob{top:0}#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr{display:inline-block;width:100%}#onetrust-pc-sdk ul.ot-subgrps .ot-acc-txt{margin:0}#onetrust-pc-sdk ul.ot-subgrps li{padding:0;border:none}#onetrust-pc-sdk ul.ot-subgrps li h5{position:relative;top:5px;font-weight:bold;margin-bottom:0;float:left}#onetrust-pc-sdk li.ot-subgrp{margin-left:20px;overflow:auto}#onetrust-pc-sdk li.ot-subgrp>h5{width:calc(100% - 100px)}#onetrust-pc-sdk .ot-cat-item p>ul,#onetrust-pc-sdk li.ot-subgrp p>ul{margin:0px;list-style:disc;margin-left:15px;font-size:inherit}#onetrust-pc-sdk .ot-cat-item p>ul li,#onetrust-pc-sdk li.ot-subgrp p>ul li{font-size:inherit;padding-top:10px;padding-left:0px;padding-right:0px;border:none}#onetrust-pc-sdk .ot-cat-item p>ul li:last-child,#onetrust-pc-sdk li.ot-subgrp p>ul li:last-child{padding-bottom:10px}#onetrust-pc-sdk .ot-pc-logo{height:40px;width:120px}#onetrust-pc-sdk .ot-pc-footer{position:absolute;bottom:0px;width:100%;max-height:160px;border-top:1px solid #d8d8d8}#onetrust-pc-sdk.ot-ftr-stacked .ot-pc-refuse-all-handler{margin-bottom:0px}#onetrust-pc-sdk.ot-ftr-stacked #ot-pc-content{bottom:160px}#onetrust-pc-sdk.ot-ftr-stacked .ot-pc-footer button{width:100%;max-width:none}#onetrust-pc-sdk.ot-ftr-stacked .ot-btn-container{margin:0 30px;width:calc(100% - 60px);padding-right:0}#onetrust-pc-sdk .ot-pc-footer-logo{height:30px;width:100%;text-align:right;background:#f4f4f4}#onetrust-pc-sdk .ot-pc-footer-logo a{display:inline-block;margin-top:5px;margin-right:10px}#onetrust-pc-sdk[dir=rtl] .ot-pc-footer-logo{direction:rtl}#onetrust-pc-sdk[dir=rtl] .ot-pc-footer-logo a{margin-right:25px}#onetrust-pc-sdk .ot-tgl{float:right;position:relative;z-index:1}#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob{background-color:#cddcf2;border:1px solid #3860be}#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob:before{-webkit-transform:translateX(20px);-ms-transform:translateX(20px);transform:translateX(20px);background-color:#3860be;border-color:#3860be}#onetrust-pc-sdk .ot-tgl input:focus+.ot-switch{outline:#000 solid 1px}#onetrust-pc-sdk .ot-switch{position:relative;display:inline-block;width:45px;height:25px}#onetrust-pc-sdk .ot-switch-nob{position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:#f2f1f1;border:1px solid #ddd;transition:all .2s ease-in 0s;-moz-transition:all .2s ease-in 0s;-o-transition:all .2s ease-in 0s;-webkit-transition:all .2s ease-in 0s;border-radius:20px}#onetrust-pc-sdk .ot-switch-nob:before{position:absolute;content:"";height:21px;width:21px;bottom:1px;background-color:#7d7d7d;-webkit-transition:.4s;transition:.4s;border-radius:20px}#onetrust-pc-sdk .ot-chkbox input:checked~label::before{background-color:#3860be}#onetrust-pc-sdk .ot-chkbox input+label::after{content:none;color:#fff}#onetrust-pc-sdk .ot-chkbox input:checked+label::after{content:""}#onetrust-pc-sdk .ot-chkbox input:focus+label::before{outline-style:solid;outline-width:2px;outline-style:auto}#onetrust-pc-sdk .ot-chkbox label{position:relative;display:inline-block;padding-left:30px;cursor:pointer;font-weight:500}#onetrust-pc-sdk .ot-chkbox label::before,#onetrust-pc-sdk .ot-chkbox label::after{position:absolute;content:"";display:inline-block;border-radius:3px}#onetrust-pc-sdk .ot-chkbox label::before{height:18px;width:18px;border:1px solid #3860be;left:0px;top:auto}#onetrust-pc-sdk .ot-chkbox label::after{height:5px;width:9px;border-left:3px solid;border-bottom:3px solid;transform:rotate(-45deg);-o-transform:rotate(-45deg);-ms-transform:rotate(-45deg);-webkit-transform:rotate(-45deg);left:4px;top:5px}#onetrust-pc-sdk .ot-label-txt{display:none}#onetrust-pc-sdk .ot-chkbox input,#onetrust-pc-sdk .ot-tgl input{position:absolute;opacity:0;width:0;height:0}#onetrust-pc-sdk .ot-arw-cntr{float:right;position:relative;pointer-events:none}#onetrust-pc-sdk .ot-arw-cntr .ot-arw{width:16px;height:16px;margin-left:5px;color:dimgray;display:inline-block;vertical-align:middle;-webkit-transition:all 150ms ease-in 0s;-moz-transition:all 150ms ease-in 0s;-o-transition:all 150ms ease-in 0s;transition:all 150ms ease-in 0s}#onetrust-pc-sdk input:checked~.ot-acc-hdr .ot-arw,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-arw-cntr svg{transform:rotate(90deg);-o-transform:rotate(90deg);-ms-transform:rotate(90deg);-webkit-transform:rotate(90deg)}#onetrust-pc-sdk input[type=checkbox]:focus+.ot-acc-hdr{outline:#000 1px solid}#onetrust-pc-sdk .ot-tgl-cntr,#onetrust-pc-sdk .ot-arw-cntr{display:inline-block}#onetrust-pc-sdk .ot-tgl-cntr{width:45px;float:right;margin-top:2px}#onetrust-pc-sdk #ot-lst-cnt .ot-tgl-cntr{margin-top:10px}#onetrust-pc-sdk .ot-always-active-subgroup{width:auto;padding-left:0px !important;top:3px;position:relative}#onetrust-pc-sdk .ot-label-status{padding-left:5px;font-size:.75em;display:none}#onetrust-pc-sdk .ot-arw-cntr{margin-top:-1px}#onetrust-pc-sdk .ot-arw-cntr svg{-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s;transition:all 300ms ease-in 0s;height:10px;width:10px}#onetrust-pc-sdk input:checked~.ot-acc-hdr .ot-arw{transform:rotate(90deg);-o-transform:rotate(90deg);-ms-transform:rotate(90deg);-webkit-transform:rotate(90deg)}#onetrust-pc-sdk .ot-arw{width:10px;margin-left:15px;transition:all 300ms ease-in 0s;-webkit-transition:all 300ms ease-in 0s;-moz-transition:all 300ms ease-in 0s;-o-transition:all 300ms ease-in 0s}#onetrust-pc-sdk .ot-vlst-cntr{margin-bottom:0}#onetrust-pc-sdk .ot-hlst-cntr{margin-top:5px;display:inline-block;width:100%}#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a,#onetrust-pc-sdk .category-host-list-handler{clear:both;color:#3860be;margin-left:0;font-size:.813em;text-decoration:none;float:left;overflow:hidden}#onetrust-pc-sdk .category-vendors-list-handler:hover,#onetrust-pc-sdk .category-vendors-list-handler+a:hover,#onetrust-pc-sdk .category-host-list-handler:hover{text-decoration-line:underline}#onetrust-pc-sdk .category-vendors-list-handler+a{clear:none}#onetrust-pc-sdk .ot-vlst-cntr .ot-ext-lnk{display:inline-block;height:13px;width:13px;background-repeat:no-repeat;margin-left:1px;margin-top:6px;cursor:pointer}#onetrust-pc-sdk .back-btn-handler{font-size:1em;text-decoration:none}#onetrust-pc-sdk .back-btn-handler:hover{opacity:.6}#onetrust-pc-sdk #ot-lst-title h3{display:inline-block;word-break:break-word;word-wrap:break-word;margin-bottom:0;color:#656565;font-size:1em;font-weight:bold;margin-left:15px}#onetrust-pc-sdk #ot-lst-title{margin:10px 0 10px 0px;font-size:1em;text-align:left}#onetrust-pc-sdk #ot-pc-hdr{margin:0 0 0 30px;height:auto;width:auto}#onetrust-pc-sdk #ot-pc-hdr input::placeholder{color:#d4d4d4;font-style:italic}#onetrust-pc-sdk #vendor-search-handler{height:31px;width:100%;border-radius:50px;font-size:.8em;padding-right:35px;padding-left:15px;float:left;margin-left:15px}#onetrust-pc-sdk .ot-ven-name{display:block;width:auto;padding-right:5px}#onetrust-pc-sdk #ot-lst-cnt{overflow-y:auto;margin-left:20px;margin-right:7px;width:calc(100% - 27px);max-height:calc(100% - 80px);height:100%;transform:translate3d(0, 0, 0)}#onetrust-pc-sdk #ot-pc-lst{width:100%;bottom:100px;position:absolute;top:60px}#onetrust-pc-sdk #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr .ot-arw-cntr,#onetrust-pc-sdk #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr .ot-arw-cntr *{visibility:hidden}#onetrust-pc-sdk #ot-pc-lst .ot-tgl-cntr{right:12px;position:absolute}#onetrust-pc-sdk #ot-pc-lst .ot-arw-cntr{float:right;position:relative}#onetrust-pc-sdk #ot-pc-lst .ot-arw{margin-left:10px}#onetrust-pc-sdk #ot-pc-lst .ot-acc-hdr{overflow:hidden;cursor:pointer}#onetrust-pc-sdk .ot-vlst-cntr{overflow:hidden}#onetrust-pc-sdk #ot-sel-blk{overflow:hidden;width:100%;position:sticky;position:-webkit-sticky;top:0;z-index:3}#onetrust-pc-sdk #ot-back-arw{height:12px;width:12px}#onetrust-pc-sdk .ot-lst-subhdr{width:100%;display:inline-block}#onetrust-pc-sdk .ot-search-cntr{float:left;width:78%;position:relative}#onetrust-pc-sdk .ot-search-cntr>svg{width:30px;height:30px;position:absolute;float:left;right:-15px}#onetrust-pc-sdk .ot-fltr-cntr{float:right;right:50px;position:relative}#onetrust-pc-sdk #filter-btn-handler{background-color:#3860be;border-radius:17px;display:inline-block;position:relative;width:32px;height:32px;-moz-transition:.1s ease;-o-transition:.1s ease;-webkit-transition:1s ease;transition:.1s ease;padding:0;margin:0}#onetrust-pc-sdk #filter-btn-handler:hover{background-color:#3860be}#onetrust-pc-sdk #filter-btn-handler svg{width:12px;height:12px;margin:3px 10px 0 10px;display:block;position:static;right:auto;top:auto}#onetrust-pc-sdk .ot-ven-link{color:#3860be;text-decoration:none;font-weight:100;display:inline-block;padding-top:10px;transform:translate(0, 1%);-o-transform:translate(0, 1%);-ms-transform:translate(0, 1%);-webkit-transform:translate(0, 1%);position:relative;z-index:2}#onetrust-pc-sdk .ot-ven-link *{font-size:inherit}#onetrust-pc-sdk .ot-ven-link:hover{text-decoration:underline}#onetrust-pc-sdk .ot-ven-hdr{width:calc(100% - 160px);height:auto;float:left;word-break:break-word;word-wrap:break-word;vertical-align:middle;padding-bottom:3px}#onetrust-pc-sdk .ot-ven-link{letter-spacing:.03em;font-size:.75em;font-weight:400}#onetrust-pc-sdk .ot-ven-dets{border-radius:2px;background-color:#f8f8f8}#onetrust-pc-sdk .ot-ven-dets li:first-child p:first-child{border-top:none}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:not(:first-child){border-top:1px solid #ddd !important}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p{display:inline-block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p:nth-of-type(odd){width:30%}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc:nth-child(n+3) p:nth-of-type(even){width:50%;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p,#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc h4{padding-top:5px;padding-bottom:5px;display:block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc h4{display:inline-block}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p:nth-last-child(-n+1){padding-bottom:10px}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc p:nth-child(-n+2):not(.disc-pur){padding-top:10px}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur-cont{display:inline}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur{position:relative;width:50% !important;word-break:break-word;word-wrap:break-word;left:calc(30% + 17px)}#onetrust-pc-sdk .ot-ven-dets .ot-ven-disc .disc-pur:nth-child(-n+1){position:static}#onetrust-pc-sdk .ot-ven-dets p,#onetrust-pc-sdk .ot-ven-dets h4,#onetrust-pc-sdk .ot-ven-dets span{font-size:.69em;text-align:left;vertical-align:middle;word-break:break-word;word-wrap:break-word;margin:0;padding-bottom:10px;padding-left:15px;color:#2e3644}#onetrust-pc-sdk .ot-ven-dets h4{padding-top:5px}#onetrust-pc-sdk .ot-ven-dets span{color:dimgray;padding:0;vertical-align:baseline}#onetrust-pc-sdk .ot-ven-dets .ot-ven-pur h4{border-top:1px solid #e9e9e9;border-bottom:1px solid #e9e9e9;padding-bottom:5px;margin-bottom:5px;font-weight:bold}#onetrust-pc-sdk #ot-host-lst .ot-sel-all{float:right;position:relative;margin-right:42px;top:10px}#onetrust-pc-sdk #ot-host-lst .ot-sel-all input[type=checkbox]{width:auto;height:auto}#onetrust-pc-sdk #ot-host-lst .ot-sel-all label{height:20px;width:20px;padding-left:0px}#onetrust-pc-sdk #ot-host-lst .ot-acc-txt{overflow:hidden;width:95%}#onetrust-pc-sdk .ot-host-hdr{position:relative;z-index:1;pointer-events:none;width:calc(100% - 125px);float:left}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-desc{display:inline-block;width:90%}#onetrust-pc-sdk .ot-host-name{pointer-events:none}#onetrust-pc-sdk .ot-host-hdr>a{text-decoration:underline;font-size:.82em;position:relative;z-index:2;float:left;margin-bottom:5px;pointer-events:initial}#onetrust-pc-sdk .ot-host-name+a{margin-top:5px}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-name a,#onetrust-pc-sdk .ot-host-desc,#onetrust-pc-sdk .ot-host-info{color:dimgray;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-host-name,#onetrust-pc-sdk .ot-host-name a{font-weight:bold;font-size:.82em;line-height:1.3}#onetrust-pc-sdk .ot-host-name a{font-size:1em}#onetrust-pc-sdk .ot-host-expand{margin-top:3px;margin-bottom:3px;clear:both;display:block;color:#3860be;font-size:.72em;font-weight:normal}#onetrust-pc-sdk .ot-host-expand *{font-size:inherit}#onetrust-pc-sdk .ot-host-desc,#onetrust-pc-sdk .ot-host-info{font-size:.688em;line-height:1.4;font-weight:normal}#onetrust-pc-sdk .ot-host-desc{margin-top:10px}#onetrust-pc-sdk .ot-host-opt{margin:0;font-size:inherit;display:inline-block;width:100%}#onetrust-pc-sdk .ot-host-opt li>div div{font-size:.8em;padding:5px 0}#onetrust-pc-sdk .ot-host-opt li>div div:nth-child(1){width:30%;float:left}#onetrust-pc-sdk .ot-host-opt li>div div:nth-child(2){width:70%;float:left;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-host-info{border:none;display:inline-block;width:calc(100% - 10px);padding:10px;margin-bottom:10px;background-color:#f8f8f8}#onetrust-pc-sdk .ot-host-info>div{overflow:auto}#onetrust-pc-sdk #no-results{text-align:center;margin-top:30px}#onetrust-pc-sdk #no-results p{font-size:1em;color:#2e3644;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk #no-results p span{font-weight:bold}#onetrust-pc-sdk #ot-fltr-modal{width:100%;height:auto;display:none;-moz-transition:.2s ease;-o-transition:.2s ease;-webkit-transition:2s ease;transition:.2s ease;overflow:hidden;opacity:1;right:0}#onetrust-pc-sdk #ot-fltr-modal .ot-label-txt{display:inline-block;font-size:.85em;color:dimgray}#onetrust-pc-sdk #ot-fltr-cnt{z-index:2147483646;background-color:#fff;position:absolute;height:90%;max-height:300px;width:325px;left:210px;margin-top:10px;margin-bottom:20px;padding-right:10px;border-radius:3px;-webkit-box-shadow:0px 0px 12px 2px #c7c5c7;-moz-box-shadow:0px 0px 12px 2px #c7c5c7;box-shadow:0px 0px 12px 2px #c7c5c7}#onetrust-pc-sdk .ot-fltr-scrlcnt{overflow-y:auto;overflow-x:hidden;clear:both;max-height:calc(100% - 60px)}#onetrust-pc-sdk #ot-anchor{border:12px solid transparent;display:none;position:absolute;z-index:2147483647;right:55px;top:75px;transform:rotate(45deg);-o-transform:rotate(45deg);-ms-transform:rotate(45deg);-webkit-transform:rotate(45deg);background-color:#fff;-webkit-box-shadow:-3px -3px 5px -2px #c7c5c7;-moz-box-shadow:-3px -3px 5px -2px #c7c5c7;box-shadow:-3px -3px 5px -2px #c7c5c7}#onetrust-pc-sdk .ot-fltr-btns{margin-left:15px}#onetrust-pc-sdk #filter-apply-handler{margin-right:15px}#onetrust-pc-sdk .ot-fltr-opt{margin-bottom:25px;margin-left:15px;width:75%;position:relative}#onetrust-pc-sdk .ot-fltr-opt p{display:inline-block;margin:0;font-size:.9em;color:#2e3644}#onetrust-pc-sdk .ot-chkbox label span{font-size:.85em;color:dimgray}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]+label::after{content:none;color:#fff}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]:checked+label::after{content:""}#onetrust-pc-sdk .ot-chkbox input[type=checkbox]:focus+label::before{outline-style:solid;outline-width:2px;outline-style:auto}#onetrust-pc-sdk #ot-selall-vencntr,#onetrust-pc-sdk #ot-selall-adtlvencntr,#onetrust-pc-sdk #ot-selall-hostcntr,#onetrust-pc-sdk #ot-selall-licntr,#onetrust-pc-sdk #ot-selall-gnvencntr{right:15px;position:relative;width:20px;height:20px;float:right}#onetrust-pc-sdk #ot-selall-vencntr label,#onetrust-pc-sdk #ot-selall-adtlvencntr label,#onetrust-pc-sdk #ot-selall-hostcntr label,#onetrust-pc-sdk #ot-selall-licntr label,#onetrust-pc-sdk #ot-selall-gnvencntr label{float:left;padding-left:0}#onetrust-pc-sdk #ot-ven-lst:first-child{border-top:1px solid #e2e2e2}#onetrust-pc-sdk ul{list-style:none;padding:0}#onetrust-pc-sdk ul li{position:relative;margin:0;padding:15px 15px 15px 10px;border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk ul li h3{font-size:.75em;color:#656565;margin:0;display:inline-block;width:70%;height:auto;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk ul li p{margin:0;font-size:.7em}#onetrust-pc-sdk ul li input[type=checkbox]{position:absolute;cursor:pointer;width:100%;height:100%;opacity:0;margin:0;top:0;left:0}#onetrust-pc-sdk .ot-cat-item>button:focus,#onetrust-pc-sdk .ot-acc-cntr>button:focus,#onetrust-pc-sdk li>button:focus{outline:#000 solid 2px}#onetrust-pc-sdk .ot-cat-item>button,#onetrust-pc-sdk .ot-acc-cntr>button,#onetrust-pc-sdk li>button{position:absolute;cursor:pointer;width:100%;height:100%;margin:0;top:0;left:0;z-index:1;max-width:none;border:none}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=false]~.ot-acc-txt,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=false]~.ot-acc-txt,#onetrust-pc-sdk li>button[aria-expanded=false]~.ot-acc-txt{margin-top:0;max-height:0;opacity:0;overflow:hidden;width:100%;transition:.25s ease-out;display:none}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=true]~.ot-acc-txt,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=true]~.ot-acc-txt,#onetrust-pc-sdk li>button[aria-expanded=true]~.ot-acc-txt{transition:.1s ease-in;margin-top:10px;width:100%;overflow:auto;display:block}#onetrust-pc-sdk .ot-cat-item>button[aria-expanded=true]~.ot-acc-grpcntr,#onetrust-pc-sdk .ot-acc-cntr>button[aria-expanded=true]~.ot-acc-grpcntr,#onetrust-pc-sdk li>button[aria-expanded=true]~.ot-acc-grpcntr{width:auto;margin-top:0px;padding-bottom:10px}#onetrust-pc-sdk .ot-host-item>button:focus,#onetrust-pc-sdk .ot-ven-item>button:focus{outline:0;border:2px solid #000}#onetrust-pc-sdk .ot-hide-acc>button{pointer-events:none}#onetrust-pc-sdk .ot-hide-acc .ot-plus-minus>*,#onetrust-pc-sdk .ot-hide-acc .ot-arw-cntr>*{visibility:hidden}#onetrust-pc-sdk .ot-hide-acc .ot-acc-hdr{min-height:30px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt){padding-right:10px;width:calc(100% - 37px);margin-top:10px;max-height:calc(100% - 90px)}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk{background-color:#f9f9fc;border:1px solid #e2e2e2;width:calc(100% - 2px);padding-bottom:5px;padding-top:5px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt{border:unset;background-color:unset}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all-hdr{display:none}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all{padding-right:.5rem}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) #ot-sel-blk.ot-vnd-list-cnt .ot-sel-all .ot-chkbox{right:0}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-sel-all{padding-right:34px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-sel-all-chkbox{width:auto}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) ul li{border:1px solid #e2e2e2;margin-bottom:10px}#onetrust-pc-sdk.ot-addtl-vendors #ot-lst-cnt:not(.ot-host-cnt) .ot-acc-cntr>.ot-acc-hdr{padding:10px 0 10px 15px}#onetrust-pc-sdk.ot-addtl-vendors .ot-sel-all-chkbox{float:right}#onetrust-pc-sdk.ot-addtl-vendors .ot-plus-minus~.ot-sel-all-chkbox{right:34px}#onetrust-pc-sdk.ot-addtl-vendors #ot-ven-lst:first-child{border-top:none}#onetrust-pc-sdk .ot-acc-cntr{position:relative;border-left:1px solid #e2e2e2;border-right:1px solid #e2e2e2;border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk .ot-acc-cntr input{z-index:1}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr{background-color:#f9f9fc;padding:5px 0 5px 15px;width:auto}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr .ot-plus-minus{vertical-align:middle;top:auto}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr .ot-arw-cntr{right:10px}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-hdr input{z-index:2}#onetrust-pc-sdk .ot-acc-cntr>input[type=checkbox]:checked~.ot-acc-hdr{border-bottom:1px solid #e2e2e2}#onetrust-pc-sdk .ot-acc-cntr>.ot-acc-txt{padding-left:10px;padding-right:10px}#onetrust-pc-sdk .ot-acc-cntr button[aria-expanded=true]~.ot-acc-txt{width:auto}#onetrust-pc-sdk .ot-acc-cntr .ot-addtl-venbox{display:none}#onetrust-pc-sdk .ot-vlst-cntr{margin-bottom:0;width:100%}#onetrust-pc-sdk .ot-vensec-title{font-size:.813em;vertical-align:middle;display:inline-block}#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a{margin-left:0;margin-top:10px}#onetrust-pc-sdk #ot-selall-vencntr.line-through label::after,#onetrust-pc-sdk #ot-selall-adtlvencntr.line-through label::after,#onetrust-pc-sdk #ot-selall-licntr.line-through label::after,#onetrust-pc-sdk #ot-selall-hostcntr.line-through label::after,#onetrust-pc-sdk #ot-selall-gnvencntr.line-through label::after{height:auto;border-left:0;transform:none;-o-transform:none;-ms-transform:none;-webkit-transform:none;left:5px;top:9px}#onetrust-pc-sdk #ot-category-title{float:left;padding-bottom:10px;font-size:1em;width:100%}#onetrust-pc-sdk .ot-cat-grp{margin-top:10px}#onetrust-pc-sdk .ot-cat-item{line-height:1.1;margin-top:10px;display:inline-block;width:100%}#onetrust-pc-sdk .ot-btn-container{text-align:right}#onetrust-pc-sdk .ot-btn-container button{display:inline-block;font-size:.75em;letter-spacing:.08em;margin-top:19px}#onetrust-pc-sdk #close-pc-btn-handler.ot-close-icon{position:absolute;top:10px;right:0;z-index:1;padding:0;background-color:transparent;border:none}#onetrust-pc-sdk #close-pc-btn-handler.ot-close-icon svg{display:block;height:10px;width:10px}#onetrust-pc-sdk #clear-filters-handler{margin-top:20px;margin-bottom:10px;float:right;max-width:200px;text-decoration:none;color:#3860be;font-size:.9em;font-weight:bold;background-color:transparent;border-color:transparent;padding:1px}#onetrust-pc-sdk #clear-filters-handler:hover{color:#2285f7}#onetrust-pc-sdk #clear-filters-handler:focus{outline:#000 solid 1px}#onetrust-pc-sdk .ot-enbl-chr h4~.ot-tgl,#onetrust-pc-sdk .ot-enbl-chr h4~.ot-always-active{right:45px}#onetrust-pc-sdk .ot-enbl-chr h4~.ot-tgl+.ot-tgl{right:120px}#onetrust-pc-sdk .ot-enbl-chr .ot-pli-hdr.ot-leg-border-color span:first-child{width:90px}#onetrust-pc-sdk .ot-enbl-chr li.ot-subgrp>h5+.ot-tgl-cntr{padding-right:25px}#onetrust-pc-sdk .ot-plus-minus{width:20px;height:20px;font-size:1.5em;position:relative;display:inline-block;margin-right:5px;top:3px}#onetrust-pc-sdk .ot-plus-minus span{position:absolute;background:#27455c;border-radius:1px}#onetrust-pc-sdk .ot-plus-minus span:first-of-type{top:25%;bottom:25%;width:10%;left:45%}#onetrust-pc-sdk .ot-plus-minus span:last-of-type{left:25%;right:25%;height:10%;top:45%}#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-arw,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:first-of-type,#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:last-of-type{transform:rotate(90deg)}#onetrust-pc-sdk button[aria-expanded=true]~.ot-acc-hdr .ot-plus-minus span:last-of-type{left:50%;right:50%}#onetrust-pc-sdk #ot-selall-vencntr label,#onetrust-pc-sdk #ot-selall-adtlvencntr label,#onetrust-pc-sdk #ot-selall-hostcntr label,#onetrust-pc-sdk #ot-selall-licntr label{position:relative;display:inline-block;width:20px;height:20px}#onetrust-pc-sdk .ot-host-item .ot-plus-minus,#onetrust-pc-sdk .ot-ven-item .ot-plus-minus{float:left;margin-right:8px;top:10px}#onetrust-pc-sdk .ot-ven-item ul{list-style:none inside;font-size:100%;margin:0}#onetrust-pc-sdk .ot-ven-item ul li{margin:0 !important;padding:0;border:none !important}#onetrust-pc-sdk .ot-pli-hdr{color:#77808e;overflow:hidden;padding-top:7.5px;padding-bottom:7.5px;width:calc(100% - 2px);border-top-left-radius:3px;border-top-right-radius:3px}#onetrust-pc-sdk .ot-pli-hdr span:first-child{top:50%;transform:translateY(50%);max-width:90px}#onetrust-pc-sdk .ot-pli-hdr span:last-child{padding-right:10px;max-width:95px;text-align:center}#onetrust-pc-sdk .ot-li-title{float:right;font-size:.813em}#onetrust-pc-sdk .ot-pli-hdr.ot-leg-border-color{background-color:#f4f4f4;border:1px solid #d8d8d8}#onetrust-pc-sdk .ot-pli-hdr.ot-leg-border-color span:first-child{text-align:left;width:70px}#onetrust-pc-sdk li.ot-subgrp>h5,#onetrust-pc-sdk .ot-cat-header{width:calc(100% - 130px)}#onetrust-pc-sdk li.ot-subgrp>h5+.ot-tgl-cntr{padding-left:13px}#onetrust-pc-sdk .ot-acc-grpcntr .ot-acc-grpdesc{margin-bottom:5px}#onetrust-pc-sdk .ot-acc-grpcntr .ot-subgrp-cntr{border-top:1px solid #d8d8d8}#onetrust-pc-sdk .ot-acc-grpcntr .ot-vlst-cntr+.ot-subgrp-cntr{border-top:none}#onetrust-pc-sdk .ot-acc-hdr .ot-arw-cntr+.ot-tgl-cntr,#onetrust-pc-sdk .ot-acc-txt h4+.ot-tgl-cntr{padding-left:13px}#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-subgrp>h5,#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-cat-header{width:calc(100% - 145px)}#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item h5+.ot-tgl-cntr,#onetrust-pc-sdk .ot-pli-hdr~.ot-cat-item .ot-cat-header+.ot-tgl{padding-left:28px}#onetrust-pc-sdk .ot-sel-all-hdr,#onetrust-pc-sdk .ot-sel-all-chkbox{display:inline-block;width:100%;position:relative}#onetrust-pc-sdk .ot-sel-all-chkbox{z-index:1}#onetrust-pc-sdk .ot-sel-all{margin:0;position:relative;padding-right:23px;float:right}#onetrust-pc-sdk .ot-consent-hdr,#onetrust-pc-sdk .ot-li-hdr{float:right;font-size:.812em;line-height:normal;text-align:center;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-li-hdr{max-width:100px;padding-right:10px}#onetrust-pc-sdk .ot-consent-hdr{max-width:55px}#onetrust-pc-sdk #ot-selall-licntr{display:block;width:21px;height:auto;float:right;position:relative;right:80px}#onetrust-pc-sdk #ot-selall-licntr label{position:absolute}#onetrust-pc-sdk .ot-ven-ctgl{margin-left:66px}#onetrust-pc-sdk .ot-ven-litgl+.ot-arw-cntr{margin-left:81px}#onetrust-pc-sdk .ot-enbl-chr .ot-host-cnt .ot-tgl-cntr{width:auto}#onetrust-pc-sdk #ot-lst-cnt:not(.ot-host-cnt) .ot-tgl-cntr{width:auto;top:auto;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-chkbox{position:relative;display:inline-block;width:20px;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-chkbox label{position:absolute;padding:0;width:20px;height:20px}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 2rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk .ot-acc-grpdesc+.ot-leg-btn-container{padding-left:20px;padding-right:20px;width:calc(100% - 40px);margin-bottom:5px}#onetrust-pc-sdk .ot-subgrp .ot-leg-btn-container{margin-bottom:5px}#onetrust-pc-sdk #ot-ven-lst .ot-leg-btn-container{margin-top:10px}#onetrust-pc-sdk .ot-leg-btn-container{display:inline-block;width:100%;margin-bottom:10px}#onetrust-pc-sdk .ot-leg-btn-container button{height:auto;padding:6.5px 8px;margin-bottom:0;letter-spacing:0;font-size:.75em;line-height:normal}#onetrust-pc-sdk .ot-leg-btn-container svg{display:none;height:14px;width:14px;padding-right:5px;vertical-align:sub}#onetrust-pc-sdk .ot-active-leg-btn{cursor:default;pointer-events:none}#onetrust-pc-sdk .ot-active-leg-btn svg{display:inline-block}#onetrust-pc-sdk .ot-remove-objection-handler{text-decoration:underline;padding:0;font-size:.75em;font-weight:600;line-height:1;padding-left:10px}#onetrust-pc-sdk .ot-obj-leg-btn-handler span{font-weight:bold;text-align:center;font-size:inherit;line-height:1.5}#onetrust-pc-sdk.ot-close-btn-link #close-pc-btn-handler{border:none;height:auto;line-height:1.5;text-decoration:underline;font-size:.69em;background:none;right:15px;top:15px;width:auto;font-weight:normal}#onetrust-pc-sdk .ot-cat-header{float:left;font-weight:600;font-size:.875em;line-height:1.5;max-width:90%;vertical-align:middle}#onetrust-pc-sdk .ot-vnd-item>button:focus{outline:#000 solid 2px}#onetrust-pc-sdk .ot-vnd-item>button{position:absolute;cursor:pointer;width:100%;height:100%;margin:0;top:0;left:0;z-index:1;max-width:none;border:none}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=false]~.ot-acc-txt{margin-top:0;max-height:0;opacity:0;overflow:hidden;width:100%;transition:.25s ease-out;display:none}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=true]~.ot-acc-txt{transition:.1s ease-in;margin-top:10px;width:100%;overflow:auto;display:block}#onetrust-pc-sdk .ot-vnd-item>button[aria-expanded=true]~.ot-acc-grpcntr{width:auto;margin-top:0px;padding-bottom:10px}#onetrust-pc-sdk .ot-accordion-layout.ot-cat-item{position:relative;border-radius:2px;margin:0;padding:0;border:1px solid #d8d8d8;border-top:none;width:calc(100% - 2px);float:left}#onetrust-pc-sdk .ot-accordion-layout.ot-cat-item:first-of-type{margin-top:10px;border-top:1px solid #d8d8d8}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc{padding-left:20px;padding-right:20px;width:calc(100% - 40px);font-size:.812em;margin-bottom:10px;margin-top:15px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc>ul{padding-top:10px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpdesc>ul li{padding-top:0;line-height:1.5;padding-bottom:10px}#onetrust-pc-sdk .ot-accordion-layout div+.ot-acc-grpdesc{margin-top:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr:first-child{margin-top:10px}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr:last-child,#onetrust-pc-sdk .ot-accordion-layout .ot-hlst-cntr:last-child{margin-bottom:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-hdr{padding-top:11.5px;padding-bottom:11.5px;padding-left:20px;padding-right:20px;width:calc(100% - 40px);display:inline-block}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-txt{width:100%;padding:0}#onetrust-pc-sdk .ot-accordion-layout .ot-subgrp-cntr{padding-left:20px;padding-right:15px;padding-bottom:0;width:calc(100% - 35px)}#onetrust-pc-sdk .ot-accordion-layout .ot-subgrp{padding-right:5px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-grpcntr{z-index:1;position:relative}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header+.ot-arw-cntr{position:absolute;top:50%;transform:translateY(-50%);right:20px;margin-top:-2px}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header+.ot-arw-cntr .ot-arw{width:15px;height:20px;margin-left:5px;color:dimgray}#onetrust-pc-sdk .ot-accordion-layout .ot-cat-header{float:none;color:#2e3644;margin:0;display:inline-block;height:auto;word-wrap:break-word;min-height:inherit}#onetrust-pc-sdk .ot-accordion-layout .ot-vlst-cntr,#onetrust-pc-sdk .ot-accordion-layout .ot-hlst-cntr{padding-left:20px;width:calc(100% - 20px);display:inline-block;margin-top:0;padding-bottom:2px}#onetrust-pc-sdk .ot-accordion-layout .ot-acc-hdr{position:relative;min-height:25px}#onetrust-pc-sdk .ot-accordion-layout h4~.ot-tgl,#onetrust-pc-sdk .ot-accordion-layout h4~.ot-always-active{position:absolute;top:50%;transform:translateY(-50%);right:20px}#onetrust-pc-sdk .ot-accordion-layout h4~.ot-tgl+.ot-tgl{right:95px}#onetrust-pc-sdk .ot-accordion-layout .category-vendors-list-handler,#onetrust-pc-sdk .ot-accordion-layout .category-vendors-list-handler+a{margin-top:5px}#onetrust-pc-sdk #ot-lst-cnt{margin-top:1rem;max-height:calc(100% - 96px)}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 2rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info{margin-bottom:1rem;padding-left:.75rem;padding-right:.75rem;display:flex;flex-direction:column}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info[data-vnd-info-key*=DPOEmail]{border-top:1px solid #d8d8d8;padding-top:1rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info[data-vnd-info-key*=DPOLink]{border-bottom:1px solid #d8d8d8;padding-bottom:1rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info .ot-vnd-lbl{font-weight:bold;font-size:.85em;margin-bottom:.5rem}#onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info .ot-vnd-cnt{margin-left:.5rem;font-weight:500;font-size:.85rem}#onetrust-pc-sdk .ot-vs-list,#onetrust-pc-sdk .ot-vnd-serv{width:auto;padding:1rem 1.25rem;padding-bottom:0}#onetrust-pc-sdk .ot-vs-list .ot-vnd-serv-hdr-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-serv-hdr-cntr{padding-bottom:.75rem;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-vs-list .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-weight:600;font-size:.95em;line-height:2;margin-left:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item{border:none;margin:0;padding:0}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item button,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item button{outline:none;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item button[aria-expanded=true],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item button[aria-expanded=true]{border-bottom:none}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:first-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:first-child{margin-top:.25rem;border-top:unset}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:last-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:last-child{margin-bottom:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item:last-child button,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item:last-child button{border-bottom:none}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info-cntr{border:1px solid #d8d8d8;padding:.75rem 1.75rem;padding-bottom:0;width:auto;margin-top:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info{margin-bottom:1rem;padding-left:.75rem;padding-right:.75rem;display:flex;flex-direction:column}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOEmail],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOEmail]{border-top:1px solid #d8d8d8;padding-top:1rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOLink],#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info[data-vnd-info-key*=DPOLink]{border-bottom:1px solid #d8d8d8;padding-bottom:1rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info .ot-vnd-lbl,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info .ot-vnd-lbl{font-weight:bold;font-size:.85em;margin-bottom:.5rem}#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-vnd-info .ot-vnd-cnt,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info .ot-vnd-cnt{margin-left:.5rem;font-weight:500;font-size:.85rem}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt{padding-left:40px}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-size:.8em}#onetrust-pc-sdk .ot-vs-list.ot-vnd-subgrp-cnt .ot-cat-header,#onetrust-pc-sdk .ot-vnd-serv.ot-vnd-subgrp-cnt .ot-cat-header{font-size:.8em}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv{margin-bottom:1rem;padding:1rem .95rem}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv .ot-vnd-serv-hdr-cntr{padding-bottom:.75rem;border-bottom:1px solid #d8d8d8}#onetrust-pc-sdk .ot-subgrp-cntr .ot-vnd-serv .ot-vnd-serv-hdr-cntr .ot-vnd-serv-hdr{font-weight:700;font-size:.8em;line-height:20px;margin-left:.82rem}#onetrust-pc-sdk .ot-subgrp-cntr .ot-cat-header{font-weight:700;font-size:.8em;line-height:20px}#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-vnd-serv .ot-vnd-lst-cont .ot-accordion-layout .ot-acc-hdr div.ot-chkbox{margin-left:.82rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr{padding:.5rem 0;margin:0;display:flex;width:100%;align-items:center;justify-content:space-between}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr div:first-child,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr div:first-child,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr div:first-child{margin-left:.5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr div:last-child,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr div:last-child,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr div:last-child{margin-right:.5rem;margin-left:.5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-always-active,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-always-active{position:relative;right:unset;top:unset;transform:unset}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-plus-minus,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-plus-minus{top:0}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-arw-cntr,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-arw-cntr{float:none;top:unset;right:unset;transform:unset;margin-top:-2px;position:relative}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-cat-header,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-cat-header{flex:1;margin:0 .5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-tgl,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-tgl{position:relative;transform:none;right:0;top:0;float:none}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox{position:relative;margin:0 .5rem}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox label{padding:0}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox label::before,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox label::before{position:relative}#onetrust-pc-sdk .ot-vs-config .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk ul.ot-subgrps .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk #ot-pc-lst .ot-vs-list .ot-vnd-item .ot-acc-hdr .ot-chkbox input,#onetrust-pc-sdk .ot-accordion-layout.ot-checkbox-consent .ot-acc-hdr .ot-chkbox input{position:absolute;cursor:pointer;width:100%;height:100%;opacity:0;margin:0;top:0;left:0;z-index:1}#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp .ot-acc-hdr h5.ot-cat-header,#onetrust-pc-sdk .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp .ot-acc-hdr h4.ot-cat-header{margin:0}#onetrust-pc-sdk .ot-vs-config .ot-subgrp-cntr ul.ot-subgrps li.ot-subgrp h5{top:0;line-height:20px}#onetrust-pc-sdk .ot-vs-list{display:flex;flex-direction:column;padding:0;margin:.5rem 4px}#onetrust-pc-sdk .ot-vs-selc-all{display:flex;padding:0;float:unset;align-items:center;justify-content:flex-start}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf{justify-content:flex-end}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf.ot-caret-conf .ot-sel-all-chkbox{margin-right:48px}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf .ot-sel-all-chkbox{margin:0;padding:0;margin-right:14px;justify-content:flex-end}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr.ot-chkbox,#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr.ot-tgl{display:inline-block;right:unset;width:auto;height:auto;float:none}#onetrust-pc-sdk .ot-vs-selc-all.ot-toggle-conf #ot-selall-vencntr label{width:45px;height:25px}#onetrust-pc-sdk .ot-vs-selc-all .ot-sel-all-chkbox{margin-right:11px;margin-left:.75rem;display:flex;align-items:center}#onetrust-pc-sdk .ot-vs-selc-all .sel-all-hdr{margin:0 1.25rem;font-size:.812em;line-height:normal;text-align:center;word-break:break-word;word-wrap:break-word}#onetrust-pc-sdk .ot-vnd-list-cnt #ot-selall-vencntr.ot-chkbox{float:unset;right:0}#onetrust-pc-sdk[dir=rtl] #ot-back-arw,#onetrust-pc-sdk[dir=rtl] input~.ot-acc-hdr .ot-arw{transform:rotate(180deg);-o-transform:rotate(180deg);-ms-transform:rotate(180deg);-webkit-transform:rotate(180deg)}#onetrust-pc-sdk[dir=rtl] input:checked~.ot-acc-hdr .ot-arw{transform:rotate(270deg);-o-transform:rotate(270deg);-ms-transform:rotate(270deg);-webkit-transform:rotate(270deg)}#onetrust-pc-sdk[dir=rtl] .ot-chkbox label::after{transform:rotate(45deg);-webkit-transform:rotate(45deg);-o-transform:rotate(45deg);-ms-transform:rotate(45deg);border-left:0;border-right:3px solid}#onetrust-pc-sdk[dir=rtl] .ot-search-cntr>svg{right:0}@media only screen and (max-width: 600px){#onetrust-pc-sdk.otPcCenter{left:0;min-width:100%;height:100%;top:0;border-radius:0}#onetrust-pc-sdk #ot-pc-content,#onetrust-pc-sdk.ot-ftr-stacked .ot-btn-container{margin:1px 3px 0 10px;padding-right:10px;width:calc(100% - 23px)}#onetrust-pc-sdk .ot-btn-container button{max-width:none;letter-spacing:.01em}#onetrust-pc-sdk #close-pc-btn-handler{top:10px;right:17px}#onetrust-pc-sdk p{font-size:.7em}#onetrust-pc-sdk #ot-pc-hdr{margin:10px 10px 0 5px;width:calc(100% - 15px)}#onetrust-pc-sdk .vendor-search-handler{font-size:1em}#onetrust-pc-sdk #ot-back-arw{margin-left:12px}#onetrust-pc-sdk #ot-lst-cnt{margin:0;padding:0 5px 0 10px;min-width:95%}#onetrust-pc-sdk .switch+p{max-width:80%}#onetrust-pc-sdk .ot-ftr-stacked button{width:100%}#onetrust-pc-sdk #ot-fltr-cnt{max-width:320px;width:90%;border-top-right-radius:0;border-bottom-right-radius:0;margin:0;margin-left:15px;left:auto;right:40px;top:85px}#onetrust-pc-sdk .ot-fltr-opt{margin-left:25px;margin-bottom:10px}#onetrust-pc-sdk .ot-pc-refuse-all-handler{margin-bottom:0}#onetrust-pc-sdk #ot-fltr-cnt{right:40px}}@media only screen and (max-width: 476px){#onetrust-pc-sdk .ot-fltr-cntr,#onetrust-pc-sdk #ot-fltr-cnt{right:10px}#onetrust-pc-sdk #ot-anchor{right:25px}#onetrust-pc-sdk button{width:100%}#onetrust-pc-sdk:not(.ot-addtl-vendors) #ot-pc-lst:not(.ot-enbl-chr) .ot-sel-all{padding-right:9px}#onetrust-pc-sdk:not(.ot-addtl-vendors) #ot-pc-lst:not(.ot-enbl-chr) .ot-tgl-cntr{right:0}}@media only screen and (max-width: 896px)and (max-height: 425px)and (orientation: landscape){#onetrust-pc-sdk.otPcCenter{left:0;top:0;min-width:100%;height:100%;border-radius:0}#onetrust-pc-sdk #ot-anchor{left:initial;right:50px}#onetrust-pc-sdk #ot-lst-title{margin-top:12px}#onetrust-pc-sdk #ot-lst-title *{font-size:inherit}#onetrust-pc-sdk #ot-pc-hdr input{margin-right:0;padding-right:45px}#onetrust-pc-sdk .switch+p{max-width:85%}#onetrust-pc-sdk #ot-sel-blk{position:static}#onetrust-pc-sdk #ot-pc-lst{overflow:auto}#onetrust-pc-sdk #ot-lst-cnt{max-height:none;overflow:initial}#onetrust-pc-sdk #ot-lst-cnt.no-results{height:auto}#onetrust-pc-sdk input{font-size:1em !important}#onetrust-pc-sdk p{font-size:.6em}#onetrust-pc-sdk #ot-fltr-modal{width:100%;top:0}#onetrust-pc-sdk ul li p,#onetrust-pc-sdk .category-vendors-list-handler,#onetrust-pc-sdk .category-vendors-list-handler+a,#onetrust-pc-sdk .category-host-list-handler{font-size:.6em}#onetrust-pc-sdk.ot-shw-fltr #ot-anchor{display:none !important}#onetrust-pc-sdk.ot-shw-fltr #ot-pc-lst{height:100% !important;overflow:hidden;top:0px}#onetrust-pc-sdk.ot-shw-fltr #ot-fltr-cnt{margin:0;height:100%;max-height:none;padding:10px;top:0;width:calc(100% - 20px);position:absolute;right:0;left:0;max-width:none}#onetrust-pc-sdk.ot-shw-fltr .ot-fltr-scrlcnt{max-height:calc(100% - 65px)}}
            #onetrust-consent-sdk #onetrust-pc-sdk,
                #onetrust-consent-sdk #ot-search-cntr,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-switch.ot-toggle,
                #onetrust-consent-sdk #onetrust-pc-sdk ot-grp-hdr1 .checkbox,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title:after
                ,#onetrust-consent-sdk #onetrust-pc-sdk #ot-sel-blk,
                        #onetrust-consent-sdk #onetrust-pc-sdk #ot-fltr-cnt,
                        #onetrust-consent-sdk #onetrust-pc-sdk #ot-anchor {
                    background-color: #ffffff;
                }
               
            #onetrust-consent-sdk #onetrust-pc-sdk h3,
                #onetrust-consent-sdk #onetrust-pc-sdk h4,
                #onetrust-consent-sdk #onetrust-pc-sdk h5,
                #onetrust-consent-sdk #onetrust-pc-sdk h6,
                #onetrust-consent-sdk #onetrust-pc-sdk p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-ven-lst .ot-ven-opts p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-desc,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-title,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-li-title,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-sel-all-hdr span,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-fltr-modal #modal-header,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-checkbox label span,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-sel-blk p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-lst-title h3,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst .back-btn-handler p,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst .ot-ven-name,
                #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-lst #ot-ven-lst .consent-category,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-inactive-leg-btn,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-label-status,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-chkbox label span,
                #onetrust-consent-sdk #onetrust-pc-sdk #clear-filters-handler,
                #onetrust-consent-sdk #onetrust-pc-sdk .ot-optout-signal
                {
                    color: #777777;
                }
             #onetrust-consent-sdk #onetrust-pc-sdk .privacy-notice-link,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler + a,
                    #onetrust-consent-sdk #onetrust-pc-sdk .category-host-list-handler,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-ven-link,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-name a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-acc-hdr .ot-host-expand,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-pc-content #ot-pc-desc .ot-link-btn,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-vnd-serv .ot-vnd-item .ot-vnd-info a,
                    #onetrust-consent-sdk #onetrust-pc-sdk #ot-lst-cnt .ot-vnd-info a
                    {
                        color: #b70014;
                    }
            #onetrust-consent-sdk #onetrust-pc-sdk .category-vendors-list-handler:hover { text-decoration: underline;}
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-grpcntr.ot-acc-txt,
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-txt .ot-subgrp-tgl .ot-switch.ot-toggle
             {
                background-color: #F8F8F8;
            }
             #onetrust-consent-sdk #onetrust-pc-sdk #ot-host-lst .ot-host-info,
                    #onetrust-consent-sdk #onetrust-pc-sdk .ot-acc-txt .ot-ven-dets
                            {
                                background-color: #F8F8F8;
                            }
        #onetrust-consent-sdk #onetrust-pc-sdk
            button:not(#clear-filters-handler):not(.ot-close-icon):not(#filter-btn-handler):not(.ot-remove-objection-handler):not(.ot-obj-leg-btn-handler):not([aria-expanded]):not(.ot-link-btn),
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-active-leg-btn {
                background-color: #777777;border-color: #777777;
                color: #ffffff;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-active-menu {
                border-color: #777777;
            }
            
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-remove-objection-handler{
                background-color: transparent;
                border: 1px solid transparent;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-leg-btn-container .ot-inactive-leg-btn {
                background-color: #FFFFFF;
                color: #78808E; border-color: #78808E;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-tgl input:focus + .ot-switch, .ot-switch .ot-switch-nob, .ot-switch .ot-switch-nob:before,
            #onetrust-pc-sdk .ot-checkbox input[type="checkbox"]:focus + label::before,
            #onetrust-pc-sdk .ot-chkbox input[type="checkbox"]:focus + label::before {
                outline-color: #777777;
                outline-width: 1px;
            }
            #onetrust-pc-sdk .ot-host-item > button:focus, #onetrust-pc-sdk .ot-ven-item > button:focus {
                border: 1px solid #777777;
            }
            #onetrust-consent-sdk #onetrust-pc-sdk *:focus,
            #onetrust-consent-sdk #onetrust-pc-sdk .ot-vlst-cntr > a:focus {
               outline: 1px solid #777777;
            }#onetrust-pc-sdk .ot-vlst-cntr .ot-ext-lnk {
                    background-image: url('https://cdn-apac.onetrust.com/logos/static/ot_external_link.svg');
                }
            #onetrust-pc-sdk .ot-cat-grp .ot-always-active {
    color: #b70014;
}

#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob {

    border-color: #b70014;
    background-color: #f0dcdc;

}

#onetrust-pc-sdk .ot-tgl input:checked+.ot-switch .ot-switch-nob:before {

    background-color: #b70014;
    border-color: #b70014;

}.ot-sdk-cookie-policy{font-family:inherit;font-size:16px}.ot-sdk-cookie-policy.otRelFont{font-size:1rem}.ot-sdk-cookie-policy h3,.ot-sdk-cookie-policy h4,.ot-sdk-cookie-policy h6,.ot-sdk-cookie-policy p,.ot-sdk-cookie-policy li,.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy th,.ot-sdk-cookie-policy #cookie-policy-description,.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}.ot-sdk-cookie-policy h4{font-size:1.2em}.ot-sdk-cookie-policy h6{font-size:1em;margin-top:2em}.ot-sdk-cookie-policy th{min-width:75px}.ot-sdk-cookie-policy a,.ot-sdk-cookie-policy a:hover{background:#fff}.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}.ot-sdk-cookie-policy .ot-mobile-border{display:none}.ot-sdk-cookie-policy section{margin-bottom:2em}.ot-sdk-cookie-policy table{border-collapse:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy{font-family:inherit;font-size:1rem}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h3,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h4,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title{color:dimgray}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup{margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group-desc,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-table-header,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td{font-size:.9em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td span,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td a{font-size:inherit}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group{font-size:1em;margin-bottom:.6em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-title{margin-bottom:1.2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy>section{margin-bottom:1em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th{min-width:75px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a:hover{background:#fff}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead{background-color:#f6f6f4;font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-mobile-border{display:none}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy section{margin-bottom:2em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li{list-style:disc;margin-left:1.5em}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-subgroup ul li h4{display:inline-block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{border-collapse:inherit;margin:auto;border:1px solid #d7d7d7;border-radius:5px;border-spacing:initial;width:100%;overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border-bottom:1px solid #d7d7d7;border-right:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr th:last-child,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr td:last-child{border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:25%}.ot-sdk-cookie-policy[dir=rtl]{text-align:left}#ot-sdk-cookie-policy h3{font-size:1.5em}@media only screen and (max-width: 530px){.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) table,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tbody,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) th,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td,.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{display:block}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) thead tr{position:absolute;top:-9999px;left:-9999px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr{margin:0 0 1em 0}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd),.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) tr:nth-child(odd) a{background:#f6f6f4}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td{border:none;border-bottom:1px solid #eee;position:relative;padding-left:50%}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{position:absolute;height:100%;left:6px;width:40%;padding-right:10px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) .ot-mobile-border{display:inline-block;background-color:#e4e4e4;position:absolute;height:100%;top:0;left:45%;width:2px}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) td:before{content:attr(data-label);font-weight:bold}.ot-sdk-cookie-policy:not(#ot-sdk-cookie-policy-v2) li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table{overflow:hidden}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table td{border:none;border-bottom:1px solid #d7d7d7}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tbody,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{display:block}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-host,#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table .ot-cookies-type{width:auto}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy tr{margin:0 0 1em 0}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{height:100%;width:40%;padding-right:10px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td:before{content:attr(data-label);font-weight:bold}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li{word-break:break-word;word-wrap:break-word}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy thead tr{position:absolute;top:-9999px;left:-9999px;z-index:-9999}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td{border-bottom:1px solid #d7d7d7;border-right:0px}#ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table tr:last-child td:last-child{border-bottom:0px}}
                
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h5,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy h6,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy li,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy p,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy a,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy span,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy td,
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-description {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy th {
                        color: #696969;
                    }
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy .ot-sdk-cookie-policy-group {
                        color: #696969;
                    }
                    
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy #cookie-policy-title {
                            color: #696969;
                        }
                    
            
                    #ot-sdk-cookie-policy-v2.ot-sdk-cookie-policy table th {
                            background-color: #F8F8F8;
                        }
                    
            .ot-floating-button__front{background-image:url('https://cdn-apac.onetrust.com/logos/static/ot_persistent_cookie.png')}</style></head><body class="ja">

<div id="wrapper">
  <header>
    <div id="header_meta">
      <a href="https://www.konami.com/games/jp/ja/" target="_blank"><img src="http://www.yugioh-card.com/ci/logo/konami_logo_normal.png" alt="KONAMI" id="konami" class="ui-draggable ui-draggable-handle" style="position: relative;"></a>

      <nav id="language">
        <span class="hex2_1 orn"><span class="hex2_2">
          日本語
          
          
          
          
          
           
           
        </span></span>
        <ul>
          <li><a href="javascript:ChangeLanguage('ja')" class="current">日本語</a></li>
          <li><a href="javascript:ChangeLanguage('en')">English</a></li>
          <li><a href="javascript:ChangeLanguage('de')">Deutsch</a></li>
          <li><a href="javascript:ChangeLanguage('fr')">Français</a></li>
          <li><a href="javascript:ChangeLanguage('it')">Italiano</a></li>
          <li><a href="javascript:ChangeLanguage('es')">Español</a></li>
          <li><a href="javascript:ChangeLanguage('pt')">Portugues</a></li>
          <li><a href="javascript:ChangeLanguage('ko')">한글</a></li>
        </ul>
      </nav>

    </div><!--#header_meta-->


    <div id="header_menu">
      <nav>
        <dl id="menber_menu">
  
  
          <dd class="rogin">
            <div class="rogin_btn">
              <div class="hex2_1 my"><div class="hex2_2"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"></path></svg>ログイン中 <span>[0039904244]</span></div></div>
              <a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"></path></svg>ログアウト</span></a>
              </div>
          </dd>
  
          <dd class="logo"></dd>
          
          <dd class="forbidden_limited">
            <a class="btn hex pnk" href="/yugiohdb/forbidden_limited.action">
              <span>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 35.32"><defs></defs><path d="M26.09,16v3.57a10.85,10.85,0,0,0,.16-1.8A10.5,10.5,0,0,0,26.09,16Zm0,17.94H18a17,17,0,0,1-5.6,0H4.15V30a17.58,17.58,0,0,1-1.37-1.36v6.67H27.46V28.8a17.2,17.2,0,0,1-1.37,1.33ZM23.35,23.08V13.74L22,15.1v6.62H15.26l-1.37,1.36ZM4.15,1.35H26.09V5.44a14.34,14.34,0,0,1,1.37,1.33V0H2.78V6.93A17.71,17.71,0,0,1,4.15,5.56Zm0,16.83v0ZM8.26,9.25a10.62,10.62,0,0,0-1.38,1.3V22.36L8.26,21Zm6.92,23.58A15,15,0,1,0,0,17.83a15,15,0,0,0,15.19,15Zm12.54-15A12.56,12.56,0,0,1,7.47,27.55L25.06,10.13a12.29,12.29,0,0,1,2.67,7.65ZM15.19,5.37a12.54,12.54,0,0,1,8,2.82L5.5,25.65a12.3,12.3,0,0,1-2.84-7.87A12.47,12.47,0,0,1,15.19,5.37Z" transform="translate(0.01)"></path></svg>
                <h3>リミットレギュレーション</h3>
                
              </span>
            </a>
          </dd>
        </dl><!--#menber_menu-->
        <div class="bottom">
          <div id="spnav_btn" style="display: none;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41.59 31"><defs></defs><path d="M2.63,0H39a2.64,2.64,0,0,1,2.64,2.63h0A2.63,2.63,0,0,1,39,5.26H2.63A2.63,2.63,0,0,1,0,2.63H0A2.63,2.63,0,0,1,2.63,0Z"></path><path d="M2.63,12.87H39a2.64,2.64,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,18.13H2.63A2.63,2.63,0,0,1,0,15.5H0A2.63,2.63,0,0,1,2.63,12.87Z"></path><path d="M2.63,25.74H39a2.63,2.63,0,0,1,2.64,2.63h0A2.64,2.64,0,0,1,39,31H2.63A2.63,2.63,0,0,1,0,28.37H0A2.63,2.63,0,0,1,2.63,25.74Z"></path></svg></div>
          


        <ul class="main_menu">
          
          <li class="menu_top"><a href="/yugiohdb/"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"></path></svg><h3>Top</h3></a></li>

          
          <li class="menu_card_search">
            <a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"></stop><stop offset="1" stop-color="#fff"></stop></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"></path></svg><h3>カード検索</h3></a>

          </li>

          
          <li class="menu_cardlist sab_menu">
            <a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"></path></svg><h3>カードリスト</h3></a>
            <ul>
              <li><a href="/yugiohdb/card_list.action?clm=3">公開日の新しい順</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=1">一般商品</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=2">特典・同梱系</a></li>
        
              <li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
        
            </ul>
          </li>

          
          <li class="menu_decks">
            <a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"></path></svg><h3>デッキ検索</h3></a>
          </li>
        </ul>
          
          <div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

        <ul class="main_menu">

          
      

          <li class="menu_trends sab_menu">
            <a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><!--?xml version="1.0" encoding="UTF-8"?--><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g><g><path d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"></path></g></g></svg><h3>トレンド</h3></a>
            <ul>
              
              <li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
              
              <li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
            </ul>
          </li>
      
      



  
  
  
  
        

          
          <li class="my menu_my_decks sab_menu">
            <a class="main" href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"></path></svg><h3>マイデッキ</h3></a>
            <ul>
              <li><a href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
              <li><a href="/yugiohdb/member_deck.action?ope=21&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
            </ul>
          </li>

          
          <li class="my menu_my_cardlist sab_menu">
            <a class="main" href="/yugiohdb/member_have_want_card.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"></path></svg><h3>マイカードリスト</h3></a>
            <ul>
              <li><a href="member_have_want_card.action?ope=1">持っているカードリスト</a></li>
              <li><a href="member_have_want_card.action?ope=2">欲しいカードリスト</a></li>
            </ul>
          </li>
  

        

          
          <li class="menu_q_a">
            <a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"></path></svg><h3>Ｑ＆Ａ</h3></a>
          </li>
        
          
          <li class="menu_forbidden">
            <a href="/yugiohdb/forbidden_limited.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 35.32"><defs></defs><path d="M26.09,16v3.57a10.85,10.85,0,0,0,.16-1.8A10.5,10.5,0,0,0,26.09,16Zm0,17.94H18a17,17,0,0,1-5.6,0H4.15V30a17.58,17.58,0,0,1-1.37-1.36v6.67H27.46V28.8a17.2,17.2,0,0,1-1.37,1.33ZM23.35,23.08V13.74L22,15.1v6.62H15.26l-1.37,1.36ZM4.15,1.35H26.09V5.44a14.34,14.34,0,0,1,1.37,1.33V0H2.78V6.93A17.71,17.71,0,0,1,4.15,5.56Zm0,16.83v0ZM8.26,9.25a10.62,10.62,0,0,0-1.38,1.3V22.36L8.26,21Zm6.92,23.58A15,15,0,1,0,0,17.83a15,15,0,0,0,15.19,15Zm12.54-15A12.56,12.56,0,0,1,7.47,27.55L25.06,10.13a12.29,12.29,0,0,1,2.67,7.65ZM15.19,5.37a12.54,12.54,0,0,1,8,2.82L5.5,25.65a12.3,12.3,0,0,1-2.84-7.87A12.47,12.47,0,0,1,15.19,5.37Z" transform="translate(0.01)"></path></svg><h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br>レギュレーション</span></h3></a>
          </li>
          <li class="menu_btn_pagetop"><a href="#"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"></path></svg></a></li>

        </ul><!--#main_menu-->

        </div>

      </nav>
    </div><!-- #header_menu-->
  </header>
  <div id="spnav" style="display: none;">
    <ul class="main_menu">

  
  
  
  
      <li class="rogin my">
        
        <div class="rogin_btn">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51.4 51.4"><defs></defs><path d="M30,55.7A25.7,25.7,0,1,1,55.7,30,25.69,25.69,0,0,1,30,55.7ZM30,9.4A20.57,20.57,0,0,0,9.4,30,20.31,20.31,0,0,0,15,44.1a15.15,15.15,0,0,1,6.4-9,13.07,13.07,0,0,1-4.3-9.6,12.9,12.9,0,0,1,25.8,0,13.07,13.07,0,0,1-4.3,9.6,15.9,15.9,0,0,1,6.4,9h0c-1.7,1.7-1.3,1.4,0,0h0A20.31,20.31,0,0,0,50.6,30,20.57,20.57,0,0,0,30,9.4Z" transform="translate(-4.3 -4.3)"></path></svg>ログイン中
          <span>[0039904244]</span>
        </div>
        
        <a class="logout" href="https://my.konami.net/logout/logout.html?redirect_uri=https%3a%2f%2fwww%2edb%2eyugioh%2dcard%2ecom%2fyugiohdb%2fmember_logout%2eaction">
          <span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 49.2 54"><defs></defs><path d="M33.6,57V47h-12V34h5v8h7V13L44.1,8H26.6v9h-5V3h33V47Zm-5-26h-10v6.7L5.4,26,18.6,14.3V21h10Z" transform="translate(-5.4 -3)"></path></svg>ログアウト</span>
        </a>
      </li>
  
    </ul>
    


        <ul class="main_menu">
          
          <li class="menu_top"><a href="/yugiohdb/"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"></path></svg><h3>Top</h3></a></li>

          
          <li class="menu_card_search">
            <a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"></stop><stop offset="1" stop-color="#fff"></stop></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"></path></svg><h3>カード検索</h3></a>

          </li>

          
          <li class="menu_cardlist sab_menu">
            <a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"></path></svg><h3>カードリスト</h3></a>
            <ul>
              <li><a href="/yugiohdb/card_list.action?clm=3">公開日の新しい順</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=1">一般商品</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=2">特典・同梱系</a></li>
        
              <li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
        
            </ul>
          </li>

          
          <li class="menu_decks">
            <a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"></path></svg><h3>デッキ検索</h3></a>
          </li>
        </ul>
          
          <div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

        <ul class="main_menu">

          
      

          <li class="menu_trends sab_menu">
            <a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><!--?xml version="1.0" encoding="UTF-8"?--><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g><g><path d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"></path></g></g></svg><h3>トレンド</h3></a>
            <ul>
              
              <li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
              
              <li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
            </ul>
          </li>
      
      



  
  
  
  
        

          
          <li class="my menu_my_decks sab_menu">
            <a class="main" href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"></path></svg><h3>マイデッキ</h3></a>
            <ul>
              <li><a href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
              <li><a href="/yugiohdb/member_deck.action?ope=21&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
            </ul>
          </li>

          
          <li class="my menu_my_cardlist sab_menu">
            <a class="main" href="/yugiohdb/member_have_want_card.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"></path></svg><h3>マイカードリスト</h3></a>
            <ul>
              <li><a href="member_have_want_card.action?ope=1">持っているカードリスト</a></li>
              <li><a href="member_have_want_card.action?ope=2">欲しいカードリスト</a></li>
            </ul>
          </li>
  

        

          
          <li class="menu_q_a">
            <a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"></path></svg><h3>Ｑ＆Ａ</h3></a>
          </li>
        
          
          <li class="menu_forbidden">
            <a href="/yugiohdb/forbidden_limited.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 35.32"><defs></defs><path d="M26.09,16v3.57a10.85,10.85,0,0,0,.16-1.8A10.5,10.5,0,0,0,26.09,16Zm0,17.94H18a17,17,0,0,1-5.6,0H4.15V30a17.58,17.58,0,0,1-1.37-1.36v6.67H27.46V28.8a17.2,17.2,0,0,1-1.37,1.33ZM23.35,23.08V13.74L22,15.1v6.62H15.26l-1.37,1.36ZM4.15,1.35H26.09V5.44a14.34,14.34,0,0,1,1.37,1.33V0H2.78V6.93A17.71,17.71,0,0,1,4.15,5.56Zm0,16.83v0ZM8.26,9.25a10.62,10.62,0,0,0-1.38,1.3V22.36L8.26,21Zm6.92,23.58A15,15,0,1,0,0,17.83a15,15,0,0,0,15.19,15Zm12.54-15A12.56,12.56,0,0,1,7.47,27.55L25.06,10.13a12.29,12.29,0,0,1,2.67,7.65ZM15.19,5.37a12.54,12.54,0,0,1,8,2.82L5.5,25.65a12.3,12.3,0,0,1-2.84-7.87A12.47,12.47,0,0,1,15.19,5.37Z" transform="translate(0.01)"></path></svg><h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br>レギュレーション</span></h3></a>
          </li>
          <li class="menu_btn_pagetop"><a href="#"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"></path></svg></a></li>

        </ul><!--#main_menu-->

    <div class="close"><span>✕</span>閉じる</div>
  </div>
  <div id="bg">




  <nav id="pan_nav"><div>
    <ul>
      <li><a href="/yugiohdb/">ホーム</a></li><!--
     --><li>»</li><!--
     --><li><a href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li><!--
     --><li>»</li><!--
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

      <div id="deck_header" class="box_default">

  


        <textarea class="p_url" type="text" wrap="soft" style="resize: none; overflow: hidden; overflow-wrap: break-word; height: 30px;" onclick="this.setSelectionRange(0,9999);" readonly="">http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja</textarea>



      <div class="box_default_table">



        <dl>


          <dt>
            <span>お気に入り</span>
          </dt>
          <dd class="mark_btn_set star">
            <span class="num" id="favoriteCnt">0</span>
  
            <label class="mark_btn star">
              <input type="checkbox" name="deckFavorite" id="deckFavorite" class="checkbox01-input" onclick="updateDeckFavorite()">
              <div class="btn hex check orn"><span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.97 98.94"><defs></defs><g><polygon points="103.97 37.79 70.18 29.63 51.98 0 33.79 29.63 0 37.79 22.55 64.26 19.86 98.94 51.98 85.66 84.11 98.94 81.42 64.26 103.97 37.79"></polygon></g></svg> お気に入り</span></div>
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
            <span>PDF</span>
          </dt>
          <dd class="a_set">
            
            <a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=1&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja"><span>PDFで印刷</span></a>
            
            <a class="btn hex " href="/yugiohdb/member_deck_pdf.action?pdfType=2&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja"><span>PDFで印刷（名前）</span></a>

          </dd>
        </dl>
    
    
  



      </div>


  
      <div id="bottom_btn_set">
        
        <a class="btn hex " href="/yugiohdb/member_deck.action?ope=8&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja"><span>デッキをコピー</span></a>

    
        
        <a class="btn hex orn" href="/yugiohdb/member_deck.action?ope=2&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja"><span>編集開始</span></a>
    
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
      
      <iframe src="//platform.twitter.com/widgets/tweet_button.html?url=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202306110137&amp;lang=ja&amp;count=horizontal&amp;hashtags=YugiohDB_JP " scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowtransparency="true"></iframe>

      
      <iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202306110137&amp;send=false&amp;layout=button_count&amp;show_faces=false&amp;action=like&amp;colorscheme=light&amp;locale=ja_JP" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:20px;" allowtransparency="true"></iframe>

      
      <div class="fb-share-button" data-href="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja&amp;a=202306110137" data-layout="button_count" data-size="small"></div>

      
      <iframe data-lang="ja" data-type="share-a" data-url="http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja&amp;a=202306110137" data-line-it-id="0" scrolling="no" frameborder="0" allowtransparency="true" style="width: 86px; height: 20px; visibility: visible; position: static !important; opacity: 1 !important;" class="line-it-button" src="https://social-plugins.line.me/widget/share?url=http%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fcgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70%26request_locale%3Dja%26a%3D202306110137&amp;buttonType=share-a&amp;lang=ja&amp;type=share&amp;id=0&amp;origin=https%3A%2F%2Fwww.db.yugioh-card.com%2Fyugiohdb%2Fmember_deck.action%3Fope%3D1%26cgid%3Dc8525f77e0268f9b1ba9110a8a05bc35%26dno%3D70&amp;title=%E9%81%8A%E6%88%AF%E7%8E%8B%20%E3%83%87%E3%83%83%E3%82%AD%E3%83%AC%E3%82%B7%E3%83%94%20%E8%A9%B3%E7%B4%B0%20%7C%20%E9%81%8A%E6%88%AF%E7%8E%8B%20%E3%82%AA%E3%83%95%E3%82%A3%E3%82%B7%E3%83%A3%E3%83%AB%E3%82%AB%E3%83%BC%E3%83%89%E3%82%B2%E3%83%BC%E3%83%A0%20%E3%83%87%E3%83%A5%E3%82%A8%E3%83%AB%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%BA%20-%20%E3%82%AB%E3%83%BC%E3%83%89%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9&amp;env=REAL" title="このページの情報をLINEでシェアできます。"></iframe>
      <script src="https://d.line-scdn.net/r/web/social-plugin/js/thirdparty/loader.min.js" async="async" defer="defer"></script>
    </div>
  </div>



<form name="form_sort" method="POST" action="/yugiohdb/member_deck.action?ope=1&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35&amp;dno=70&amp;request_locale=ja">
  
  <div id="num_total">

    
    <a id="num_total_m" class="navbtn hex btn" href="#main"><span>
      <h4>メインデッキ合計</h4>
      <div class="hex icon icon_r"><span>40</span></div>
    </span></a>

    
    <a id="num_total_e" class="navbtn hex btn" href="#extra"><span>
      <h4>エクストラデッキ合計</h4>
      <div class="hex icon icon_r"><span>15</span></div>
    </span></a>

    
    <a id="num_total_s" class="navbtn hex btn" href="#side"><span>
      <h4>サイドデッキ合計</h4>
      <div class="hex icon icon_r"><span>3</span></div>
    </span></a>


  </div>
  


  
  <div class="sort_set">
    <div class="pulldown">

      <span>
        <select id="sort" name="sort">
          <option value="1">登録順</option>
          <option value="2">名前順</option>
          <option value="3">レベル／ランク／リンク順</option>
        </select>
      </span>
    </div>
  </div>


  
  <div id="mode_set" class="tablink">
    <ul>
      <li class="3"><span>テキスト詳細表示</span></li>
      <li class="1"><span>テキスト表示</span></li>
      <li class="2 now"><span>画像表示</span></li>
    </ul>
    <select id="deck_display" name="deck_display">
      <option value="3">テキスト詳細表示</option>
      <option value="1">テキスト表示</option>
      <option value="2">画像表示</option>
    </select>
  </div>
</form>


  <div id="deck_text" style="display: none;">
    


      <div id="text_main" class="deck_set">
        <table id="monster_list" class="deck_list">
          <tbody><tr>
            <th colspan="3">モンスターカード</th>
            <th class="num">
              <span>6</span>
            </th>
          </tr>
  
  
    
          <tr class=" row">

            <td class="row_num">
              1
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_effect.png" alt="効果/モンスター" title="効果/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>夢幻崩界イヴリース</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13571&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">

            <td class="row_num">
              2
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_effect.png" alt="効果/モンスター" title="効果/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>斬機サーキュラー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=17430&amp;request_locale=ja">
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
    
  
  

        </tbody></table><!--#monster_list-->


  
        <table id="spell_list" class="deck_list">

          <tbody><tr>
            <th colspan="3">魔法カード</th>
            <th class="num">
              <span>20</span>
            </th>
          </tr>
  
    
          <tr class=" row">
            <td class="row_num">
              1
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>サイバネット・マイニング</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14301&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              2
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>斬機方程式</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14753&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              3
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>スモール・ワールド</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=16555&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              4
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>転生炎獣の聖域</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13938&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class="semi_limited row">
            <td class="row_num">
              5
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>墓穴の指名者</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13619&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
          </tr>
    
    
  
    
          <tr class="limited row">
            <td class="row_num">
              6
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>抹殺の指名者</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14627&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              7
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>アームズ・ホール</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=7493&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              8
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>アームド・チェンジャー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=6524&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
          </tr>
    
    
  
    

        </tbody></table><!--#spell_list-->


    
        <table id="trap_list" class="deck_list">

          <tbody><tr>
            <th colspan="3">罠カード</th>
            <th class="num">
              <span>14</span>
            </th>
          </tr>
  
    
          <tr class=" row">
            <td class="row_num">
              1
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>強制脱出装置</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=5914&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              2
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>無限泡影</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13631&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              3
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>斬機超階乗</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14755&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              4
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>サイバネット・コンフリクト</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13878&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>3</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              5
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>神の警告</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=9008&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
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
    
  
  

        </tbody></table><!--#trap_list-->
      </div><!-- .deck_set -->
      <div class="deck_set">

  
        <table id="extra_list" class="deck_list">

          <tbody><tr>
            <th colspan="3">エクストラデッキ</th>
            <th class="num">
              <span>15</span>
            </th>
          </tr>

  
    
          <tr class=" row">
            <td class="row_num">
              1
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>塊斬機ラプラシアン</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14752&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              2
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>塊斬機ダランベルシアン</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              3
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>リンク・スパイダー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13034&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              4
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>転生炎獣ベイルリンクス</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14249&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              5
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>転生炎獣アルミラージ</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14338&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              6
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>コード・トーカー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13460&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              7
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>アップデートジャマー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14122&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              8
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>スプラッシュ・メイジ</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=15034&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              9
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>トランスコード・トーカー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13698&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>2</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              10
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>デコード・トーカー・ヒートソウル</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14962&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              11
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>ファイアウォール・ドラゴン</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13082&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>1</span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              12
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>アクセスコード・トーカー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=15032&amp;request_locale=ja">
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
    
  

  
        </tbody></table><!--#extra_list-->




        <table id="side_list" class="deck_list">
          <tbody><tr>
            <th colspan="3">サイドデッキ</th>
            <th class="num">
              <span>3</span>
            </th>
          </tr>

  
    
          <tr class=" row">
            <td class="row_num">
              1
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>塊斬機ダランベルシアン</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>
                1
              </span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              2
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>リングリボー</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14904&amp;request_locale=ja">
            </td>
            <td class="num">
              <span>
                1
              </span>
            </td>
          </tr>
    
    
  
    
          <tr class=" row">
            <td class="row_num">
              3
            </td>
            <td class="c_img">
      
              <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
      
      
            </td>
            <td class="card_name">
              <span>コード・トーカー・インヴァート</span>
              <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14542&amp;request_locale=ja">
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
    
  

  
        </tbody></table><!--#side_list-->
        <div class="deck_none"></div>

      </div><!-- .deck_set -->
  </div><!-- #deck_text -->




  <div id="deck_detailtext" style="display: none;">
    


  
  <div id="detailtext_main" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
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
      <div class="t_body">
    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">1</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_effect.png" alt="効果/モンスター" title="効果/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">夢幻崩界イヴリース</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13571&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13571">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
                    闇属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
      
        
        
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/icon_level.png" alt="レベル" title="レベル">
                    レベル
        

                    &nbsp;2
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/0
                    </span>
      
      
                    <span class="">
                      守備力/
        
        
                          0
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">2</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_effect.png" alt="効果/モンスター" title="効果/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">斬機サーキュラー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=17430&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="17430">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
                    光属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
      
        
        
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/icon_level.png" alt="レベル" title="レベル">
                    レベル
        

                    &nbsp;4
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/1500
                    </span>
      
      
                    <span class="">
                      守備力/
        
        
                          1500
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
      </div>
  
  

  
  
      <div class="t_haed">
        <div class="status flex_1"><span>魔法カード</span></div>
        <div class="cards_num_set"><span>20</span></div>
      </div>
      <div class="t_body">
    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">1</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">サイバネット・マイニング</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14301&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14301">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">2</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">斬機方程式</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14753&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14753">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">3</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">スモール・ワールド</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=16555&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="16555">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">4</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">転生炎獣の聖域</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13938&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13938">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    フィールド魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple semi_limited">
            <div class="card_count">
              <span class="row_num">5</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">墓穴の指名者</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13619&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13619">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    速攻魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple limited">
            <div class="card_count">
              <span class="row_num">6</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">抹殺の指名者</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14627&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14627">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    速攻魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">7</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">アームズ・ホール</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=7493&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="7493">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">8</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_spell.png" alt="魔法" title="魔法" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">アームド・チェンジャー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=6524&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="6524">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_spell.png" alt="魔法" title="魔法">
                    魔法
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    装備魔法
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


    
      </div>
  
  
  



  
  
      <div class="t_haed">
        <div class="status flex_1"><span>罠カード</span></div>
        <div class="cards_num_set"><span>14</span></div>
      </div>
      <div class="t_body">
    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">1</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">強制脱出装置</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=5914&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="5914">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
                    罠
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常罠
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">2</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">無限泡影</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13631&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13631">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
                    罠
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常罠
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">3</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">斬機超階乗</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14755&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14755">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
                    罠
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    通常罠
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">4</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">サイバネット・コンフリクト</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13878&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13878">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
                    罠
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    カウンター罠
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>3</span>
            </div>
          </div><!-- .t_row -->


    
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">5</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_trap.png" alt="罠" title="罠" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">神の警告</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=9008&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="9008">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_trap.png" alt="罠" title="罠">
                    罠
                  </span>
                </div><!-- .item_set -->
    
          
                <div class="flex_3 other">
                  <span>
                    【
                    カウンター罠
                    】
                  </span>
          
    
    
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


    
      </div>
  
    </div><!-- .list -->

  </div>
  







  
  <div id="detailtext_ext" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
      <div class="top">
        <h3>エクストラデッキ</h3>
        <span>15</span>
  
      </div>
    </div>

    <div id="main_m_list" class="list">
      <div class="t_body">
  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">1</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">塊斬機ラプラシアン</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14752&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14752">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
                    地属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->エクシーズ／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
      
        
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
                    ランク
        
        

                    &nbsp;4
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2000
                    </span>
      
      
                    <span class="">
                      守備力/
        
        
                          0
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">2</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">塊斬機ダランベルシアン</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14800">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
                    地属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->エクシーズ／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
      
        
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
                    ランク
        
        

                    &nbsp;4
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2000
                    </span>
      
      
                    <span class="">
                      守備力/
        
        
                          0
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">3</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">リンク・スパイダー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13034&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13034">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
                    地属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link2.png" alt="リンク" title="リンク">
                    リンク&nbsp;1
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/1000
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">4</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">転生炎獣ベイルリンクス</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14249&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14249">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
                    炎属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link2.png" alt="リンク" title="リンク">
                    リンク&nbsp;1
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/500
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">5</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">転生炎獣アルミラージ</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14338&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14338">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
                    炎属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link3.png" alt="リンク" title="リンク">
                    リンク&nbsp;1
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/0
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">6</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">コード・トーカー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13460&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13460">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
                    闇属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link82.png" alt="リンク" title="リンク">
                    リンク&nbsp;2
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/1300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">7</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">アップデートジャマー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14122&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14122">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_wind.png" alt="風属性" title="風属性">
                    風属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link84.png" alt="リンク" title="リンク">
                    リンク&nbsp;2
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2000
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">8</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">スプラッシュ・メイジ</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=15034&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="15034">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_water.png" alt="水属性" title="水属性">
                    水属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link93.png" alt="リンク" title="リンク">
                    リンク&nbsp;2
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/1100
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">9</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">トランスコード・トーカー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13698&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13698">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
                    地属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link862.png" alt="リンク" title="リンク">
                    リンク&nbsp;3
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>2</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">10</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">デコード・トーカー・ヒートソウル</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14962&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14962">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_fire.png" alt="炎属性" title="炎属性">
                    炎属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link813.png" alt="リンク" title="リンク">
                    リンク&nbsp;3
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">11</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">ファイアウォール・ドラゴン</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=13082&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="13082">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
                    光属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link8462.png" alt="リンク" title="リンク">
                    リンク&nbsp;4
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2500
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">12</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">アクセスコード・トーカー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=15032&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="15032">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
                    闇属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link8462.png" alt="リンク" title="リンク">
                    リンク&nbsp;4
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
      </div>
    </div><!-- #card_list.list -->

  </div>
  






  
  <div id="detailtext_side" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
      <div class="top">
        <h3>サイドデッキ</h3>
        <span>3</span>
  
      </div>
    </div>

    <div id="main_m_list" class="list">
      <div class="t_body">
  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">1</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_xyz.png" alt="エクシーズ/モンスター" title="エクシーズ/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">塊斬機ダランベルシアン</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14800">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_earth.png" alt="地属性" title="地属性">
                    地属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->エクシーズ／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
      
        
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/icon_rank.png" alt="ランク" title="ランク">
                    ランク
        
        

                    &nbsp;4
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/2000
                    </span>
      
      
                    <span class="">
                      守備力/
        
        
                          0
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">2</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">リングリボー</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14904&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14904">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_dark.png" alt="闇属性" title="闇属性">
                    闇属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link1.png" alt="リンク" title="リンク">
                    リンク&nbsp;1
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
        



          <div class="t_row c_simple ">
            <div class="card_count">
              <span class="row_num">3</span>
            </div>
            <div class="inside">
              
              <div class="card_name flex_1">

          

                <img src="external/image/parts/card/card_icon_link.png" alt="リンク/モンスター" title="リンク/モンスター" class="ui-draggable ui-draggable-handle" style="position: relative;">
          
          
                
                <span class="name">コード・トーカー・インヴァート</span>
                <input type="hidden" class="link_value" value="/yugiohdb/card_search.action?ope=2&amp;cid=14542&amp;request_locale=ja">
        
              </div>
              <div class="remove_btn ">
                <a href="javascript:void(0);" class="btn hex red" title="このカードをリストから削除">
                  <span>X</span>
                  <input type="hidden" class="lang" value="ja">
                  <input type="hidden" class="cid" value="14542">
                </a>
              </div>
              <div class="element">
                <div class="item_set ">
                  <span>
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/attribute/attribute_icon_light.png" alt="光属性" title="光属性">
                    光属性
                  </span>
                </div><!-- .item_set -->
    
    


                <div class="flex_2 other">
                  <span>
                    【
                    サイバース族<!--
            
                     -->／<!--
                     -->リンク／効果<!--
            
            
            
                     -->】
                  </span>
                </div><!-- .other -->

                <div class="num_set flex_1">
                  <span>
      
                    <img class="icon_img ui-draggable ui-draggable-handle" src="external/image/parts/link_pc/link46.png" alt="リンク" title="リンク">
                    リンク&nbsp;2
      
      
                  </span>

                  <span class="">
    

                  </span>

                  <div class="">
      
                    <span class="">
                      攻撃力/1300
                    </span>
      
      
                    <span class="">
                      守備力/
        
                          -
        
        
                    </span>
      
                  </div>

  
                </div><!-- .other or .num_set -->
              </div><!-- .element -->
            </div><!-- .inside -->
            
            <div class="cards_num_set">
              <span>1</span>
            </div>
          </div><!-- .t_row -->


  
      </div>
    </div><!-- #card_list.list -->

  </div>
  
  </div>




      <div id="deck_image" style="display: block;">

    



  <div id="main" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
      <div class="top">
        <h3>メインデッキ</h3>
        <span>40</span>
      </div>
    </div>

    
    <div class="image_set">
  
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13571&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_monster_0_1 ui-draggable ui-draggable-handle" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13571&amp;ciid=1&amp;enc=4Mp-kHZoU5G8AmEG5-_lBg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13571&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_monster_0_1 ui-draggable ui-draggable-handle" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13571&amp;ciid=1&amp;enc=4Mp-kHZoU5G8AmEG5-_lBg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13571&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_monster_0_1 ui-draggable ui-draggable-handle" alt="夢幻崩界イヴリース" title="夢幻崩界イヴリース" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13571&amp;ciid=1&amp;enc=4Mp-kHZoU5G8AmEG5-_lBg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=17430&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_monster_1_1 ui-draggable ui-draggable-handle" alt="斬機サーキュラー" title="斬機サーキュラー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=17430&amp;ciid=1&amp;enc=QF5Ab2yaHTaaC0wF6ydPiQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=17430&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_monster_1_1 ui-draggable ui-draggable-handle" alt="斬機サーキュラー" title="斬機サーキュラー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=17430&amp;ciid=1&amp;enc=QF5Ab2yaHTaaC0wF6ydPiQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=17430&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_monster_1_1 ui-draggable ui-draggable-handle" alt="斬機サーキュラー" title="斬機サーキュラー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=17430&amp;ciid=1&amp;enc=QF5Ab2yaHTaaC0wF6ydPiQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  

  
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14301&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_0_1 ui-draggable ui-draggable-handle" alt="サイバネット・マイニング" title="サイバネット・マイニング" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14301&amp;ciid=1&amp;enc=eKqWv3RZUlLbRgj2UIOcEw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14301&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_0_1 ui-draggable ui-draggable-handle" alt="サイバネット・マイニング" title="サイバネット・マイニング" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14301&amp;ciid=1&amp;enc=eKqWv3RZUlLbRgj2UIOcEw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14301&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_spell_0_1 ui-draggable ui-draggable-handle" alt="サイバネット・マイニング" title="サイバネット・マイニング" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14301&amp;ciid=1&amp;enc=eKqWv3RZUlLbRgj2UIOcEw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14753&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_1_1 ui-draggable ui-draggable-handle" alt="斬機方程式" title="斬機方程式" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14753&amp;ciid=1&amp;enc=hEVU1Z6Vxzh7k3daV-CWlQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14753&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_1_1 ui-draggable ui-draggable-handle" alt="斬機方程式" title="斬機方程式" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14753&amp;ciid=1&amp;enc=hEVU1Z6Vxzh7k3daV-CWlQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14753&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_spell_1_1 ui-draggable ui-draggable-handle" alt="斬機方程式" title="斬機方程式" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14753&amp;ciid=1&amp;enc=hEVU1Z6Vxzh7k3daV-CWlQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=16555&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_2_1 ui-draggable ui-draggable-handle" alt="スモール・ワールド" title="スモール・ワールド" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=16555&amp;ciid=1&amp;enc=iVMSFkScU-fjDqNLnPehag&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=16555&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_2_1 ui-draggable ui-draggable-handle" alt="スモール・ワールド" title="スモール・ワールド" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=16555&amp;ciid=1&amp;enc=iVMSFkScU-fjDqNLnPehag&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=16555&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_spell_2_1 ui-draggable ui-draggable-handle" alt="スモール・ワールド" title="スモール・ワールド" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=16555&amp;ciid=1&amp;enc=iVMSFkScU-fjDqNLnPehag&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13938&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_3_1 ui-draggable ui-draggable-handle" alt="転生炎獣の聖域" title="転生炎獣の聖域" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13938&amp;ciid=1&amp;enc=skW_u1Fh9fSjERjVP3R9pQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13938&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_3_1 ui-draggable ui-draggable-handle" alt="転生炎獣の聖域" title="転生炎獣の聖域" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13938&amp;ciid=1&amp;enc=skW_u1Fh9fSjERjVP3R9pQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13938&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_spell_3_1 ui-draggable ui-draggable-handle" alt="転生炎獣の聖域" title="転生炎獣の聖域" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13938&amp;ciid=1&amp;enc=skW_u1Fh9fSjERjVP3R9pQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13619&amp;request_locale=ja">
        
          
          
            <span class=" semi_limited">
            <img class="card_image_spell_4_1 ui-draggable ui-draggable-handle" alt="墓穴の指名者" title="墓穴の指名者" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13619&amp;ciid=1&amp;enc=diw-7xfIox8Qjat1B7yuOQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13619&amp;request_locale=ja">
        
        
          
          
            <span class=" semi_limited">
            <img class="card_image_spell_4_1 ui-draggable ui-draggable-handle" alt="墓穴の指名者" title="墓穴の指名者" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13619&amp;ciid=1&amp;enc=diw-7xfIox8Qjat1B7yuOQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14627&amp;request_locale=ja">
        
          
          
            <span class=" limited">
            <img class="card_image_spell_5_1 ui-draggable ui-draggable-handle" alt="抹殺の指名者" title="抹殺の指名者" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14627&amp;ciid=1&amp;enc=zKQ4xQyAG_Gqp9XOrwth_A&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=7493&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_6_1 ui-draggable ui-draggable-handle" alt="アームズ・ホール" title="アームズ・ホール" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=7493&amp;ciid=1&amp;enc=lE4aw0FCFXSt3sdyZSo5Bg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=7493&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_6_1 ui-draggable ui-draggable-handle" alt="アームズ・ホール" title="アームズ・ホール" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=7493&amp;ciid=1&amp;enc=lE4aw0FCFXSt3sdyZSo5Bg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=7493&amp;request_locale=ja">
        
        
        
          
          
            <span>
            <img class="card_image_spell_6_1 ui-draggable ui-draggable-handle" alt="アームズ・ホール" title="アームズ・ホール" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=7493&amp;ciid=1&amp;enc=lE4aw0FCFXSt3sdyZSo5Bg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=6524&amp;request_locale=ja">
        
          
          
            <span>
            <img class="card_image_spell_7_1 ui-draggable ui-draggable-handle" alt="アームド・チェンジャー" title="アームド・チェンジャー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=6524&amp;ciid=1&amp;enc=o1shmrowuYfBP5yde57ynQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=6524&amp;request_locale=ja">
        
        
          
          
            <span>
            <img class="card_image_spell_7_1 ui-draggable ui-draggable-handle" alt="アームド・チェンジャー" title="アームド・チェンジャー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=6524&amp;ciid=1&amp;enc=o1shmrowuYfBP5yde57ynQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  

  
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=5914&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_trap_0_1 ui-draggable ui-draggable-handle" alt="強制脱出装置" title="強制脱出装置" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=5914&amp;ciid=1&amp;enc=KXIN7gIpf-qauKs9iEtt2A&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=5914&amp;request_locale=ja">

        
        
          
          
            <span>
            <img class="card_image_trap_0_1 ui-draggable ui-draggable-handle" alt="強制脱出装置" title="強制脱出装置" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=5914&amp;ciid=1&amp;enc=KXIN7gIpf-qauKs9iEtt2A&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=5914&amp;request_locale=ja">

        
        
        
          
          
            <span>
            <img class="card_image_trap_0_1 ui-draggable ui-draggable-handle" alt="強制脱出装置" title="強制脱出装置" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=5914&amp;ciid=1&amp;enc=KXIN7gIpf-qauKs9iEtt2A&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13631&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_trap_1_1 ui-draggable ui-draggable-handle" alt="無限泡影" title="無限泡影" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13631&amp;ciid=1&amp;enc=GNP_kIy6vDlGQ3wGgRb3wg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13631&amp;request_locale=ja">

        
        
          
          
            <span>
            <img class="card_image_trap_1_1 ui-draggable ui-draggable-handle" alt="無限泡影" title="無限泡影" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13631&amp;ciid=1&amp;enc=GNP_kIy6vDlGQ3wGgRb3wg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13631&amp;request_locale=ja">

        
        
        
          
          
            <span>
            <img class="card_image_trap_1_1 ui-draggable ui-draggable-handle" alt="無限泡影" title="無限泡影" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13631&amp;ciid=1&amp;enc=GNP_kIy6vDlGQ3wGgRb3wg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14755&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_trap_2_1 ui-draggable ui-draggable-handle" alt="斬機超階乗" title="斬機超階乗" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14755&amp;ciid=1&amp;enc=-8Likk9Nlg-63giBwYaogQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14755&amp;request_locale=ja">

        
        
          
          
            <span>
            <img class="card_image_trap_2_1 ui-draggable ui-draggable-handle" alt="斬機超階乗" title="斬機超階乗" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14755&amp;ciid=1&amp;enc=-8Likk9Nlg-63giBwYaogQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14755&amp;request_locale=ja">

        
        
        
          
          
            <span>
            <img class="card_image_trap_2_1 ui-draggable ui-draggable-handle" alt="斬機超階乗" title="斬機超階乗" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14755&amp;ciid=1&amp;enc=-8Likk9Nlg-63giBwYaogQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13878&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_trap_3_1 ui-draggable ui-draggable-handle" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13878&amp;ciid=1&amp;enc=tHtWCS9qQ21aY_eKHBVAiA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13878&amp;request_locale=ja">

        
        
          
          
            <span>
            <img class="card_image_trap_3_1 ui-draggable ui-draggable-handle" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13878&amp;ciid=1&amp;enc=tHtWCS9qQ21aY_eKHBVAiA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13878&amp;request_locale=ja">

        
        
        
          
          
            <span>
            <img class="card_image_trap_3_1 ui-draggable ui-draggable-handle" alt="サイバネット・コンフリクト" title="サイバネット・コンフリクト" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13878&amp;ciid=1&amp;enc=tHtWCS9qQ21aY_eKHBVAiA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=9008&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_trap_4_1 ui-draggable ui-draggable-handle" alt="神の警告" title="神の警告" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=9008&amp;ciid=1&amp;enc=YoWuM7VNM10h5Zp4J74p_w&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=9008&amp;request_locale=ja">

        
        
          
          
            <span>
            <img class="card_image_trap_4_1 ui-draggable ui-draggable-handle" alt="神の警告" title="神の警告" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=9008&amp;ciid=1&amp;enc=YoWuM7VNM10h5Zp4J74p_w&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  

    </div>

  </div><!--#main-->

<!-- -->

  <div id="extra" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
      <div class="top">
        <h3>エクストラデッキ</h3>
        <span>15</span>
      </div>
    </div>

    <div class="image_set">
  
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14752&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_0_1 ui-draggable ui-draggable-handle" alt="塊斬機ラプラシアン" title="塊斬機ラプラシアン" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14752&amp;ciid=1&amp;enc=MyVu56tUC4oxGA7fZQTeHA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_1_1 ui-draggable ui-draggable-handle" alt="塊斬機ダランベルシアン" title="塊斬機ダランベルシアン" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14800&amp;ciid=1&amp;enc=u_nVY2UkC0dUvcFYh23FhA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13034&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_2_1 ui-draggable ui-draggable-handle" alt="リンク・スパイダー" title="リンク・スパイダー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13034&amp;ciid=1&amp;enc=BBMQTHLvAxC72VC8PbGTvw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14249&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_3_1 ui-draggable ui-draggable-handle" alt="転生炎獣ベイルリンクス" title="転生炎獣ベイルリンクス" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14249&amp;ciid=1&amp;enc=qmd0pcUnBQXTPIXsGVjlZw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14249&amp;request_locale=ja">
        
        
          
          
            <span>

            <img class="card_image_extra_3_1 ui-draggable ui-draggable-handle" alt="転生炎獣ベイルリンクス" title="転生炎獣ベイルリンクス" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14249&amp;ciid=1&amp;enc=qmd0pcUnBQXTPIXsGVjlZw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14338&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_4_1 ui-draggable ui-draggable-handle" alt="転生炎獣アルミラージ" title="転生炎獣アルミラージ" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14338&amp;ciid=1&amp;enc=MO4r0tjPhynLtnfy68AVaw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13460&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_5_1 ui-draggable ui-draggable-handle" alt="コード・トーカー" title="コード・トーカー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13460&amp;ciid=1&amp;enc=r51L46PP0F1Hhn5XbdIkww&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14122&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_6_1 ui-draggable ui-draggable-handle" alt="アップデートジャマー" title="アップデートジャマー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14122&amp;ciid=1&amp;enc=UjSpu_jmocbM1pvH3TrgsA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=15034&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_7_1 ui-draggable ui-draggable-handle" alt="スプラッシュ・メイジ" title="スプラッシュ・メイジ" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=15034&amp;ciid=1&amp;enc=J3jhN5NFlU0H8mJSSFvWYQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=15034&amp;request_locale=ja">
        
        
          
          
            <span>

            <img class="card_image_extra_7_1 ui-draggable ui-draggable-handle" alt="スプラッシュ・メイジ" title="スプラッシュ・メイジ" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=15034&amp;ciid=1&amp;enc=J3jhN5NFlU0H8mJSSFvWYQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13698&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_8_1 ui-draggable ui-draggable-handle" alt="トランスコード・トーカー" title="トランスコード・トーカー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13698&amp;ciid=1&amp;enc=3LsccTlxzA4ckR1VHhE5rg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13698&amp;request_locale=ja">
        
        
          
          
            <span>

            <img class="card_image_extra_8_1 ui-draggable ui-draggable-handle" alt="トランスコード・トーカー" title="トランスコード・トーカー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13698&amp;ciid=1&amp;enc=3LsccTlxzA4ckR1VHhE5rg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14962&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_9_1 ui-draggable ui-draggable-handle" alt="デコード・トーカー・ヒートソウル" title="デコード・トーカー・ヒートソウル" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14962&amp;ciid=1&amp;enc=OlNxTfT7jJQZosZo-2SkhQ&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=13082&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_10_1 ui-draggable ui-draggable-handle" alt="ファイアウォール・ドラゴン" title="ファイアウォール・ドラゴン" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=13082&amp;ciid=1&amp;enc=voYX8-89zJtbQv82-9LugA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=15032&amp;request_locale=ja">
        
          
          
            <span>

            <img class="card_image_extra_11_1 ui-draggable ui-draggable-handle" alt="アクセスコード・トーカー" title="アクセスコード・トーカー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=15032&amp;ciid=1&amp;enc=w7j6BmFBc2iOiY0--hPaUw&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    </div>

  </div><!--#extra-->




  <div id="side" class="card_set">
    <div class="subcatergory">
      <div class="icon hex"><span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43 54"><defs></defs><path d="M34.5,57V13.5L51.5,9V48.5Zm-2-20-24-9.5V7.5L28.5,3,51,7,32.5,12.5Zm0,20-21-8.8v-17l21,8.3Z" transform="translate(-8.5 -3)"></path></svg></span></div>
      <div class="top">
        <h3>サイドデッキ</h3>
        <span>3</span>
      </div>
    </div>

    <div class="image_set">
  
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14800&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_side_0_1 ui-draggable ui-draggable-handle" alt="塊斬機ダランベルシアン" title="塊斬機ダランベルシアン" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14800&amp;ciid=1&amp;enc=u_nVY2UkC0dUvcFYh23FhA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14904&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_side_1_1 ui-draggable ui-draggable-handle" alt="リングリボー" title="リングリボー" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14904&amp;ciid=1&amp;enc=F6fcPMqoCYfgnIXO0G1lHA&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    
      <a target="_blank" href="/yugiohdb/card_search.action?ope=2&amp;cid=14542&amp;request_locale=ja">

        
          
          
            <span>
            <img class="card_image_side_2_1 ui-draggable ui-draggable-handle" alt="コード・トーカー・インヴァート" title="コード・トーカー・インヴァート" src="/yugiohdb/get_image.action?type=1&amp;lang=ja&amp;cid=14542&amp;ciid=1&amp;enc=Vkx-oXbBI_oMi6rpDuY3Zg&amp;osplang=1" style="position: relative;">
            <div><span></span></div></span>
          
        
        
        
      </a>
      
    
  
    </div>

  </div><!--#side-->


      </div>


  
      <div id="btnarea_cd">
        
        <a onclick="return DeckDelete()" class="btn hex red"><span>デッキを削除</span></a>
      </div>
  

    </div><!--#article_body-->

  </article>






  </div><!--#bg--></div><!--#main980-->

  

  
    <nav id="title_top_msg" class="nav_home"><div class="in_bg">
      <div class="title_btn">
        <span class="title">遊戯王 OCG デュエルモンスターズ カードデータベースとは</span>
        <div class="batu"><span>∧</span></div>
      </div>
      <div class="in">
        <div class="in_btn">
          <p>遊戯王 オフィシャルカードゲーム デュエルモンスターズの公式サイトです。<br>全ての遊戯王OCGカードを検索したり、詳細なルールや禁止・制限カードを参照する事ができます。<br>また、自分が持っているカードやデッキをマイデッキに登録して管理したり、公開されているデッキレシピを検索して自分のデッキ構築の参考にする事ができます。</p>
          <a class="btn" href="https://www.yugioh-card.com/japan/howto/" target="_blank">
            <img src="external/image/ja/logo_ocgtcg.png" class="ui-draggable ui-draggable-handle" style="position: relative;">
            <span>遊び方はこちら</span>
          </a>
        </div>


        <div id="nav_bottom">
          
          <a class="top_main_card_search" href="/yugiohdb/card_search.action">
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"></stop><stop offset="1" stop-color="#fff"></stop></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"></path></svg></span>
              <h3>カード検索</h3>
            </div>
            <div class="tex_bottom">
              遊戯王OCGの全てのカードを検索することができます。カードの詳細画面から、そのカードを使用したデッキ検索をすることができます。公開日よりカード検索ができるようになります。
            </div>
          </a>

          
          <a class="top_main_cardlist" href="/yugiohdb/card_list.action">
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"></path></svg></span>
              <h3>カードリスト</h3>
            </div>
            <div class="tex_bottom">
              遊戯王OCGカードを、収録べつ(商品/特典など)に閲覧することができます。<br>商品の公開日より最新情報として掲載しています。
            </div>
          </a>

          
          <a class="top_main_decks" href="/yugiohdb/deck_search.action">
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"></path></svg></span>
              <h3>デッキ検索</h3>
            </div>
            <div class="tex_bottom">
              公開されているデッキを検索することができます。<br>大会優勝デッキ/大会入賞デッキの検索や、特定カードを使用しているデッキの検索ができます。
            </div>
          </a>


          
    
          <a class="top_trends" href="/yugiohdb/trends_search.action?ope=1">
      
      
            <div class="tex_top">
              <span class="icon"><!--?xml version="1.0" encoding="UTF-8"?--><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g><g><path d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"></path></g></g></svg></span>
              <h3>トレンド</h3>
            </div>
            <div class="tex_bottom">
              新たに制作されたデッキや、大会で使用されたデッキを元に算出されたランキングです<br>現在注目されているデッキの傾向をチェックすることができます。
            </div>
          </a>

          
            
            
            
            
          <a class="top_main_my menu_my_decks" href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">
            
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"></path></svg></span>
              <h3>マイデッキ</h3>

            </div>
            <div class="tex_bottom">
              デッキレシピの登録や登録したデッキを他のユーザに公開できます(ハーフデッキやデュエルリンクスのデッキも登録できます)。自分のデッキやカードの管理の使用にもおすすめの機能です。
            </div>
          </a>

          
            
            
            
            
          <a class="top_main_my my_cardlist" href="/yugiohdb/member_have_want_card.action">
            
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"></path></svg></span>
              <h3>マイカードリスト</h3>
            </div>
            <div class="tex_bottom">
              自分の持っているカードや欲しいカードをリストとして管理することができます。ログイン後にカード詳細画面から追加できます。
            </div>
          </a>



        

          
          <a class="top_main_q_a" href="/yugiohdb/faq_search.action">
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"></path></svg></span>
              <h3>Ｑ＆Ａ</h3>

            </div>
            <div class="tex_bottom">
              遊戯王カードゲーム事務局によせられた質問と回答をカード名などで検索ができます。最新カードのルール等も随時更新しています。
            </div>
          </a>
        
          
          <a class="top_main_forbidden" href="/yugiohdb/forbidden_limited.action">
            <div class="tex_top">
              <span class="icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 35.32"><defs></defs><path d="M26.09,16v3.57a10.85,10.85,0,0,0,.16-1.8A10.5,10.5,0,0,0,26.09,16Zm0,17.94H18a17,17,0,0,1-5.6,0H4.15V30a17.58,17.58,0,0,1-1.37-1.36v6.67H27.46V28.8a17.2,17.2,0,0,1-1.37,1.33ZM23.35,23.08V13.74L22,15.1v6.62H15.26l-1.37,1.36ZM4.15,1.35H26.09V5.44a14.34,14.34,0,0,1,1.37,1.33V0H2.78V6.93A17.71,17.71,0,0,1,4.15,5.56Zm0,16.83v0ZM8.26,9.25a10.62,10.62,0,0,0-1.38,1.3V22.36L8.26,21Zm6.92,23.58A15,15,0,1,0,0,17.83a15,15,0,0,0,15.19,15Zm12.54-15A12.56,12.56,0,0,1,7.47,27.55L25.06,10.13a12.29,12.29,0,0,1,2.67,7.65ZM15.19,5.37a12.54,12.54,0,0,1,8,2.82L5.5,25.65a12.3,12.3,0,0,1-2.84-7.87A12.47,12.47,0,0,1,15.19,5.37Z" transform="translate(0.01)"></path></svg></span>
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
    <div id="content_copyright">©スタジオ・ダイス／集英社・テレビ東京・KONAMI</div>

    <div id="cdb_link_set"><a class="link_ocg" href="//www.yugioh-card.com/japan/" target="_blank">遊戯王公式サイト</a> <a class="link_neuron" href="//www.konami.com/yugioh/neuron/ja/" target="_blank">遊戯王ニューロン</a> <a class="link_cgn" href="//cardgame-network.konami.net/" target="_blank">KONAMI CARD GAME NETWORK</a> <a class="link_kst" href="http://www.konamistyle.jp/" target="_blank">コナミスタイル</a> <a class="link_kfs" href="https://www.konami.com/games/card/friendly_shop/" target="_blank">コナミ フレンドリーショップ</a> <a class="link_rushdb" href="https://www.db.yugioh-card.com/rushdb/" target="_blank">遊戯王ラッシュデュエルカードデータベース</a> <a class="link_tiktok" href="https://www.tiktok.com/@yugioh_cardgame_official?is_from_webapp=1&amp;sender_device=pc" target="_blank">「遊戯王カードゲーム」公式TikTok</a></div>
    <div id="footer_menu">
      


        <ul class="main_menu">
          
          <li class="menu_top"><a href="/yugiohdb/"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"></path></svg><h3>Top</h3></a></li>

          
          <li class="menu_card_search">
            <a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 41.81 40.37"><defs><linearGradient x1="2.97" y1="24.1" x2="44.78" y2="24.1" gradientTransform="matrix(1, 0, 0, -1, 0, 46)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff"></stop><stop offset="1" stop-color="#fff"></stop></linearGradient></defs><path d="M23.54,39.8l-19-2.53,3.9-28.8,5.92.79A12.89,12.89,0,0,1,15,8l-7.73-1L3,38.44l21.75,2.89,1.6-11.79c-.46-.05-.91-.12-1.36-.21ZM13.17,14q0-.67.15-1.35l-4-.53-2.45,18,16.32,2.16L23.62,29c-.45-.13-.89-.29-1.32-.46L22,30.83,8.4,29l2.08-15.34ZM38.06,27.58l-1.19.67-1.31-2.31a13.22,13.22,0,0,0,4-17.43,13.51,13.51,0,0,0-18.3-5.09,13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.31,2.32-1.19.66L40,42.08l4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,22,4.59,12.14,12.14,0,0,1,38.41,9.17,11.9,11.9,0,0,1,33.79,25.46ZM22.36,5.74A10.56,10.56,0,0,0,20.74,6.9l14.5,1.92L33.13,24.45l.07,0a10.93,10.93,0,0,0,1.44-1l2-14.78a12.34,12.34,0,0,0-1-1.16ZM17,15.77l11.09,1.47L27,25.76a10.59,10.59,0,0,0,1.38,0l1.31-9.7L17,14.4A10.44,10.44,0,0,0,17,15.77Z" transform="translate(-2.97 -1.71)"></path></svg><h3>カード検索</h3></a>

          </li>

          
          <li class="menu_cardlist sab_menu">
            <a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1ZM14.73,1.7l-.15,1.77,4.68-1.41ZM37.53,9l-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45Z" transform="translate(-1.82 -1.7)"></path></svg><h3>カードリスト</h3></a>
            <ul>
              <li><a href="/yugiohdb/card_list.action?clm=3">公開日の新しい順</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=1">一般商品</a></li>
              <li><a href="/yugiohdb/card_list.action?clm=2">特典・同梱系</a></li>
        
              <li><a href="/yugiohdb/card_calendar.action">カード誕生日</a></li>
        
            </ul>
          </li>

          
          <li class="menu_decks">
            <a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.78 40.37"><defs></defs><path d="M25.51,37.66l-9.6,1.07V21.24a14.24,14.24,0,0,1-1.37-5.19V28.73L2.74,26.8V13.48l11.78-1.3.26,0c.09-.44.2-.89.33-1.32l-.56-.09L1.37,12.27V28l1.37.22v10l12.12,2,12-1.33V29.43c-.46-.08-.92-.17-1.37-.29Zm-11,1.12L4.11,37.08V28.4l10.43,1.71Zm24.89-11.2-1.19.67-1.31-2.31A13.22,13.22,0,0,0,41,8.51,13.52,13.52,0,0,0,22.66,3.42a13.25,13.25,0,0,0-5.14,18.12,13.51,13.51,0,0,0,17,5.72l1.32,2.32-1.2.66,6.71,11.84,4.79-2.66Zm-4.27-2.12a12.14,12.14,0,0,1-16.45-4.58A11.9,11.9,0,0,1,23.33,4.59,12.14,12.14,0,0,1,39.78,9.17,11.9,11.9,0,0,1,35.16,25.46ZM20.22,9l12.64,2.07L22.22,12.26v11a10.93,10.93,0,0,0,1.37,1V13.47L36.48,12v11a9.86,9.86,0,0,0,1.37-1.45V10.52L21.19,7.79A10.18,10.18,0,0,0,20.22,9Z" transform="translate(-1.37 -1.71)"></path></svg><h3>デッキ検索</h3></a>
          </li>
        </ul>
          
          <div class="logo"><a href="/yugiohdb/"><h1>遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース</h1></a></div>

        <ul class="main_menu">

          
      

          <li class="menu_trends sab_menu">
            <a class="bg main" href="/yugiohdb/trends_search.action?ope=1"><!--?xml version="1.0" encoding="UTF-8"?--><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.46"><defs></defs><g><g><path d="M21.64,12.46l-11,1v15l1,.17v7.92l11,1.92h1l9-1V14.46l-10-2h-1Zm1,24.91l-10-1.83v-6.75l10,1.67v6.91Zm9-.91l-8,.89V16.46l8-.89v20.89ZM22.64,15.46v13.83l-11-1.83V14.46l10.31-.94,6.47,1.29-5.79,.64ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"></path></g></g></svg><h3>トレンド</h3></a>
            <ul>
              
              <li><a href="/yugiohdb/trends_search.action?ope=1">人気デッキランキング</a></li>
              
              <li><a href="/yugiohdb/trends_search.action?ope=2">注目カテゴリーランキング</a></li>
            </ul>
          </li>
      
      



  
  
  
  
        

          
          <li class="my menu_my_decks sab_menu">
            <a class="main" href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.17 35.12"><defs></defs><path d="M23.37,5.39,9.05,7V26l1.37.21v11.9l15.09,2.25,1.37.15,12.34-1.37V7.75ZM25.51,39,11.8,36.94V26.41l13.71,2.05Zm0-29.7v17.8L10.42,24.83V8.19L23.34,6.76,34,8.35ZM37.85,37.92l-11,1.22V10.51l11-1.22Z" transform="translate(-9.05 -5.39)"></path></svg><h3>マイデッキ</h3></a>
            <ul>
              <li><a href="/yugiohdb/member_deck.action?ope=4&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">マイデッキ</a></li>
              <li><a href="/yugiohdb/member_deck.action?ope=21&amp;cgid=c8525f77e0268f9b1ba9110a8a05bc35">お気に入りデッキ</a></li>
            </ul>
          </li>

          
          <li class="my menu_my_cardlist sab_menu">
            <a class="main" href="/yugiohdb/member_have_want_card.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44.26 40.22"><defs></defs><path d="M22.81,2.41l-21,6.35L11.2,39.15l21-6.35ZM3.54,9.66,21.9,4.1l8.58,27.79L12.12,37.45ZM31.59,26.2l.41,0L33.47,8.1l-7.66-.61.43,1.39L32,9.34l-1.17,14.4ZM35.12,4.69,33,30.8l.89,2.9-3.68,1.11,3.81.31L36.6,3.44l-12.34-1,.43,1.4Zm.71,25.25-.22,2.65.72.23L42,15.49,37.12,14,37,15.34l3.23,1Zm1.7-21-.11,1.39,6.94,2.21-9,27.66-11.2-3.57-2.3.7,14.38,4.58,9.84-30.25ZM21.63,7.88,5.89,12.64,11.26,30,27,25.28Zm-14,5.66,13.12-4,4.57,14.81-13.12,4ZM14.73,1.7l-.15,1.77,4.68-1.41Z" transform="translate(-1.82 -1.7)"></path></svg><h3>マイカードリスト</h3></a>
            <ul>
              <li><a href="member_have_want_card.action?ope=1">持っているカードリスト</a></li>
              <li><a href="member_have_want_card.action?ope=2">欲しいカードリスト</a></li>
            </ul>
          </li>
  

        

          
          <li class="menu_q_a">
            <a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 31.52 35.31"><defs></defs><path d="M34.83,38.3H22.66l-4,1.3-.43-1.3H12.89V27.48l-1.37.44V39.65H36.2V20.9a9.68,9.68,0,0,1-1.37.51ZM15.63,21v6.46h.89l2.21-.72.19-.06a5.85,5.85,0,0,0,.78-.58H17V20.71A7,7,0,0,0,15.63,21Zm-3.58,3.92.84,2.51V22.66A3.5,3.5,0,0,0,12,24.61ZM12.89,5.7H25.57a10.85,10.85,0,0,1,7.91-.63,11.57,11.57,0,0,1,2.73,1.19V4.35H11.52V17.13a10.32,10.32,0,0,1,1.37-.69ZM17,15.51V11.14h4.28l.4-1.35H15.63v5.86A12.87,12.87,0,0,1,17,15.51ZM31.4,16.58l.19.05h.5V10.09l-.1,0c-2-.59-4-.15-4.95,1l0,.1h3.71v5.24Zm-.13,5.24-.1.35-.45,1.5v2.4H30l-.4,1.36h2.48v-5.6Zm3.56-10v3.83a2.41,2.41,0,0,0,.73-1.13A2.9,2.9,0,0,0,34.83,11.83ZM33.11,6.32A8.68,8.68,0,0,0,24,8.63a5.08,5.08,0,0,0-1,1.54l-.39,1.3,2.63.77.39-1.3s0-.26.37-.72a6.12,6.12,0,0,1,6.37-1.45c3.19.93,5.18,3.68,4.45,6.13a4.49,4.49,0,0,1-3.56,2.93,4.3,4.3,0,0,1-2.26.05l-2.63-.77-1.55,5.21,2.63.77.78-2.6,0-.08c4.12.66,8-1.32,9-4.79C40.44,11.81,37.66,7.64,33.11,6.32ZM10.65,24.52c.17-2,1.88-3.95,4.4-4.78,3.16-1,6.37.1,7.19,2.53A4.44,4.44,0,0,1,21,26.69,4.2,4.2,0,0,1,19.16,28l-2.61.85L18.28,34l2.6-.85L20,30.58l0-.08c3.77-1.77,5.84-5.6,4.7-9-1.26-3.77-5.94-5.64-10.45-4.16-3.54,1.16-5.92,4-6.17,7a5.23,5.23,0,0,0,.08,1.82l.43,1.29,2.6-.85-.43-1.29A1.18,1.18,0,0,1,10.65,24.52Zm8.91,13.36L22.17,37l-.86-2.58-2.61.85Zm6.88-14.25-.77,2.6L28.3,27l.78-2.61Z" transform="translate(-8.04 -4.35)"></path></svg><h3>Ｑ＆Ａ</h3></a>
          </li>
        
          
          <li class="menu_forbidden">
            <a href="/yugiohdb/forbidden_limited.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 35.32"><defs></defs><path d="M26.09,16v3.57a10.85,10.85,0,0,0,.16-1.8A10.5,10.5,0,0,0,26.09,16Zm0,17.94H18a17,17,0,0,1-5.6,0H4.15V30a17.58,17.58,0,0,1-1.37-1.36v6.67H27.46V28.8a17.2,17.2,0,0,1-1.37,1.33ZM23.35,23.08V13.74L22,15.1v6.62H15.26l-1.37,1.36ZM4.15,1.35H26.09V5.44a14.34,14.34,0,0,1,1.37,1.33V0H2.78V6.93A17.71,17.71,0,0,1,4.15,5.56Zm0,16.83v0ZM8.26,9.25a10.62,10.62,0,0,0-1.38,1.3V22.36L8.26,21Zm6.92,23.58A15,15,0,1,0,0,17.83a15,15,0,0,0,15.19,15Zm12.54-15A12.56,12.56,0,0,1,7.47,27.55L25.06,10.13a12.29,12.29,0,0,1,2.67,7.65ZM15.19,5.37a12.54,12.54,0,0,1,8,2.82L5.5,25.65a12.3,12.3,0,0,1-2.84-7.87A12.47,12.47,0,0,1,15.19,5.37Z" transform="translate(0.01)"></path></svg><h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br>レギュレーション</span></h3></a>
          </li>
          <li class="menu_btn_pagetop"><a href="#"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"></path></svg></a></li>

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
            <button id="ot-sdk-btn" class="ot-sdk-show-settings">Cookie詳細設定</button>
            <!-- OneTrust Cookie 設定ボタンの終点 -->
          </li>
        </ul>
      </nav>
      <small>©2023 Konami Digital Entertainment</small>

    </div>
  </footer>
  <nav id="footer_icon">
    <div>
        <ul class="main_menu">
          
          <li class="menu_top"><a href="/yugiohdb/"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42.6 33.7"><path d="M23.4,0h-3.9L0,18l3.5,3.7,4.5-4.2,3,16.2H31.6l3-16.2,4.5,4.2,3.5-3.8L23.4,0Zm-1.8,25.6c-3.9,.1-7-3-7.1-6.9s3-7.1,6.9-7.1,7.1,3.2,7.1,7-3.1,7-6.9,7Z"></path></svg><h3>Top</h3></a></li>

          
          <li class="menu_card_search">
            <a class="main" href="/yugiohdb/card_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30.35 28.26"><defs></defs><path d="M13.44,23.3,2.21,21.64,3.93,10l3.52.52a11.1,11.1,0,0,1,.63-3.12l-5-.74-3,20.27,14,2.06,1.08-7.32a12.7,12.7,0,0,1-1.33-.53Zm-1.76-14,5.14.76-1.11,7.48a6.7,6.7,0,0,0,1.69.5L19.12,6.39,14,5.63a7,7,0,0,0-2.37,3.69ZM26.17,20l-.66.4L24.66,19a10,10,0,1,0-2.23,1.3l.85,1.44-.67.4,4.25,7.2,3.57-2.11Zm-3.73-2.21A7.82,7.82,0,1,1,25.2,7.1a7.83,7.83,0,0,1-2.76,10.71Z" transform="translate(-0.08 -1.07)"></path></svg><h3>カード検索</h3></a>

          </li>

          
          <li class="menu_cardlist sab_menu">
            <a class="bg main" href="/yugiohdb/card_list.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 33.07 29.79"><defs></defs><path d="M128.74,4.57l-1.11,13.66-1-.08,1.63,5.31-3.2,1,3.66.3,1.94-23.71L121.15.28l1.17,3.79ZM120.44,0,104.77,4.79l7,22.75,15.67-4.8Zm-9.06,21-4-13.11L120,4l4,13.1ZM131.13,5l-.31,3.78,4.33,1.43-4.3,13-1.18-.39-.25,3.06-7.08-.58-2.89.88,10.93,3.61,7.46-22.58Z" transform="translate(-104.77)"></path></svg><h3>カードリスト</h3></a>
          </li>

          
          <li class="menu_decks">
            <a href="/yugiohdb/deck_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 35.46 28.79"><defs></defs><path d="M452,16.6a11,11,0,0,1-1.39-7.34l-1.65.26V29l8.35-1.73V21.19A10.91,10.91,0,0,1,452,16.6ZM451.16,7l-4.78-.4-8.07,1-.18.61V19l10.09,1.74V9.52l.38-.73,2.12-.32A9.87,9.87,0,0,1,451.16,7ZM439,27.26,448.22,29V21.17L439,19.6Zm30.21-7.13-.69.4-.85-1.45a10.22,10.22,0,1,0-2.23,1.33l.86,1.46-.68.41L470,29.61l3.64-2.14Zm-3.77-2.27a8,8,0,1,1,2.78-11l0,.06A8,8,0,0,1,465.44,17.86Zm1-12-9.12-.75a7.16,7.16,0,0,0-2.07,9.51.83.83,0,0,1,.08.12V8.51l.51-1,10.67-1.63ZM456.25,15.92a7.14,7.14,0,0,0,10.09.27,7,7,0,0,0,.85-1V6.8L456.25,8.51Z" transform="translate(-438.13 -0.82)"></path></svg><h3>デッキ検索</h3></a>
          </li>
        
          <li class="menu_trends">
        
            <a href="/yugiohdb/trends_search.action?ope=1">
        
        
              <!--?xml version="1.0" encoding="UTF-8"?--><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 43.09 38.32"><defs></defs><g><g><path d="M11.92,36.35l10.8,1.97v-7.46l-10.8-1.8v7.29Zm11.88,1.95l8.64-.96V14.78l-8.64,.96v22.56Zm-1.82-25.73l-11.14,1.01v14.04l11.88,1.98V14.66l6.25-.69-6.99-1.4ZM0,9.12l7.77,4.53,.5-.86L.5,8.26l-.5,.86ZM5.2,4.3l3.1,3.93,.79-.62-3.1-3.93-.79,.62Zm37.39,3.96l-7.77,4.53,.5,.86,7.77-4.53-.5-.86Zm-5.48-4.57l-3.1,3.93,.79,.62,3.1-3.93-.79-.62ZM21.53,0l-4.06,5.49-7.28-2.81s-.04,.1,3.42,6.93c5.2-.75,10.62-.75,15.82,0,3.47-6.88,3.43-6.92,3.43-6.92l-7.29,2.81L21.53,0Z"></path></g></g></svg>
              <h3>トレンド</h3>
            </a>
          </li>


        

          
          <li class="menu_q_a">
            <a href="/yugiohdb/faq_search.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.73 27.45"><defs></defs><path d="M370.6,22.79A1.66,1.66,0,1,0,369,21.12v0A1.65,1.65,0,0,0,370.6,22.79Zm-10.11-5.65a1,1,0,0,0,.75-.63,1.82,1.82,0,0,0,.09-.8,2,2,0,0,1,0-.59,2.8,2.8,0,0,1,.2-.62,2.88,2.88,0,0,1,3.08-1.37,3.8,3.8,0,0,1,1.5.85,3.47,3.47,0,0,1,1,1.87,2,2,0,0,1,0,.69,3.28,3.28,0,0,1-.21.86A5.07,5.07,0,0,1,365,19.07c-.28.18-1,.52-1.11.81s.11.68.22.93l.95,2.1c.09.21.27.8.61.74a1.57,1.57,0,0,0,.54-.29c.18-.13.48-.25.57-.46a.6.6,0,0,0,0-.49,2.71,2.71,0,0,0-.21-.37c-.13-.21-.25-.42-.37-.63s-.3-.37-.15-.59a2.13,2.13,0,0,1,.65-.42l.42-.29a4.71,4.71,0,0,0,1.6-1.91,6.46,6.46,0,0,0,.36-1.21,4.79,4.79,0,0,0-.44-3,5.11,5.11,0,0,0-3.53-2.49,8.79,8.79,0,0,0-1.14-.11h-.58a10.28,10.28,0,0,0-1.08.21,4.51,4.51,0,0,0-2.93,2.87c-.28.72-.55,2,.12,2.46a1,1,0,0,0,.94.19Zm1.19-11.25H369l.09-.14a4.42,4.42,0,0,1,1.07-1,6.55,6.55,0,0,1,6.18-.87,6.31,6.31,0,0,1,2.37,1.57V1.76H360.21v10.4a4.46,4.46,0,0,1,1.47-1Zm17.9,2.2a6,6,0,0,0-6-4,5.86,5.86,0,0,0-3.45,1.41,3.37,3.37,0,0,0-.69.67,1.62,1.62,0,0,0-.3,1.57,1.21,1.21,0,0,0,.83.66c1.13.29,1.51-.82,2-1.39a2.14,2.14,0,0,1,.58-.46,2.75,2.75,0,0,1,.79-.33,3.64,3.64,0,0,1,4.29,3.19,3.87,3.87,0,0,1-.06,1.44,3.19,3.19,0,0,1-1.89,2.43,7.33,7.33,0,0,1-3.42.12,1.09,1.09,0,0,0-1.09.27,4.34,4.34,0,0,0-.27,1.13l-.51,2.53c-.11.47-.22.91.29,1h.62c1.29.21,1-.77,1.15-1.7.07-.4-.05-.73.28-.87a2,2,0,0,1,.9,0,5,5,0,0,0,1.44,0,7.09,7.09,0,0,0,1.21-.28A5.71,5.71,0,0,0,379,13.35,7.49,7.49,0,0,0,379.58,8.09ZM365.72,25.43A1.47,1.47,0,1,0,367.19,24a1.47,1.47,0,0,0-1.47,1.48Zm11.47-3.29h-4.6a2.22,2.22,0,0,1-4,0h-1.24a3.25,3.25,0,0,1,.11.42,1.26,1.26,0,0,1-.13.63,1.22,1.22,0,0,1-.2.25h0a2,2,0,1,1-2,2,2,2,0,0,1,.42-1.24.93.93,0,0,1-.29-.05c-.4-.13-.6-.64-.76-1l-.45-1h-2.44V16.91a1.65,1.65,0,0,1-1.47.87V29.21H378.6V14.76a5,5,0,0,1-1.47,1.06Z" transform="translate(-359.09 -1.76)"></path></svg><h3>Ｑ＆Ａ</h3></a>
          </li>
        
          
          <li class="menu_forbidden">
            <a href="/yugiohdb/forbidden_limited.action"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 25.28 27.73"><defs></defs><path d="M243.27,11.32v8.13A8.61,8.61,0,0,0,243.27,11.32Zm-7.69,12.75a8.69,8.69,0,0,0,5.69-2.13h-8.89l-1,1a8.61,8.61,0,0,0,4.2,1.13Zm7.12-20a10.13,10.13,0,0,1,1,.72h0c.33.26.65.53,1,.82h0c.16.15.3.31.46.47V1.71h-19.1V6A13.33,13.33,0,0,1,242.7,4.07ZM227.87,19.42h0V11.33a8.67,8.67,0,0,0,0,8.13Zm.18,7a13.32,13.32,0,0,1-2-1.67v4.64h19.1V24.71A13.38,13.38,0,0,1,228,26.43ZM235.58,28A12.64,12.64,0,1,0,222.94,15.4h0A12.66,12.66,0,0,0,235.58,28Zm9.63-12.64A9.65,9.65,0,0,1,235.58,25a9.52,9.52,0,0,1-5.46-1.71L243.23,9.56a9.57,9.57,0,0,1,2,5.8Zm-9.63-9.69a9.65,9.65,0,0,1,5.47,1.71L227.93,21.17a9.63,9.63,0,0,1,7.65-15.46Z" transform="translate(-222.94 -1.71)"></path></svg><h3><span class="type1">リミットレギュレーション</span><span class="type2">リミット<br>レギュレーション</span></h3></a>
          </li>
          <li class="menu_btn_pagetop"><a href="#"><!--?xml version="1.0" encoding="UTF-8"?--><svg id="a" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 27.2"><defs></defs><path d="M0,20.4v6.8H36v-6.8s-36,0-36,0ZM18,0L.1,17.7H35.8L18,0Z"></path></svg></a></li>

        </ul><!--#main_menu-->
    </div>
  </nav>
</div><!--wrapper-->
<noscript>JavaScript を有効にしてください</noscript>




<div id="topcontrol" title="Scroll Back to Top" style="position: fixed; bottom: 5px; right: 5px; opacity: 0; cursor: pointer;"><img src="external/image/parts/to_top_btn.png" style="width:38px; height:39px"></div><textarea tabindex="-1" style="position: absolute; inset: -999px auto auto 0px; border: 0px; padding: 0px; box-sizing: content-box; overflow-wrap: break-word; overflow: hidden; transition: none 0s ease 0s; height: 0px !important; min-height: 0px !important; font-family: &quot;ヒラギノ角ゴ Pro W3&quot;, &quot;Hiragino Kaku Gothic Pro&quot;, メイリオ, Meiryo, Osaka, &quot;ＭＳ Ｐゴシック&quot;, &quot;MS PGothic&quot;, sans-serif; font-size: 14px; font-weight: 400; font-style: normal; letter-spacing: 0px; text-transform: none; word-spacing: 0px; text-indent: 0px; line-height: 16.8px; width: 952px;" class="autosizejs" id="autosizejs" wrap="soft"></textarea><script type="text/javascript" id="" src="https://www.konami.com/games/s/common/js/privacy_information.js"></script><div style="display: none; visibility: hidden;">

<script src="https://cdn-apac.onetrust.com/scripttemplates/otSDKStub.js" type="text/javascript" charset="UTF-8" data-domain-script="18fee0f9-e24a-48b9-99b4-5890649986fe"></script>
<script type="text/javascript">function OptanonWrapper(){};</script>
</div><script type="text/javascript" id="">var domain=document.domain,trackDomain=google_tag_manager["GTM-PWR3GWF"].macro(9),nonTrackDomain=google_tag_manager["GTM-PWR3GWF"].macro(10),aoValue=google_tag_manager["GTM-PWR3GWF"].macro(11),edgescapeValue=google_tag_manager["GTM-PWR3GWF"].macro(12),agCookieValue=google_tag_manager["GTM-PWR3GWF"].macro(13);if(-1!=trackDomain.indexOf(domain)||"2"==aoValue||"2"==edgescapeValue||"3"==edgescapeValue&&"2"==agCookieValue){var expireDate=new Date;expireDate.setDate(expireDate.getDate()+28);document.cookie="Analytics\x3d2; secure\x3dtrue; expires\x3d"+expireDate.toGMTString()}
-1!=nonTrackDomain.indexOf(domain)&&(document.cookie="Analytics\x3d; max-age\x3d0");</script><script type="text/javascript" id="">var analyticsValue=google_tag_manager["GTM-PWR3GWF"].macro(14);"2"!=analyticsValue?window["ga-disable-UA-97638476-6"]=!0:window["ga-disable-UA-97638476-6"]=!1;</script><div id="onetrust-consent-sdk"><div class="onetrust-pc-dark-filter ot-hide ot-fade-in"></div><div id="onetrust-pc-sdk" class="otPcCenter ot-hide ot-fade-in" aria-modal="true" role="alertdialog" aria-describedby="ot-pc-desc" lang="ja" aria-label="Cookie詳細設定"><!-- Close Button --><div class="ot-pc-header"><!-- Logo Tag --><div class="ot-pc-logo" role="img" aria-label="企業ロゴ"><img alt="企業ロゴ" src="https://cdn-apac.onetrust.com/logos/20753d39-0b26-410d-9c3b-1911487b304f/a8235db7-3daa-4589-b001-0fddd095cfd7/5c123760-d29b-4df8-8396-dafec20c1740/logo_KONAMI_2560.png"></div><button id="close-pc-btn-handler" class="ot-close-icon" aria-label="閉じる" style="background-image: url(&quot;https://cdn-apac.onetrust.com/logos/static/ot_close.svg&quot;);"></button></div><!-- Close Button --><div id="ot-pc-content" class="ot-pc-scrollbar"><div class="ot-optout-signal ot-hide"><div class="ot-optout-icon"><svg xmlns="http://www.w3.org/2000/svg"><path class="ot-floating-button__svg-fill" d="M14.588 0l.445.328c1.807 1.303 3.961 2.533 6.461 3.688 2.015.93 4.576 1.746 7.682 2.446 0 14.178-4.73 24.133-14.19 29.864l-.398.236C4.863 30.87 0 20.837 0 6.462c3.107-.7 5.668-1.516 7.682-2.446 2.709-1.251 5.01-2.59 6.906-4.016zm5.87 13.88a.75.75 0 00-.974.159l-5.475 6.625-3.005-2.997-.077-.067a.75.75 0 00-.983 1.13l4.172 4.16 6.525-7.895.06-.083a.75.75 0 00-.16-.973z" fill="#FFF" fill-rule="evenodd"></path></svg></div><span></span></div><h2 id="ot-pc-title">Cookie詳細設定</h2><div id="ot-pc-desc">コナミのWebサイトは、Cookieを用いてお客様のブラウザに情報を保管し、ブラウザから情報を取得する場合があります。取得される情報には、お客様に関するもの、ブラウザの設定、お客様のデバイスに関する情報が含まれている場合がありますが、お客様を直接特定できるようなものではありません。
Cookieは、Webサイトを正常に動作させるために使われます。また、Webサイトの使い勝手を改善する際やお客様の興味に応じた広告を提供する際にも使われる場合があります。
お客様は、一部のCookieをコナミのWebサイトで利用されないよう設定することができます。各Cookieのカテゴリ名をタップすると表示される詳細情報から、コナミのWebサイト上の設定を変更できます。一部のCookieは、拒否することで、コナミのWebサイトの使い勝手や提供できるサービス内容に影響が出る場合があります。
            <br><a href="https://legal.konami.com/officialsite/cookie-notice/ja/" class="privacy-notice-link" rel="noopener" target="_blank" aria-label="あなたのプライバシーを守るための詳細設定, 新しいタブで開く">詳細情報</a></div><section class="ot-sdk-row ot-cat-grp"><h3 id="ot-category-title">Cookieの同意管理を設定</h3><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0001"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0001" aria-labelledby="ot-header-id-C0001"></button><!-- Accordion header --><div class="ot-acc-hdr ot-always-active-group"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0001">必須のCookie</h4><div class="ot-always-active">常にアクティブ</div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0001">コナミのウェブサイトを正常に機能させるために必要なものです。例えば、お客様がコナミのウェブサイトの保護された領域にアクセスすることや、ショッピングカートの使用を可能にするCookieを含みます。この Cookieをブロック/警告するようにブラウザを設定することは可能ですが、ウェブサイトの一部が機能しなくなる可能性があります。この Cookieが個人を特定できる情報を保存することはありません。</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0003"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0003" aria-labelledby="ot-header-id-C0003"></button><!-- Accordion header --><div class="ot-acc-hdr"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0003">機能性 Cookie</h4><div class="ot-tgl"><input type="checkbox" name="ot-group-id-C0003" id="ot-group-id-C0003" aria-checked="true" role="switch" class="category-switch-handler" data-optanongroupid="C0003" checked="" aria-labelledby="ot-header-id-C0003"> <label class="ot-switch" for="ot-group-id-C0003"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">機能性 Cookie</span></label> </div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0003">コナミのウェブサイトでの体験を改善するために利用します。例えば、お客様がコナミのウェブサイト上で入力した文字や設定を記憶することなどがそれに当たります。このCookieを許可しない場合、サービスの一部またはすべてが正常に機能しない可能性があります。</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0002"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0002" aria-labelledby="ot-header-id-C0002"></button><!-- Accordion header --><div class="ot-acc-hdr"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0002">パフォーマンス Cookie</h4><div class="ot-tgl"><input type="checkbox" name="ot-group-id-C0002" id="ot-group-id-C0002" aria-checked="true" role="switch" class="category-switch-handler" data-optanongroupid="C0002" checked="" aria-labelledby="ot-header-id-C0002"> <label class="ot-switch" for="ot-group-id-C0002"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">パフォーマンス Cookie</span></label> </div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0002">訪問者数やトラフィックが計測できるようになり、コナミのウェブサイトのパフォーマンスを改善する際に役立ちます。最も人気があるページ、人気が低いページを確認し、訪問者がウェブサイト内をどのように移動するかを理解するのに役立ちます。この Cookie が個人を特定できる情報を保存することはありません。</p></div></div><div class="ot-accordion-layout ot-cat-item ot-vs-config" data-optanongroupid="C0004"><button aria-expanded="false" ot-accordion="true" aria-controls="ot-desc-id-C0004" aria-labelledby="ot-header-id-C0004"></button><!-- Accordion header --><div class="ot-acc-hdr"><div class="ot-plus-minus"><span></span><span></span></div><h4 class="ot-cat-header" id="ot-header-id-C0004">広告Cookie</h4><div class="ot-tgl"><input type="checkbox" name="ot-group-id-C0004" id="ot-group-id-C0004" aria-checked="true" role="switch" class="category-switch-handler" data-optanongroupid="C0004" checked="" aria-labelledby="ot-header-id-C0004"> <label class="ot-switch" for="ot-group-id-C0004"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">広告Cookie</span></label> </div></div><!-- accordion detail --><div class="ot-acc-grpcntr ot-acc-txt"><p class="ot-acc-grpdesc ot-category-desc" id="ot-desc-id-C0004">このCookieは、コナミが設定する場合もあれば、コナミの広告パートナーによりコナミのウェブサイト経由で設定される場合もあります。これらのコナミの広告パートナーはお客様が何に興味をもっているかというプロファイルを作成し、コナミのウェブサイトに加え、第三者のウェブサイトでもお客様の興味に応じた広告を表示するためなどの目的でこの Cookie を利用します。このCookieが個人情報を直接保存することはありませんが、お客様のブラウザとインターネット接続に使われているデバイスを一意的に識別します。この Cookieを受け入れない場合は、お客様の興味に応じた広告ではなく、一般的な広告が表示されるようになります。</p></div></div><!-- Groups sections starts --><!-- Group section ends --><!-- Accordion Group section starts --><!-- Accordion Group section ends --></section></div><section id="ot-pc-lst" class="ot-hide ot-hosts-ui ot-pc-scrollbar"><div id="ot-pc-hdr"><div id="ot-lst-title"><button class="ot-link-btn back-btn-handler" aria-label="Back"><svg id="ot-back-arw" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 444.531 444.531" xml:space="preserve"><title>Back Button</title><g><path fill="#656565" d="M213.13,222.409L351.88,83.653c7.05-7.043,10.567-15.657,10.567-25.841c0-10.183-3.518-18.793-10.567-25.835
                    l-21.409-21.416C323.432,3.521,314.817,0,304.637,0s-18.791,3.521-25.841,10.561L92.649,196.425
                    c-7.044,7.043-10.566,15.656-10.566,25.841s3.521,18.791,10.566,25.837l186.146,185.864c7.05,7.043,15.66,10.564,25.841,10.564
                    s18.795-3.521,25.834-10.564l21.409-21.412c7.05-7.039,10.567-15.604,10.567-25.697c0-10.085-3.518-18.746-10.567-25.978
                    L213.13,222.409z"></path></g></svg></button><h3>Performance Cookies</h3></div><div class="ot-lst-subhdr"><div class="ot-search-cntr"><p role="status" class="ot-scrn-rdr"></p><label for="vendor-search-handler" class="ot-scrn-rdr"></label> <input id="vendor-search-handler" type="text" name="vendor-search-handler"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 -30 110 110" aria-hidden="true"><title>Search Icon</title><path fill="#2e3644" d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23
            s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92
            c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17
            s-17-7.626-17-17S14.61,6,23.984,6z"></path></svg></div><div class="ot-fltr-cntr"><button id="filter-btn-handler" aria-label="Filter" aria-haspopup="true"><svg role="presentation" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 402.577 402.577" xml:space="preserve"><title>Filter Icon</title><g><path fill="#fff" d="M400.858,11.427c-3.241-7.421-8.85-11.132-16.854-11.136H18.564c-7.993,0-13.61,3.715-16.846,11.136
      c-3.234,7.801-1.903,14.467,3.999,19.985l140.757,140.753v138.755c0,4.955,1.809,9.232,5.424,12.854l73.085,73.083
      c3.429,3.614,7.71,5.428,12.851,5.428c2.282,0,4.66-0.479,7.135-1.43c7.426-3.238,11.14-8.851,11.14-16.845V172.166L396.861,31.413
      C402.765,25.895,404.093,19.231,400.858,11.427z"></path></g></svg></button></div><div id="ot-anchor"></div><section id="ot-fltr-modal"><div id="ot-fltr-cnt"><button id="clear-filters-handler">Clear</button><div class="ot-fltr-scrlcnt ot-pc-scrollbar"><div class="ot-fltr-opts"><div class="ot-fltr-opt"><div class="ot-chkbox"><input id="chkbox-id" type="checkbox" aria-checked="false" class="category-filter-handler"> <label for="chkbox-id"><span class="ot-label-txt">checkbox label</span></label> <span class="ot-label-status">label</span></div></div></div><div class="ot-fltr-btns"><button id="filter-apply-handler">Apply</button> <button id="filter-cancel-handler">Cancel</button></div></div></div></section></div></div><section id="ot-lst-cnt" class="ot-host-cnt ot-pc-scrollbar"><div id="ot-sel-blk"><div class="ot-sel-all"><div class="ot-sel-all-hdr"><span class="ot-consent-hdr">Consent</span> <span class="ot-li-hdr">Leg.Interest</span></div><div class="ot-sel-all-chkbox"><div class="ot-tgl" id="ot-selall-hostcntr"><input type="checkbox" name="switch" id="select-all-hosts-groups-handler" aria-checked="false" role="switch"> <label class="ot-switch" for="select-all-hosts-groups-handler"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">Switch Label</span></label> <span class="ot-label-status">label</span></div><div class="ot-tgl" id="ot-selall-vencntr"><input type="checkbox" name="switch" id="select-all-vendor-groups-handler" aria-checked="false" role="switch"> <label class="ot-switch" for="select-all-vendor-groups-handler"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">Switch Label</span></label> <span class="ot-label-status">label</span></div><div class="ot-tgl" id="ot-selall-licntr"><input type="checkbox" name="switch" id="select-all-vendor-leg-handler" aria-checked="false" role="switch"> <label class="ot-switch" for="select-all-vendor-leg-handler"><span class="ot-switch-nob" aria-checked="false" role="switch"></span> <span class="ot-label-txt">Switch Label</span></label> <span class="ot-label-status">label</span></div></div></div></div><div class="ot-sdk-row"><div class="ot-sdk-column"></div></div></section></section><div class="ot-pc-footer"><div class="ot-btn-container"><button class="ot-pc-refuse-all-handler">すべて拒否</button> <button class="save-preference-btn-handler onetrust-close-btn-handler">設定した内容を保存</button></div><!-- Footer logo --><div class="ot-pc-footer-logo"><a href="https://www.onetrust.com/products/cookie-consent/" target="_blank" rel="noopener noreferrer" aria-label="Powered by OneTrust 新しいタブで開く"><img alt="Powered by Onetrust" src="https://cdn-apac.onetrust.com/logos/static/powered_by_logo.svg" title="Powered by OneTrust 新しいタブで開く"></a></div></div><!-- Cookie subgroup container --><!-- Vendor list link --><!-- Cookie lost link --><!-- Toggle HTML element --><!-- Checkbox HTML --><!-- plus minus--><!-- Arrow SVG element --><!-- Accordion basic element --><span class="ot-scrn-rdr" aria-atomic="true" aria-live="polite"></span><!-- Vendor Service container and item template --><iframe class="ot-text-resize" title="onetrust-text-resize" style="position: absolute; top: -50000px; width: 100em;" aria-hidden="true"></iframe></div></div></body></html>"""

    return html, "モンスター2種の場合"


def test_generate_monsters_success(mocker, fixture_2monsters_html):
    html, test_title = fixture_2monsters_html
    parser = HtmlParser(html)
    actual = parser.generate_monsters()
    expected = [{'name': '夢幻崩界イヴリースa', 'attribute': '闇属性', 'type': '【サイバース族／効果】', 'level': 'レベル2',
                 'attack': '攻撃力/0', 'defence': '守備力/0'},
                {'name': '斬機サーキュラー', 'attribute': '光属性', 'type': '【サイバース族／効果】', 'level': 'レベル4',
                 'attack': '攻撃力/1500', 'defence': '守備力/1500'}]

    assert actual == expected, test_title
