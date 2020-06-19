class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = m
        for i in range(m + 1, n + 1): result &= i
        return result
