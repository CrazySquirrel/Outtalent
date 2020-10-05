class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r: return i
            l += nums[i]
        return -1
