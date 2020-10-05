class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        t = n & 1
        n >>= 1
        while n:
            if (n & 1) == t: return False
            t = n & 1
            n >>= 1
        return True
