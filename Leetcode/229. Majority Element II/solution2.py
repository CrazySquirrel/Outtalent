class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums) / 3
        return [v for v in set(nums) if nums.count(v) > l]
