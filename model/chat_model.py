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
    api_version=chat_keys[0],
    azure_endpoint=chat_keys[1],
    api_key=chat_keys[2]
)

async def get_chat_output(req_messages, req_model):
    if req_model == "gpt-4":
        model = "hatcheryOpenaiCanadaGPT4"

    elif req_model == "gpt-4o":
        model = "hatcheryOpenaiCanadaGPT4o"

    res = await client.chat.completions.create(
        model = model,
        messages = req_messages,
        temperature = 0.6,
        stream = True
    )

    async for chunk in res:
        if len(chunk.choices) > 0:
            yield chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""