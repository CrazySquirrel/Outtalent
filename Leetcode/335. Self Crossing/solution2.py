class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        return any(d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b)
                   for a, b, c, d, e, f in ((x[i:i + 6] + [0] * 6)[:6] for i in range(len(x))))
