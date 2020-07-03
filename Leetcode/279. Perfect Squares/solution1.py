class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = {i: i * i for i in range(int(n ** 0.5 + 2))}

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            j = 1

            while sqrs[j] <= i:
                dp[i] = min(dp[i], dp[i - sqrs[j]] + 1)
                j += 1

        return dp[n]
