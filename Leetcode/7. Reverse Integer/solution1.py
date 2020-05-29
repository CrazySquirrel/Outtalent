class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = 2147483648  # without sign

        s = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x:
            pop = x % 10
            x //= 10

            if s == 1:
                if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7): return 0
            else:
                if rev > INT_MIN // 10 or (rev == INT_MIN // 10 and pop > 8): return 0

            rev = rev * 10 + pop

        return rev * s
