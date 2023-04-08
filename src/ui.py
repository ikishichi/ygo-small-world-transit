# -*- coding: utf-8 -*-
"""スモール・ワールド乗り換え検索の画面表示
"""
import streamlit as st
import pandas as pd

st.title("遊戯王スモール・ワールド乗り換え検索")
st.caption("遊戯王DBの公開デッキを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。")

columns = ['name', 'attribute', 'type', 'level', 'attack', 'defence']
monsters_df = pd.DataFrame(columns=columns)

with st.form(key="deck_url"):

    # URL入力欄の入力値
    url = st.text_input("デッキURL")
    
    # デッキ取得ボタンの押下状態（boolean）
    submit_btn = st.form_submit_button("デッキ取得")

    if submit_btn:
        # TODO: 送信ボタンが押されたら、DeckInfoクラスにURLを渡す。
        # TODO: 取得成功・失敗を表示。（失敗：処理終了 | 成功：処理継続）
        # TODO: Deckクラスにhtmlを渡す
        st.text(f"Deck URL: {url}")
        monsters_df = pd.DataFrame([{'name': 'エフェクト・ヴェーラー', 'attribute': '光属性', 'type': '【魔法使い族／チューナー／効果】', 'level': 'レベル1', 'attack': '攻撃力/0', 'defence': '守備力/0'}, {'name': 'ドットスケーパー', 'attribute': '地属性', 'type': '【サイバース族／効果】', 'level': 'レベル1', 'attack': '攻撃力/0', 'defence': '守備力/2100'}, {'name': 'フォーマッド・スキッパー', 'attribute': '光属性', 'type': '【サイバース族／効果】', 'level': 'レベル1', 'attack': '攻撃力/0', 'defence': '守備力/0'}, {'name': 'マイクロ・コーダー', 'attribute': '闇属性', 'type': '【サイバース族／効果】', 'level': 'レベル1', 'attack': '攻撃力/300', 'defence': '守備力/0'}, {'name': '増殖するG', 'attribute': '地属性', 'type': '【昆虫族／効果】', 'level': 'レベル2', 'attack': '攻撃力/500', 'defence': '守備力/200'}, {'name': '夢幻崩界イヴリース', 'attribute': '闇属性', 'type': '【サイバース族／効果】', 'level': 'レベル2', 'attack': '攻撃力/0', 'defence': '守備力/0'}, {'name': '灰流うらら', 'attribute': '炎属性', 'type': '【アンデット族／チューナー／効果】', 'level': 'レベル3', 'attack': '攻撃力/0', 'defence': '守備力/1800'}, {'name': 'コード・ジェネレーター', 'attribute': '地属性', 'type': '【サイバース族／効果】', 'level': 'レベル3', 'attack': '攻撃力/1300', 'defence': '守備力/500'}, {'name': '斬機シグマ', 'attribute': '光属性', 'type': '【サイバース族／チューナー／効果】', 'level': 'レベル4', 'attack': '攻撃力/1000', 'defence': '守備力/1500'}, {'name': '斬機アディオン', 'attribute': '炎属性', 'type': '【サイバース族／効果】', 'level': 'レベル4', 'attack': '攻撃力/1000', 'defence': '守備力/1000'}, {'name': '斬機サブトラ', 'attribute': '炎属性', 'type': '【サイバース族／効果】', 'level': 'レベル4', 'attack': '攻撃力/1000', 'defence': '守備力/1000'}, {'name': '斬機ダイア', 'attribute': '光属性', 'type': '【サイバース族／チューナー／効果】', 'level': 'レベル4', 'attack': '攻撃力/1000', 'defence': '守備力/1500'}, {'name': '斬機サーキュラー', 'attribute': '光属性', 'type': '【サイバース族／効果】', 'level': 'レベル4', 'attack': '攻撃力/1500', 'defence': '守備力/1500'}, {'name': 'パラレルエクシード', 'attribute': '風属性', 'type': '【サイバース族／効果】', 'level': 'レベル8', 'attack': '攻撃力/2000', 'defence': '守備力/2000'}, {'name': 'ガッチリ＠イグニスター', 'attribute': '地属性', 'type': '【サイバース族／効果】', 'level': 'レベル8', 'attack': '攻撃力/0', 'defence': '守備力/3000'}])
    
    # サーチ元指定（プルダウン）
    transit_start = st.selectbox("サーチ元", monsters_df)
    
    # TODO: サーチ元に指定されたモンスターでSearchResultクラスに検索要求する。
    # TODO: 検索結果をUI表示。
    # TODO: 検索結果のモンスター名一覧を取得し、サーチ先プルダウンに表示する。
    
    # サーチ先指定（プルダウン）
    # 検索結果の中から候補を選ぶ「絞り込み検索」
    transit_goal = st.selectbox("サーチ先", monsters_df)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("サーチ元")
        st.write("マイクロ・コーダー")
        st.write("マイクロ・コーダー")
        st.write("マイクロ・コーダー")
        st.markdown("---")
        st.write("マイクロ・コーダー")
        st.write("マイクロ・コーダー")
        st.write("マイクロ・コーダー")
        
    with col2:
        st.header("経由")
        st.write("斬機シグマ")
        st.write("斬機サブトラ")
        st.write("斬機アディオン")
        st.markdown("---")
        st.write("斬機シグマ")
        st.write("斬機サブトラ")
        st.write("斬機アディオン")
    
    with col3:
        st.header("サーチ先")
        st.write("ガッチリ＠イグニスター")
        st.write("ガッチリ＠イグニスター")
        st.write("ガッチリ＠イグニスター")
        st.markdown("---")
        st.write("夢幻崩界イヴリース")
        st.write("夢幻崩界イヴリース")
        st.write("夢幻崩界イヴリース")