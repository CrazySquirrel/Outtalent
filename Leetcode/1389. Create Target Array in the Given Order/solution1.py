class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            result = result[0:index[i]] + [nums[i]] + result[index[i]:]

        return result
