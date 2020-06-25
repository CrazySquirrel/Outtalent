class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == len(pattern): return i == len(text)

            first_match = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                return dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)

