from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt

        return dp[len(nums)][S]
