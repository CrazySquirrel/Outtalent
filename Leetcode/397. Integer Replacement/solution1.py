class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(t: int) -> int:
            if t == 1: return 0
            if t % 2:
                return min(dfs(t + 1), dfs(t - 1)) + 1
            else:
                return dfs(t // 2) + 1

        return dfs(n)
