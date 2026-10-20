class Calendar:
    def __init__(self, year: int, month: int, day: int):
        self._year = year
        self._month = month
        self._day = day

    def get_year(self) -> int:
        return self._year

    def get_month(self) -> int:
        return self._month

    def get_day(self) -> int:
        return self._day