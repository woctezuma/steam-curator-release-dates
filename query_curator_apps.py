from pathlib import Path

from src.curator_utils import fetch_app_ids_from_curator_list
from src.data_utils import CURATOR_CONTENT_FNAME
from src.export_utils import write_markdown_files
from src.json_utils import load_json, save_json
from src.steam_utils import fetch_app_info

CURATOR_ID = "41397023"
LIST_ID = "86081"


def main():
    force_update = False

    if force_update or not Path(CURATOR_CONTENT_FNAME).exists():
        print("Updating JSON.")
        app_ids = fetch_app_ids_from_curator_list(
            curator_id=CURATOR_ID,
            list_id=LIST_ID,
        )
        app_info = fetch_app_info(app_ids)
        save_json(app_info, CURATOR_CONTENT_FNAME)
    else:
        app_info = load_json(CURATOR_CONTENT_FNAME)

    print("Updating Markown.")
    data = app_info["apps"]
    write_markdown_files(data)


if __name__ == "__main__":
    main()
