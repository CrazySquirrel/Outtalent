class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, h = 0, len(A) - 1
        while l <= h:
            m = l + (h - l) // 2
            if A[m] < A[m + 1]:
                l = m + 1
            else:
                h = m - 1
        return l
