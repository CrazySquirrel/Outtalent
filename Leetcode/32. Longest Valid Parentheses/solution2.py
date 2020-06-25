class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        result = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] != ')': continue

            if s[i - 1] == '(':
                if i >= 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                if (i - dp[i - 1]) >= 2:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2

            result = max(result, dp[i])

        return result
