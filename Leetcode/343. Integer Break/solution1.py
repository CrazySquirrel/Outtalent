class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dfs(s: int):
            if s <= 0: return 0
            if s == 1: return 1
            return max(max(i * dfs(s - i), i * (s - i)) for i in range(1, s))

        return dfs(n)
