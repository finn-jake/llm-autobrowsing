import os
from utils import *
from contents import *

current_direc = os.getcwd()

# 비동기 OpenAI 클라이언트를 생성
client = get_client_(current_direc)
tools = [get_tools_(current_direc)]


async def get_chat_output(req_messages, req_model):
    search_chunk = ""
    response_message, tool_name, tool_id = "", "", ""

    if req_model == "gpt-4":
        model = "hatcheryOpenaiCanadaGPT4"

    elif req_model == "gpt-4o":
        model = "hatcheryOpenaiCanadaGPT4o"

    res = await client.chat.completions.create(
        model = model,
        messages = req_messages,
        temperature = 0.6,
        tools = tools,
        tool_choice = "auto",
        stream = True
    )

    async for chunk in res:
        if len(chunk.choices) > 0:
            if not chunk.choices[0].delta.tool_calls:
                yield chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""

            else:
                response_message, search_chunk, tool_id, tool_name = await handle_tool_calls(chunk, response_message, search_chunk, tool_id, tool_name)

    if tool_name != "":
        response_message.tool_calls[0].function.arguments = search_chunk
        response_message.role = "assistant"
        req_messages.append(response_message)

        tmp = await handle_tools_model_(tool_name, tool_id, search_chunk)
        
        req_messages.append(tmp)


        res = await client.chat.completions.create(
            model=model,
            messages=req_messages,
                #{"role": "system", "content": get_prompt_parsing_assistant()},  # 시스템 메시지
                #{"role": "user", "content": req.message}  # 사용자 메시지
            #temperature=0.6,
            stream=True  # 스트림 모드 사용
            )

        async for chunk in res:
            if len(chunk.choices) > 0:
                yield chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""