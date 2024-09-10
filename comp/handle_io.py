from model import *
import streamlit as st
import asyncio

async def handle_search_chat(message: str, col1, col2):
    st.session_state.search_messages.append({"role": "user", "content": message})

    with col1:
        with st.chat_message("user", avatar = "🥸"):
            st.markdown(message)

        full_response = ""

        assistant_message = st.chat_message("assistant", avatar = "😤")
        with assistant_message:
            message_placeholder = st.empty()

        async for chunk in get_chat_output(st.session_state.search_messages, st.session_state.chat_model, col2):
            full_response += chunk
            message_placeholder.markdown(full_response)
            await asyncio.sleep(0.02)

    st.session_state.search_messages.append({"role": "assistant", "content": full_response})