from model import *
import streamlit as st
import asyncio

# 채팅 인풋과 아웃풋 핸들링
async def handle_search_chat(message: str, col1, col2):
    # 사용자 인풋을 session state에 저장
    st.session_state.search_messages.append({"role": "user", "content": message})

    # 사용자 인풋과 답변을 UI에 출력
    with col1:
        with st.chat_message("user", avatar = "source/cruelty.svg"):
            st.markdown(message)

        full_response = ""

        assistant_message = st.chat_message("assistant", avatar = "source/rocket.svg")
        with assistant_message:
            message_placeholder = st.empty()

        async for chunk in get_chat_output(st.session_state.search_messages, st.session_state.chat_model, col2):
            full_response += chunk
            message_placeholder.markdown(full_response)
            await asyncio.sleep(0.02)

    # 답변을 session state에 저장
    st.session_state.search_messages.append({"role": "assistant", "content": full_response})