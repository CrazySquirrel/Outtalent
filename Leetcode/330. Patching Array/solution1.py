class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, j, l, result = 0, 1, len(nums), 0
        while j <= n:
            if i < l and nums[i] <= j:
                j += nums[i]
                i += 1
            else:
                j += j
                result += 1
        return result
