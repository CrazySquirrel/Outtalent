class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        a = 1
        b = 1
        for i in range(1, n):
            a, b = b, a + b
        return a
