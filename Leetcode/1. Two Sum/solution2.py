class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            if target - v in h: return [h[target - v], i]
            h[v] = i
        return []
