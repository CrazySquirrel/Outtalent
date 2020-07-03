class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0

        N = len(citations)

        l, r = 0, N - 1

        H = 0

        while l <= r:
            m = l + (r - l) // 2

            H = max(H, min(citations[m], N - m))

            if citations[m] < N - m:
                l = m + 1
            else:
                r = m - 1

        return H
