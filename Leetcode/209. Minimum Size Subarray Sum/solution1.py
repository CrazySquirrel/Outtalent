class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = inf
        l = summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            while summ >= s:
                result = min(result, i + 1 - l)
                summ -= nums[l]
                l += 1
        return result if result != inf else 0
