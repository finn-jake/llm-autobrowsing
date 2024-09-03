import os
from utils import *
from pages import *


current_direc = os.getcwd()

chat_key_path = "keys/chat_key.yaml"
search_key_path = "keys/search_key.yaml"

chat_keys = get_chat_key(current_direc, chat_key_path)
search_keys = get_search_key(current_direc, search_key_path)


## <API MODEL> ##

def main_app():
    init_session_state()

if __name__ == "__main__":
    main_app()