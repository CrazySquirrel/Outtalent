class Solution:
    def reverseBits(self, n: int) -> int:
        revert_bits = 0

        for i in range(32):
            revert_bits <<= 1
            revert_bits |= n & 1
            n >>= 1

        return revert_bits
