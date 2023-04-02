# -*- coding: utf-8 -*-
"""スモール・ワールド乗り換え検索の画面表示
"""

import streamlit as st

st.title('遊戯王スモール・ワールド乗り換え検索')
st.caption('遊戯王DBの公開デッキを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。')

# URL入力欄
url = st.text_input('デッキURL')