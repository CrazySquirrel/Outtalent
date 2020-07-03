class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        result = []
        for num in nums:
            if not result or num > result[-1]:
                result.append(num)
            else:
                result[bisect.bisect_left(result, num)] = num
        return len(result)
