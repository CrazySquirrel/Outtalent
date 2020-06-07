class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums: result += [curr + [num] for curr in result]
        return result
