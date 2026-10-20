import pytest

from calendar_app.calendar_model  import Calendar
from calendar_app.validator import is_valid_calendar_date


@pytest.mark.parametrize(
    "year, month, day",
    [
        (2025, 5, 15),
        (2025, 1, 1),
        (2025, 1, 31),
        (2025, 4, 30),
        (2025, 12, 31),
    ],
)
def test_valid_regular_date(year, month, day):
    calendar = Calendar(year, month, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is True


@pytest.mark.parametrize(
    "month, day",
    [
        (4, 31),
        (6, 31),
        (9, 31),
        (11, 31),
    ],
)
def test_invalid_day_for_30_day_month(month, day):
    calendar = Calendar(2025, month, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is False


@pytest.mark.parametrize(
    "day, expected",
    [
        (28, True),
        (29, False),
    ],
)
def test_february_in_common_year(day, expected):
    calendar = Calendar(2025, 2, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is expected


@pytest.mark.parametrize(
    "day, expected",
    [
        (29, True),
        (30, False),
    ],
)
def test_february_in_leap_year(day, expected):
    calendar = Calendar(2024, 2, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (1900, False),
        (2000, True),
    ],
)
def test_century_leap_year(year, expected):
    calendar = Calendar(year, 2, 29)
    actual = is_valid_calendar_date(calendar)

    assert actual is expected


@pytest.mark.parametrize(
    "month",
    [
        0,
        13,
    ],
)
def test_invalid_month(month):
    calendar = Calendar(2025, month, 1)
    actual = is_valid_calendar_date(calendar)

    assert actual is False


@pytest.mark.parametrize(
    "day",
    [
        -1,
        0,
        32,
    ],
)
def test_invalid_day(day):
    calendar = Calendar(2025, 1, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is False


@pytest.mark.parametrize(
    "year",
    [
        0,
        -1,
        10000,
    ],
)
def test_invalid_year(year):
    calendar = Calendar(year, 1, 1)
    actual = is_valid_calendar_date(calendar)

    assert actual is False


@pytest.mark.parametrize(
    "year, month, day",
    [
        ("2025", 1, 1),
        (2025, "1", 1),
        (2025, 1, "1"),
        (2025.0, 1, 1),
        (2025, 1.0, 1),
        (2025, 1, 1.0),
        (None, 1, 1),
        (2025, None, 1),
        (2025, 1, None),
        (True, 1, 1),
        (2025, True, 1),
        (2025, 1, False),
    ],
)
def test_invalid_date_type(year, month, day):
    calendar = Calendar(year, month, day)
    actual = is_valid_calendar_date(calendar)

    assert actual is False