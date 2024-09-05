import streamlit as st
from contents import *

def init_chat_session_state():
    st.subheader("🥑 Avocado GPT")

    if "chat_model" not in st.session_state:
        st.session_state.chat_model = "gpt-4o"

    if "search_messages" not in st.session_state:
        st.session_state.search_messages = []
        #시스템 메세지 추가
        date_aware = {"role": "user", "content": get_current_date_parsing_assistant()}
        st.session_state.search_messages.append(date_aware)

    for message in st.session_state.search_messages[1:]:
        role = message["role"]
        
        if role == "user": 
            avatar = "🥸"
        
        elif role == "assistant":
            avatar = "😤"

        with st.chat_message(role, avatar=avatar):
            st.markdown(f"{message['content']}")