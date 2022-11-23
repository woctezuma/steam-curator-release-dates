import re

import requests

from src.utils import to_int


def get_curator_url(curator_id, list_id):
    return f"https://store.steampowered.com/curator/{curator_id}/list/{list_id}"


def parse_app_ids(html):
    regex = re.compile(r"&quot;appid&quot;:(\d+),")
    return regex.findall(html)


def fetch_app_ids_from_curator_list(curator_id, list_id):
    response = requests.get(url=get_curator_url(curator_id, list_id))

    if response.ok:
        app_ids = parse_app_ids(html=response.text)
    else:
        app_ids = []

    return to_int(set(app_ids))
