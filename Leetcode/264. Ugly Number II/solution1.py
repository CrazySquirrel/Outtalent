class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 0: return 0
        dp = [1] * n
        index2 = index3 = index5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]
