class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        mid = A.index(max(A))
        return 0 < mid < len(A) - 1 and all(A[i] < A[i + 1] for i in range(0, mid)) and all(A[i - 1] > A[i] for i in range(mid + 1, len(A)))