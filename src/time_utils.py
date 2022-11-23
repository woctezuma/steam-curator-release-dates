from datetime import datetime


def to_formatted_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime("%B %d, %Y")
