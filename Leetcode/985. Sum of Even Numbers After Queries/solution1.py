class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S = sum([v for v in A if v % 2 == 0])
        result = []

        for v, i in queries:
            if A[i] % 2 == 0: S -= A[i]
            A[i] += v
            if A[i] % 2 == 0: S += A[i]
            result.append(S)

        return result
