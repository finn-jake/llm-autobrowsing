import asyncio  # 비동기 작업을 위한 asyncio 모듈
import httpx  # 비동기 HTTP 요청을 위한 httpx 모듈

import streamlit as st
from comp import *

def search_chat_main():
    st.set_page_config(page_title="CHAT", page_icon = "🥑")
    #st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
    init_chat_session_state()

    if message := st.chat_input(""):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(handle_search_chat(message))


if __name__ == "__main__":
    search_chat_main()