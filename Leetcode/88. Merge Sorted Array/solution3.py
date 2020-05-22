class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not B: return None
        i, j = m - 1, n - 1
        t = len(A) - 1
        while i >= 0 or j >= 0:
            if i < 0 or (j >= 0 and B[j] > A[i]):
                A[t] = B[j]
                j -= 1
            else:
                A[t] = A[i]
                i -= 1
            t -= 1
