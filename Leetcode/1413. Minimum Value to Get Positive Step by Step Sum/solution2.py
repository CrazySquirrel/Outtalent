class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return (1 - min(accumulate(nums, initial=0)))
