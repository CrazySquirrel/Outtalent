from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        nums[:] = reduce(lambda a, b: a + b, [[i] * counter[i] for i in range(3)])
