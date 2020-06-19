class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        i = 1
        while i <= n:
            divider = i * 10
            res += n // divider * i
            res += min(max(n % divider - i + 1, 0), i)
            i *= 10
        return res
