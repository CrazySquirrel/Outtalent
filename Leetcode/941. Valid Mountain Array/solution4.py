class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] >= A[1] or A[-2] <= A[-1]: return False
        i = len(A)
        while i > 1 and A[i - 1] < A[i - 2]: i -= 1
        while i > 1 and A[i - 2] < A[i - 1]: i -= 1
        return i == 1
