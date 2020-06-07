class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for j in range(M + 1): dp[0][j] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
