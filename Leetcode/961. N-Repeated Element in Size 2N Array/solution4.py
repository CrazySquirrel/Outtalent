class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(1, 4):
            for j in range(0, len(A) - i):
                if A[j] == A[i + j]:
                    return A[j]
