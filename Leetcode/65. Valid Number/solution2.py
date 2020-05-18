import re

P0 = re.compile('^[-+]?(\d+\.\d*|\d*\.\d+|\d+)$')
P1 = re.compile('^[-+]?\d+\s*$')


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if 'e' in s:
            a = s.split('e')
            if len(a) > 2: return False
            return P0.match(a[0]) and P1.match(a[1])
        else:
            return P0.match(s)
