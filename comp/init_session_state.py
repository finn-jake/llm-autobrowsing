import streamlit as st

def init_chat_session_state():
    st.subheader("🥑 Chat with GPT")

    if "chat_model" not in st.session_state:
        st.session_state.chat_model = "gpt-4o"

    if "search_messages" not in st.session_state:
        st.session_state.search_messages = []

    for message in st.session_state.search_messages:
        role = message["role"]

        with st.chat_message(role):
            st.markdown(f"{message['content']}")