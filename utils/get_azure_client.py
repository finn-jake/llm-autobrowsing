from utils import *

from openai import AsyncAzureOpenAI

def get_client_(current_direc):
    chat_key_path = "keys/chat_key.yaml"
    chat_keys = get_chat_key(current_direc, chat_key_path)

    # 비동기 OpenAI 클라이언트를 생성
    client = AsyncAzureOpenAI(
        api_version=chat_keys[0],
        azure_endpoint=chat_keys[1],
        api_key=chat_keys[2]
    )

    return client