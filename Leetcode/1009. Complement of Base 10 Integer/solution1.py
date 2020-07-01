class Solution:
    def bitwiseComplement(self, N: int) -> int:
        mask = 1
        while N > mask: mask = mask * 2 + 1
        return mask - N
