# -*- coding: utf-8 -*-
"""スモール・ワールド乗り換え検索の画面表示
"""
import streamlit as st

st.title("遊戯王スモール・ワールド乗り換え検索")
st.caption("遊戯王DBの公開デッキを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。")

monster_names = ()

with st.form(key="deck_url"):

    # URL入力欄の入力値
    url = st.text_input("デッキURL")
    
    # デッキ取得ボタンの押下状態（boolean）
    submit_btn = st.form_submit_button("デッキ取得")

    if submit_btn:
        # TODO: 送信ボタンが押されたら、DeckInfoクラスにURLを渡す。
        # TODO: 取得成功・失敗を表示。（失敗：処理終了 | 成功：処理継続）
        # TODO: DeckInfoクラスからモンスター名のタプルを取得し、monster_namesに代入する。
        st.text(f"Deck URL: {url}")
        monster_names = ('エフェクト・ヴェーラー', 'ドットスケーパー', 'フォーマッド・スキッパー', 'マイクロ・コーダー', '増殖するG', '夢幻崩界イヴリース', '灰流うらら', 'コード・ジェネレーター', '斬機シグマ', '斬機アディオン', '斬機サブトラ', '斬機ダイア', '斬機サーキュラー', 'パラレルエクシード', 'ガッチリ＠イグニスター')
    
    # サーチ元指定（プルダウン）
    transit_start = st.selectbox("サーチ元", monster_names)
    
    # TODO: サーチ元に指定されたモンスターでSearchResultクラスに検索要求する。
    # TODO: 検索結果をUI表示。
    # TODO: 検索結果のモンスター名一覧を取得し、サーチ先プルダウンに表示する。
    
    # サーチ先指定（プルダウン）
    # 検索結果の中から候補を選ぶ「絞り込み検索」
    transit_goal = st.selectbox("サーチ先", monster_names)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("サーチ元")
        
    with col2:
        st.header("経由")
    
    with col3:
        st.header("サーチ先")