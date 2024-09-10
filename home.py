import os
from utils import *
from pages import *
from st_on_hover_tabs import on_hover_tabs

current_direc = os.getcwd()

chat_key_path = "keys/chat_key.yaml"
search_key_path = "keys/search_key.yaml"

chat_keys = get_chat_key(current_direc, chat_key_path)
search_keys = get_search_key(current_direc, search_key_path)

def main_app():
    st.set_page_config(page_title = "HOME", page_icon = "apple.svg")
    
    #st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
    st.write("hello")


if __name__ == "__main__":  
    main_app()