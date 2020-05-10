class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_counter = 0

        while n:
            if n & 1:  ones_counter += 1  # or ones_counter += n & 1
            n >>= 1

        return ones_counter
