class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums, hs, s = sorted(nums, reverse=True), sum(nums) / 2, 0
        for i in range(len(nums)):
            s += nums[i]
            if s > hs: break
        return nums[:i + 1]
