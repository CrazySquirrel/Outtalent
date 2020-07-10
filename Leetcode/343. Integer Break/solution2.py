class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        m = 1
        while True:
            if n > 4:
                m *= 3
                n -= 3
            else:
                m *= n
                break

        return m
