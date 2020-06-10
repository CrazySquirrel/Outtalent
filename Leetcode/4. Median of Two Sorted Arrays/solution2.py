class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n, m = len(a), len(b)
        if n > m: a, b, m, n = b, a, n, m
        l, r = 0, n
        if n == 0: raise ValueError
        while l <= r:
            i = l + (r - l) // 2
            j = (n + m + 1) // 2 - i
            if i < n and j > 0 and b[j - 1] > a[i]:
                l = i + 1
            elif i > 0 and j < m and b[j] < a[i - 1]:
                r = i - 1
            else:
                if i == 0:
                    median = b[j - 1]
                elif j == 0:
                    median = a[i - 1]
                else:
                    median = max(a[i - 1], b[j - 1])
                break
        if (n + m) % 2 == 1: return median
        if i == n: return (median + b[j]) / 2
        if j == m: return (median + a[i]) / 2
        return (median + min(a[i], b[j])) / 2.0
