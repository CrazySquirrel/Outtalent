class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        size = len(A)
        ans = 0
        dp = [collections.defaultdict(int) for x in range(size)]

        for x in range(size):
            for y in range(x):
                delta = A[x] - A[y]
                dp[x][delta] += 1

                if delta in dp[y]:
                    dp[x][delta] += dp[y][delta]
                    ans += dp[y][delta]

        return ans
