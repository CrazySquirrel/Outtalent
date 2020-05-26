class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n >= 5:
            n //= 5
            result += n
        return result
