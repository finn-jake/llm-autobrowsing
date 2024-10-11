# function call 결과 i/o 처리 및 중복 결과물 처리
async def handle_tool_calls(chunk, response_message, search_chunk, tool_id, tool_name):

    # web search function call
    if chunk.choices[0].delta.tool_calls[0].function.name == "bing_search_function":
        if chunk.choices[0].delta.tool_calls[0].id:
                if chunk.choices[0].delta.tool_calls[0].index == 0:
                    response_message = chunk.choices[0].delta

                tool_id = chunk.choices[0].delta.tool_calls[0].id
                tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif (tool_name == "bing_search_function") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments


    # waether search function call
    if chunk.choices[0].delta.tool_calls[0].function.name == "search_weather_function":
        if chunk.choices[0].delta.tool_calls[0].id:
                if chunk.choices[0].delta.tool_calls[0].index == 0:
                    response_message = chunk.choices[0].delta

                tool_id = chunk.choices[0].delta.tool_calls[0].id
                tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif (tool_name == "search_weather_function") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments

    
    # URL search function call
    if chunk.choices[0].delta.tool_calls[0].function.name == "URL_extractor":
        if chunk.choices[0].delta.tool_calls[0].id:
            if chunk.choices[0].delta.tool_calls[0].index == 0:
                response_message = chunk.choices[0].delta

            tool_id = chunk.choices[0].delta.tool_calls[0].id
            tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif(tool_name == "URL_extractor") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments


    # image generate function call
    if chunk.choices[0].delta.tool_calls[0].function.name == "image_generate_function":
        if chunk.choices[0].delta.tool_calls[0].id:
            if chunk.choices[0].delta.tool_calls[0].index == 0:
                response_message = chunk.choices[0].delta

            tool_id = chunk.choices[0].delta.tool_calls[0].id
            tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif(tool_name == "image_generate_function") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments    

    return response_message, search_chunk, tool_id, tool_name