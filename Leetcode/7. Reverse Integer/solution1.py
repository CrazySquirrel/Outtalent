class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        x = abs(x)
        r = 0

        while x:
            r = r * 10 + x % 10
            x //= 10

        r *= s

        if -2 ** 31 < r < 2 ** 31 - 1:
            return r
        else:
            return 0
