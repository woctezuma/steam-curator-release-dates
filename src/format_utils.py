from src.markdown_utils import PUBLIC_DATE_FIELDS, TITLE_FIELDS, TRANSFORMED_FIELD_DICT
from src.time_utils import to_formatted_date

NOISY_TITLE_PREFIX = "Pre-Purchase "
MAX_DISPLAY_LENGTH = 50


def format_apps_for_display(data):
    for entry in data:
        format_apps_in_dict(entry)

    return data


def format_apps_in_dict(entry):
    for k in TITLE_FIELDS:
        entry[k] = clean_title(entry[k])[:MAX_DISPLAY_LENGTH]
    for k in PUBLIC_DATE_FIELDS:
        entry[k] = entry[k][:MAX_DISPLAY_LENGTH]
    for k, v in TRANSFORMED_FIELD_DICT.items():
        entry[v] = to_formatted_date(entry[k])


def clean_title(title):
    return title.removeprefix(NOISY_TITLE_PREFIX)
