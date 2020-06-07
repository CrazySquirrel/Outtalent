class Solution:
    def findComplement(self, num: int) -> int:
        all_ones = 1
        while all_ones <= num: all_ones <<= 1
        all_ones -= 1
        return all_ones ^ num
