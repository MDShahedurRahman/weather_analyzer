from datetime import datetime
from config import DATE_FORMAT


def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
