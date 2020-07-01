class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2: date1, date2 = date2, date1

        @lru_cache(None)
        def special(year: int) -> bool:
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        def split_date(date: str):
            year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
            day += [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month]
            day += 1 if month > 2 and special(year) else 0
            return year, day

        year1, day1 = split_date(date1)
        year2, day2 = split_date(date2)

        gap = sum(366 if special(year) else 365 for year in range(year1, year2))

        return gap - day1 + day2
