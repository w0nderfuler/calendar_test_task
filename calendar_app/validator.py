from datetime import date

from calendar_app.calendar_model import Calendar


def is_valid_calendar_date(calendar: Calendar) -> bool:
    year = calendar.get_year()
    month = calendar.get_month()
    day = calendar.get_day()

    if not all(type(value) is int for value in (year, month, day)):
        return False

    try:
        date(year, month, day)
        return True
    except ValueError:
        return False