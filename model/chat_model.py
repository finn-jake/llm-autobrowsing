import os
from utils import *

from openai import AsyncAzureOpenAI


current_direc = os.getcwd()

chat_key_path = "keys/chat_key.yaml"
search_key_path = "keys/search_key.yaml"

chat_keys = get_chat_key(current_direc, chat_key_path)
search_keys = get_search_key(current_direc, search_key_path)


# 비동기 OpenAI 클라이언트를 생성
client = AsyncAzureOpenAI(
    api_version=api_version,
    azure_endpoint=azure_endpoint,
    api_key=api_key
)