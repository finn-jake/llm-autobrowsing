import os
import re
import requests
import urllib.parse
import asyncio
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from openai import AzureOpenAI
import streamlit as st

from utils import *
from model import *

current_direc = os.getcwd()
search_key_path = "keys/search_key.yaml"
mini_key_path = "keys/search_os.yaml"
search_keys = get_search_key(current_direc, search_key_path)


def get_mini_client(current_direc, mini_key_path):
    '''
    Client Invocation for Mini GPT Utilization
    '''
    chat_keys = get_chat_key(current_direc, mini_key_path)

    client = AzureOpenAI(
        api_version = chat_keys[0],
        azure_endpoint = chat_keys[1],
        api_key = chat_keys[2]
    )

    return client


def read_prompt_template(default_path: str, file_path: str) -> str:
    '''
    Preparing a Mini Template for GPT Orchestration
    Summarizing Content into a Query-Suitable Form
    '''
    template_path = os.path.join(default_path, file_path)

    with open(template_path, "r") as f:
        prompt_template = f.read()

    return prompt_template

template_path = "contents/info_extract_template_v1.txt"
search_template = read_prompt_template(current_direc, template_path)


web_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
              'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3'}


def get_requests(term, url):
    '''
    Content Preprocessing for Mini GPT Orchestration
    '''
    try:
        res = requests.get(url, headers = web_header)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        tmp_cont = soup.text.replace('\n', ' ').replace('\\t', '')
        tmp_cont = re.sub(r'\s+', ' ', tmp_cont)
        tmp_cont = search_template.format(query = term, text = tmp_cont)

        tmp_input = [{'role': 'user', 'content': tmp_cont}]

        client = get_mini_client(current_direc, mini_key_path)

        tmp_res = client.chat.completions.create(
            model = "GPT4oMini",
            messages = tmp_input,
            temperature = 0.8
        )

        tmp_res = tmp_res.choices[0].message.content
        tmp_url = url

        return tmp_res, tmp_url
    except:
        pass


async def handle_search_model(term, mkt, key, endpoint):

    params = { 'q': term, 'mkt': mkt}
    headers = { 'Ocp-Apim-Subscription-Key': key }

    resp = requests.get(endpoint, headers = headers, params=params)
    res = resp.json()

    urls, contents = [], []
    res_urls = []

    for web_value in res["webPages"]["value"]:
        urls.append(web_value['url'])

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        result_01 = loop.run_in_executor(executor, get_requests, term, urls[0])
        result_02 = loop.run_in_executor(executor, get_requests, term, urls[1])
        result_03 = loop.run_in_executor(executor, get_requests, term, urls[2])
    
        executor_result = await asyncio.gather(result_01, result_02, result_03)

    result = {"search term" : term}
    for idx in range(len(executor_result)):
        contents.append(executor_result[idx][0])
        res_urls.append(executor_result[idx][1])

    if len(contents) >= 1:
        cnt = 0
        for idx in range(len(contents)):
            if cnt == 0:
                result["contexts"] = [{"source": res_urls[idx], "context": contents[idx]}]
                cnt += 1
            else:
                result["contexts"].append({"source": res_urls[idx], "context": contents[idx]})

    return result


async def handle_tools_model_(tool_name, tool_id, term, col2):
    if tool_name == "bing_search_function":

        search_result = {"information":[]}
        cnt = 0

        for term_ in term.split('}')[:-1]:
            term = json.loads(term_ + "}")
            search_result_ = await handle_search_model(term.get("search term"), 'ko-KR', search_keys[0], search_keys[1])

            search_result['information'].append(search_result_)

            with col2:
                st.markdown('<div class="floating"></div>', unsafe_allow_html=True)
                with st.container():
                    #st.markdown('<div class="floating"></div>', unsafe_allow_html=True)
                    info = search_result['information'][cnt]
                    search_term = info['search term']
                    search_contexts = info['contexts']
                    if cnt == 0:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)

                    st.markdown(f"Search Term: {search_term}")
                    
                    for context in search_contexts:
                        st.markdown(f"[Search Source]({context['source']})")
                        st.markdown(f"Compressed information: {context['context']}")

                    st.divider()

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)

                    cnt += 1

        search_result = json.dumps(search_result, ensure_ascii=False)

        result = {
            "tool_call_id": tool_id,
            "role" : "tool",
            "name" : tool_name,
            "content" : search_result
        }

        return result