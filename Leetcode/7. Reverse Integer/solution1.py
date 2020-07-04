class Solution:
    def reverse(self, x: int) -> int:
        INT_OVERFLOW = 214748364

        s = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x:
            pop = x % 10
            x //= 10

            if s == 1:
                if rev > INT_OVERFLOW or (rev == INT_OVERFLOW and pop > 7): return 0
            else:
                if rev > INT_OVERFLOW or (rev == INT_OVERFLOW and pop > 8): return 0

            rev = rev * 10 + pop

        return rev * s
