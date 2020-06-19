class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = h = 0
        for num in nums:
            l = ~h & (l ^ num)
            h = ~l & (h ^ num)
        return l
