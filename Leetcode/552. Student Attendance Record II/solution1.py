class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8

        MAX = 1000000007
        dp = [1, 2, 4]
        i = 3

        while i < n:
            dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % MAX)
            i += 1

        result = (dp[n - 1] + dp[i - 2] + dp[i - 3]) % MAX

        for i in range(n):
            result += dp[i] * dp[n - i - 1] % MAX
            result %= MAX

        return result
