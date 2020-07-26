class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for b in zip(*map('{:030b}'.format, nums)):
            zeros = b.count('0')
            total += zeros * (len(b) - zeros)
        return total
