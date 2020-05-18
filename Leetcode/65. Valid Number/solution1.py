import re

NUMBER_PATTERN = re.compile('^\s*[-+]?(\d+\.\d*|\d*\.\d+|\d+)(e[-+]?\d+)?\s*$')

class Solution:
    def isNumber(self, s: str) -> bool:
        return NUMBER_PATTERN.match(s)
