class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_counter = 0

        while n:
            ones_counter += 1
            n &= (n - 1)

        return ones_counter
