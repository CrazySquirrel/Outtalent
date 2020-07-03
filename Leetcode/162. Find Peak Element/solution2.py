class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], l: int, r: int) -> int:
        if l == r: return l
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]: return self.search(nums, l, m)
        return self.search(nums, m + 1, r)
