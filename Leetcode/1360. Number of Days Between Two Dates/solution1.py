from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        day1 = datetime(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
        day2 = datetime(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))
        return abs((day1 - day2).days)
