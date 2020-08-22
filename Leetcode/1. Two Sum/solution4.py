class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, num in enumerate(nums):
            if num in h: return [h[num], index]
            h[target - num] = index
        raise ValueError('No two sum solution')
