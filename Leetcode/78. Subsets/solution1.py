from itertools import combinations, chain


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(nums, s) for s in range(len(nums) + 1))
