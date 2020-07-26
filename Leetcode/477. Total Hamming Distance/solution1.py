class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for pos in range(32):
            bit_count = sum(((n >> pos) & 1) for n in nums)
            res += bit_count * (len(nums) - bit_count)
        return res
