class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_square(N):
            return int(N ** 0.5) ** 2 == N

        return any(is_square(c - a ** 2) for a in range(int(c ** 0.5) + 1))
