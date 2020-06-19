class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n: n = n & (n - 1)
        return m & n
