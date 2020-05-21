class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp, result = 0, -inf
        for n in nums:
            tmp += n
            result = max(result, tmp)
            tmp = max(0, tmp)
        return result
