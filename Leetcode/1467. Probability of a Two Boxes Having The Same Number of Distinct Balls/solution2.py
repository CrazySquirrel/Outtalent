from math import comb


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = len(balls)
        s = sum(balls)
        s2 = s // 2

        @lru_cache(None)
        def count(index, delta, ca):
            if index == n: return 1 if delta == 0 and ca == s2 else 0
            total = sum([count(index + 1, delta, ca + x) * comb(balls[index], x) for x in range(1, balls[index])])
            total += count(index + 1, delta + 1, ca)
            total += count(index + 1, delta - 1, ca + balls[index])
            return total

        return count(0, 0, 0) / comb(s, s // 2)
