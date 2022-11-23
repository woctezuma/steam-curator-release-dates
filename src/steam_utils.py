import requests

from src.utils import to_str

STEAM_API_URL = "https://store.steampowered.com/broadcast/ajaxgetbatchappcapsuleinfo"


def fetch_app_info(app_ids):
    concatenated_app_ids = ",".join(to_str(app_ids))

    response = requests.get(url=STEAM_API_URL, params={"appids": concatenated_app_ids})

    if response.ok:
        data = response.json()
    else:
        data = []

    return data
