class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == len(p): return i == len(s)

            fm = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                return dp(i, j + 2) or fm and dp(i + 1, j)
            else:
                return fm and dp(i + 1, j + 1)

        return dp(0, 0)
