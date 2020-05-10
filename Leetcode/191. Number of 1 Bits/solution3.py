class Solution:
    def hammingWeight(self, n: int) -> int:
        n = ((n >> 1) & 0x55555555) + (n & 0x55555555)
        n = ((n >> 2) & 0x33333333) + (n & 0x33333333)
        n = ((n >> 4) & 0x0F0F0F0F) + (n & 0x0F0F0F0F)
        n = ((n >> 8) & 0x00FF00FF) + (n & 0x00FF00FF)
        n = ((n >> 16) & 0x0000FFFF) + (n & 0x0000FFFF)
        return n
