class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = 1 << 31  # without sign
        INT_MAX = INT_MIN - 1

        s = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x:
            rev = rev * 10 + x % 10
            if INT_MIN < rev: return 0
            x //= 10

        rev *= s

        return rev if -INT_MIN < rev < INT_MAX else 0
