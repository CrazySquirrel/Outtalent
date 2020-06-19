class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3: return True
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))
