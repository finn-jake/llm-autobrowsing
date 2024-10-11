import os
from utils import *
from contents import *

current_direc = os.getcwd()

# 비동기 OpenAI 클라이언트를 생성
client = get_client_(current_direc, "keys/chat_key.yaml")
tools = [tool['tools'] for tool in get_tools_(current_direc)]


async def get_chat_output(req_messages, req_model, col2):
    search_chunk = ""
    response_message, tool_name, tool_id = "", "", ""
    copy_messages = req_messages.copy()

    if req_model == "gpt-4":
        model = "hatcheryOpenaiCanadaGPT4"

    elif req_model == "gpt-4o":
        model = "hatcheryOpenaiCanadaGPT4o"

    try:
        res = await client.chat.completions.create(
            model = model,
            messages = copy_messages,
            temperature = 0.8,
            tools = tools,
            tool_choice = "auto",
            stream = True
        )

    except:
        copy_messages = copy_messages[:-1]
        copy_messages.append({'role': 'user', 'content': '방금 오류가 발생했다고 나한테 한 문장으로 안내해줘'})

        res = await client.chat.completions.create(
            model = model,
            messages = copy_messages,
            temperature = 0.8,
            tools = tools,
            tool_choice = "auto",
            stream = True
        )

    tool_ids = []
    async for chunk in res:
        if len(chunk.choices) > 0:
            # 만약 funtion call이 필요하지 않은 경우 default gpt의 답변을 그대로 전달
            if not chunk.choices[0].delta.tool_calls:
                yield chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""

            # 만약 function call이 필요한 경우 실행
            else:
                response_message, search_chunk, tool_id, tool_name = await handle_tool_calls(chunk, response_message, search_chunk, tool_id, tool_name)
                tool_ids.append(tool_id)

    # function call이 필요한 경우 handle_tools_model_ 함수를 통해 참조할 수 있는 정보를 copy_messages에 추가
    if tool_name != "":
        response_message.tool_calls[0].function.arguments = search_chunk
        response_message.role = "assistant"
        copy_messages.append(response_message)

        tmp = await handle_tools_model_(tool_name, tool_ids[0], search_chunk, col2)
        copy_messages.append(tmp)

        #print(copy_messages)
        res = await client.chat.completions.create(
            model=model,
            messages=copy_messages,
                #{"role": "system", "content": get_prompt_parsing_assistant()},  # 시스템 메시지
                #{"role": "user", "content": req.message}  # 사용자 메시지
            #temperature=0.6,
            stream=True  # 스트림 모드 사용
            )

        async for chunk in res:
            if len(chunk.choices) > 0:
                yield chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""