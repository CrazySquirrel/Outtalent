class Solution:
    def rob(self, nums: List[int]) -> int:
        j = i = 0
        for x in nums: j, i = i, max(j + x, i)
        return max(j, i)
