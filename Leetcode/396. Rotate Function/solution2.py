class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        total = sum(A)
        ans = cur = sum(i * v for i, v in enumerate(A))
        for v in A[n - 1: 0: -1]:
            cur += total - n * v
            ans = max(ans, cur)
        return ans
