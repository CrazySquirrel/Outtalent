class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x: int) -> int:
            if x == 1: return 0
            if x % 2 == 0: return 1 + power(x // 2)
            return 1 + power(3 * x + 1)

        return heapq.nsmallest(k, [(power(i), i) for i in range(lo, hi + 1)])[-1][1]
