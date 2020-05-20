class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if s[i - 1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]

            if i > 1 and 26 >= int(s[i - 2:i]) >= 1 and s[i - 2] != '0': dp[i] += dp[i - 2]

        return dp[len(s)]
