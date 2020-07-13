class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)

        if n <= 1: return 0
        if n == 2: return max(A)

        result = -inf

        for i in range(n):
            result = max(result, sum([((j + i) % n) * v for j, v in enumerate(A)]))

        return result
