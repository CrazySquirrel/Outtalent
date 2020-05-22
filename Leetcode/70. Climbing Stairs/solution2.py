class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(1, n): a, b = b, a + b
        return a
