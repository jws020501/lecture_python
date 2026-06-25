def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()


def to_int(value, default=0):
    if isinstance(value, bool):
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def positive_int(value):
    number = to_int(value)
    if number <= 0:
        return None
    return number


def score_value(value):
    number = to_int(value)
    if number < 1 or number > 5:
        return None
    return number
