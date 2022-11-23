from src.data_utils import OUTPUT_DOC_FNAME
from src.format_utils import format_apps_for_display
from src.markdown_utils import TIMESTAMP_FIELD, format_data_as_markdown


def write_lines_to_disk(lines, fname):
    with open(fname, "w", encoding="utf8") as f:
        for line in lines:
            f.write(f"{line}\n")


def write_data_to_disk(data, fname):
    lines = format_data_as_markdown(data)
    write_lines_to_disk(lines, fname)


def write_markdown_files(data):
    data = format_apps_for_display(data)

    sorted_data = sorted(data, key=lambda x: x[TIMESTAMP_FIELD])
    write_data_to_disk(sorted_data, OUTPUT_DOC_FNAME)
