class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2: date1, date2 = date2, date1

        @lru_cache(None)
        def special(year: int) -> bool:
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        def split_date(date: str):
            year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
            if month > 1:
                m2d = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
                day += sum([m2d[m] for m in range(1, month)])
            if month > 2 and special(year):
                day += 1
            return year, day

        year1, day1 = split_date(date1)
        year2, day2 = split_date(date2)

        gap = 0

        for year in range(year1, year2):
            if special(year):
                gap += 366
            else:
                gap += 365

        return gap - day1 + day2
