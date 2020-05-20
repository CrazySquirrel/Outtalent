class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        if A[0] >= A[1] or A[-2] <= A[-1]: return False
        while len(A) > 1 and A[-1] < A[-2]: A.pop()
        while len(A) > 1 and A[-2] < A[-1]: A.pop()
        return len(A) == 1
