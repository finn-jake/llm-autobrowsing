import os
import yaml

def get_chat_key(current_direc, chat_key_path):
    key_path = os.path.join(current_direc, chat_key_path)

    with open(key_path) as f:
        config = yaml.safe_load(f)

    api_version = config["config"]["api_version"]
    azure_endpoint = config["config"]["azure_endpoint"]
    api_key = config["config"]["api_key"]
    default_model = config["config"]["model"]

    return [api_version, azure_endpoint, api_key, default_model]


def get_search_key(current_direc, search_key_path):
    key_path = os.path.join(current_direc, search_key_path)

    with open(key_path) as f:
        config = yaml.safe_load(f)

    search_key = config["config"]["BING_SUBSCRIPTION_KEY"]
    search_endpoint = config["config"]["BING_SEARCH_ENDPOINT"]

    return [search_key, search_endpoint]