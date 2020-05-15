from collections import Counter
from math import factorial


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        prod = 1
        for f in freq.values(): prod *= f + 1
        res = 0
        for i in range(1, prod):
            digits = []
            for f in freq.values():
                digits.append(i % (f + 1))
                i //= (f + 1)
            tmp = factorial(sum(digits))
            for d in digits: tmp //= factorial(d)
            res += tmp
        return res
