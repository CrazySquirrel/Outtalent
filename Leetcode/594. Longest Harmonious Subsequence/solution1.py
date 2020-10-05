from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max([c[n] + c[n + 1] for n in c if n + 1 in c] or [0])
