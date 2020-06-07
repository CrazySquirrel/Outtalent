from itertools import groupby


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 not in nums: return 0
        groups = [(key, len(list(group))) for key, group in groupby(nums) if key == 1]
        return max(groups, key=lambda s: s[1])[1]
