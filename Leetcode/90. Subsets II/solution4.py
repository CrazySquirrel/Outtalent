class Solution:
    def subsetsWithDup(self, nums: List[int], sorted: bool = False) -> List[List[int]]:
        if not nums: return [[]]
        if len(nums) == 1: return [[], nums]
        if not sorted: nums.sort()
        result = self.subsetsWithDup(nums[:-1], sorted=True)
        result = [i + [nums[-1]] for i in result] + result
        result = {tuple(r) for r in result}
        return [list(r) for r in result]
