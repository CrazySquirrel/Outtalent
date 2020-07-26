class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        l = sum(nums)

        if l < S or (l + S) % 2 == 1: return 0

        target = (l + S) // 2

        dp = [1] + [0] * target

        for n in nums:
            for i in range(n, target + 1)[::-1]:
                dp[i] += dp[i - n]

        return dp[target]
