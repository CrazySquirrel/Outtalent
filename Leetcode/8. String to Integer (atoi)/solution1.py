import re

INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def myAtoi(self, str: str) -> int:
        x = re.search("^\s*([+-]?[0-9]+)", str)
        if not x: return 0
        x = int(x.group(1))
        if x < INT_MIN: return INT_MIN
        if INT_MAX < x: return INT_MAX
        return x
