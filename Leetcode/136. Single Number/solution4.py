class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums: result ^= n
        return result
