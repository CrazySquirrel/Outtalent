import numpy as np


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1e9 + 7
        dp = np.zeros((n, k + 1, m + 1))
        ps = np.zeros((n, k + 1, m + 1))
        for i in range(1, m + 1):
            dp[0, 1, i] = 1
            ps[0, 1, i] = ps[0, 1, i - 1] + 1
        for i in range(1, n):
            for j in range(1, k + 1):
                for h in range(1, m + 1):
                    dp[i][j][h] = (dp[i][j][h] + dp[i - 1][j][h] * h) % mod
                    dp[i][j][h] = (dp[i][j][h] + ps[i - 1][j - 1][h - 1]) % mod
                    ps[i][j][h] = (ps[i][j][h - 1] + dp[i][j][h]) % mod
        result = 0
        for i in range(1, m + 1):
            result = (result + dp[n - 1][k][i]) % mod
        return int(result)
