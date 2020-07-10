class Solution:
    def integerBreak(self, n: int) -> int:
        ret = max((2 + n & 1) * 2 ** (n // 2 - 1),
                  (3 + n % 3) * 3 ** (n // 3 - 1),
                  (n % 3) * 3 ** (n // 3))
        return 1 if n == 2 else 2 if n == 3 else ret
