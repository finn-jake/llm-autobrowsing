from model import *
import streamlit as st

async def handle_search_chat(message: str):
    st.session_state.search_messages.append({"role": "user", "content": message})
    with st.chat_message("user", avatar="🪽"):
        st.markdown(message)

    full_response = ""
    message_placeholder = st.empty()

    #async for chunk in request_search_chat(st.session_state.search_messages, st.session_state.chat_model):
    #    full_respose += chunk
    #    message_placeholder.markdown(full_response)
    #   await asyncio.sleep(0.25)


    st.session_state.search_messages.append({"role": "assistant", "content": full_response})