class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        if A[0] >= A[1] or A[-2] <= A[-1]: return False
        growing = True
        for i in range(1, len(A) - 1):
            if A[i - 1] >= A[i]: growing = False
            if not growing and A[i - 1] <= A[i]: return False
        return True
