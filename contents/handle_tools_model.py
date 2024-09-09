import os
import requests
from bs4 import BeautifulSoup
from utils import *

current_direc = os.getcwd()
search_key_path = "keys/search_key.yaml"
search_keys = get_search_key(current_direc, search_key_path)

web_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
              'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3'}


async def handle_search_model(term, mkt, key, endpoint):

    params = { 'q': term, 'mkt': mkt}
    headers = { 'Ocp-Apim-Subscription-Key': key }

    resp = requests.get(endpoint, headers = headers, params=params)
    res = resp.json()

    urls, contents = [], []
    res_urls = []

 
    for web_value in res["webPages"]["value"]:
        urls.append(web_value['url'])

    for url in urls[:3]:
        res = requests.get(url, headers = web_header)
        res.raise_for_status() # 웹페이지의 상태가 정상인지 확인
        soup = BeautifulSoup(res.text, "lxml")

        contents.append(soup.text.replace('\n', ' ').replace('  ', ' '))
        res_urls.append(url)

    result = {"search term" : term}

    if len(contents) >= 1:
        cnt = 0
        for idx in range(len(contents)):
            if cnt == 0:
                result["contexts"] = [{"source": res_urls[idx], "context": contents[idx]}]
                cnt += 1
            else:
                result["contexts"].append({"source": res_urls[idx], "context": contents[idx]})

    return json.dumps(result)


async def handle_tools_model_(tool_name, tool_id, term):
    if tool_name == "bing_search_function":

        term = json.loads(term)
        search_result = await handle_search_model(term.get("search term"), 'ko-KR', search_keys[0], search_keys[1])

        result = {
            "tool_call_id": tool_id,
            "role" : "tool",
            "name" : tool_name,
            "content" : search_result
        }

        return result