class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1: return 1
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))
