import asyncio  # 비동기 작업을 위한 asyncio 모듈
import httpx  # 비동기 HTTP 요청을 위한 httpx 모듈

import streamlit as st
from pyparsing import empty
from comp import *

st.set_page_config(layout = "wide")
col1, empty, col2 = st.columns([0.5, 0.1, 0.4])

html_style = '''
<style>
div:has( >.element-container div.floating) {
    top: 0;
    bottom:0;
    position:fixed;
    overflow-y:scroll;
    overflow-x:hidden;
}
</style>
'''

st.markdown(html_style, unsafe_allow_html=True)

with col1:
    with st.container():
        init_chat_session_state()

# 답변 생성 모델에 사용자 인풋 전달
if message := st.chat_input(""):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(handle_search_chat(message, col1, col2))
