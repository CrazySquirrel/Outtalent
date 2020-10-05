class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n: return n
        for i in range(1, n + 1):
            if nums[n - i - 1] < i <= nums[n - i]: return i
        return -1
