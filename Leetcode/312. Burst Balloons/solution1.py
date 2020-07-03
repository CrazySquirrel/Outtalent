class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums) + 2

        nums.append(1)
        nums.insert(0, 1)

        dp = [[0] * n for _ in range(n)]

        for ln in range(2, n):
            for l in range(0, n - ln):
                r = l + ln
                dp[l][r] = max(nums[l] * nums[k] * nums[r] + dp[l][k] + dp[k][r] for k in range(l + 1, r))

        return dp[0][n - 1]
