HEADERS = ["AppID", "Title", "Hidden date", "Public date"]
TITLE_FIELDS = ["title"]
TIMESTAMP_FIELD = "rt_release_date"
HIDDEN_DATE_FIELD = "hidden_release"
TRANSFORMED_FIELD_DICT = {TIMESTAMP_FIELD: HIDDEN_DATE_FIELD}
HIDDEN_DATE_FIELDS = list(TRANSFORMED_FIELD_DICT.values())
PUBLIC_DATE_FIELDS = ["release"]
ENTRY_FIELDS = ["appid"] + TITLE_FIELDS + HIDDEN_DATE_FIELDS + PUBLIC_DATE_FIELDS
PLACE_HOLDER = "---"


def to_table_row(row_no, str_elements):
    concatenated_elements = "|".join(str_elements)
    line = f"|{row_no}|{concatenated_elements}|"
    return line


def get_headers_line():
    place_holder_for_number = "#"
    return to_table_row(place_holder_for_number, HEADERS)


def get_separator_line():
    place_holder = PLACE_HOLDER
    num_headers = len(HEADERS)
    return to_table_row(place_holder, [place_holder] * num_headers)


def format_data_as_markdown(data):
    lines = [get_headers_line(), get_separator_line()]

    for i, entry in enumerate(data, start=1):
        line = to_table_row(i, [str(entry[k]) for k in ENTRY_FIELDS])

        lines.append(line)

    return lines
