class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        def bisect(target):
            l, r = 0, len(result) - 1
            while l < r:
                m = l + (r - l) // 2
                if result[m] == target:
                    return m
                elif result[m] > target:
                    r = m
                else:
                    l = m + 1
            return l

        result = []
        for num in nums:
            if not result or num > result[-1]:
                result.append(num)
            else:
                result[bisect(num)] = num
        return len(result)
