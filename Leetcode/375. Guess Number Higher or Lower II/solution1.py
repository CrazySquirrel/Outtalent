class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(l: int, r: int) -> int:
            return min([k + max(dp(l, k - 1), dp(k + 1, r)) for k in range(l, r + 1)]) if l < r else 0

        return dp(1, n)
