class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3: return True

        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]: increasing = False
            if A[i] < A[i + 1]: decreasing = False

        return increasing or decreasing
