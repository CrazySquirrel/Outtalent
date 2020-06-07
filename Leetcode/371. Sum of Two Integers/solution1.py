class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        while b != 0: a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return ~(a ^ MASK) if (a >> 31) & 1 else a
