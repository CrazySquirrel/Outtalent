class Solution:
    def findComplement(self, num: int) -> int:
        p = 1
        while p < num: p = (p << 1) + 1
        return num ^ p
