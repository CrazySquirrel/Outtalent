class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        if K <= 0: return sum(A)
        A.sort()

        is_zero = False
        min_v = inf

        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] = -A[i]
                K -= 1
                if K <= 0: return sum(A)
            if A[i] == 0: is_zero = True
            min_v = min(min_v, A[i])

        if is_zero or K % 2 == 0: return sum(A)

        return sum(A) - 2 * min_v
