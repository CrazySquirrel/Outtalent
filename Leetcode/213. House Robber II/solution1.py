class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 0: return 0
        if N == 1: return nums[0]
        if N == 2: return max(nums[0], nums[1])

        return max(self.rob_range(nums[0: N - 1]), self.rob_range(nums[1: N]))

    def rob_range(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 0: return 0
        if N == 1: return nums[0]
        if N == 2: return max(nums[0], nums[1])

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N): dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
