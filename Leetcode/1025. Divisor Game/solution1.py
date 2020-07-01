class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)

        for i in range(2, N + 1):
            if i % 2 == 0 and dp[i // 2] == False:
                dp[i] = True
                continue

            for j in range(1, int(math.sqrt(i))):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break

        return dp[N]
