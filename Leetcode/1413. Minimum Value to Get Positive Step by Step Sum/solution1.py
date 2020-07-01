class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = c = 0
        for n in nums:
            c += n
            m = min(m, c)
        return 1 if m > 0 else 1 - m
