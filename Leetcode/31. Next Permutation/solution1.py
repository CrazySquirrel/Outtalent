class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i > -1 and nums[i] >= nums[i + 1]: i -= 1

        if i > -1:
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]: j += 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]
