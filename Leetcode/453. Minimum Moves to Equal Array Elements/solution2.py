class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s, m = 0, inf
        for n in nums:
            s += n
            m = min(m, n)
        return s - len(nums) * m
