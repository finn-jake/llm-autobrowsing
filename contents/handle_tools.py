async def handle_tool_calls(chunk, response_message, search_chunk, tool_id, tool_name):
    if chunk.choices[0].delta.tool_calls[0].function.name == "bing_search_function":
        if chunk.choices[0].delta.tool_calls[0].id:
                if chunk.choices[0].delta.tool_calls[0].index == 0:
                    response_message = chunk.choices[0].delta

                tool_id = chunk.choices[0].delta.tool_calls[0].id
                tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif (tool_name == "bing_search_function") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments


    if chunk.choices[0].delta.tool_calls[0].function.name == "search_weather_function":
        if chunk.choices[0].delta.tool_calls[0].id:
                if chunk.choices[0].delta.tool_calls[0].index == 0:
                    response_message = chunk.choices[0].delta

                tool_id = chunk.choices[0].delta.tool_calls[0].id
                tool_name = chunk.choices[0].delta.tool_calls[0].function.name

    elif (tool_name == "search_weather_function") and (chunk.choices[0].delta.tool_calls[0].id == None):
        search_chunk += chunk.choices[0].delta.tool_calls[0].function.arguments

    return response_message, search_chunk, tool_id, tool_name