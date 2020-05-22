class Solution:
    def helper(self, n: int):
        if n == 0:
            return (0, 1)
        else:
            a, b = self.helper(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    def climbStairs(self, n: int) -> int:
        if n <= 0: return 0
        return self.helper(n)[1]
