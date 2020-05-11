class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        n = n - ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
        return n
