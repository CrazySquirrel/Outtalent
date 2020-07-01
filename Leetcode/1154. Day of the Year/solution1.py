from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])
        leap = 1 if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 0
        return 365 - (datetime(year, 12, 31) - datetime(year, month, day)).days + leap
