from datetime import date


def parse_iso_date(value: str) -> date:
    """
    Parse an ISO formatted date string (YYYY-MM-DD).
    """
    year, month, day = map(int, value.split("-"))
    return date(year, month, day)


def days_between(d1: date, d2: date) -> int:
    """
    Return absolute number of days between two dates.
    """
    return abs((d2 - d1).days)
