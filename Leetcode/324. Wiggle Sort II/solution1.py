class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) // 2
        left, right = nums[:mid], nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
