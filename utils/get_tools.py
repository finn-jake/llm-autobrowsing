import os
import json

def get_tools_(default_path, file_path = "contents/tool_list.json"):
    tool_path = os.path.join(default_path, file_path)

    with open(tool_path, "r", encoding = "utf-8") as file:
        data = json.load(file)

    return data["tools_list"]