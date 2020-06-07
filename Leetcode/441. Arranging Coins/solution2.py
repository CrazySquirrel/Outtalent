class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + (r - l) // 2
            row = m * (m + 1) // 2
            if n < row:
                r = m - 1
            elif n > row:
                l = m + 1
            else:
                return m
        return r
