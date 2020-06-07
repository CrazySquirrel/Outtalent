class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)

        @lru_cache(None)
        def backtracking(si: int, tj: int):
            if ls - si < lt - tj: return 0
            if tj == lt: return 1
            return sum(backtracking(i + 1, tj + 1) for i in range(si, ls) if t[tj] == s[i])

        return backtracking(0, 0)
