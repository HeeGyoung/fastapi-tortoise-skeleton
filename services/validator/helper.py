import re

PHONE_WITHOUT_DASH_REGEX = r"^01[0|1|6|7|8|9]\d{3,4}\d{4}$"


def is_phone(number: str):
    return re.compile(PHONE_WITHOUT_DASH_REGEX).match(number)
