class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False] * len(nums)
        memo[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if memo[j]:
                    memo[i] = True
                    break

        return memo[0]
