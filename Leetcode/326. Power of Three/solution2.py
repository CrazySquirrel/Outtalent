class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n >= 1 and (log10(n) / log10(3)) % 1 == 0
