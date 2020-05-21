class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[i, j]
            if j == len(pattern):
                memo[i, j] = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    memo[i, j] = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    memo[i, j] = first_match and dp(i + 1, j + 1)
            return memo[i, j]

        return dp(0, 0)
