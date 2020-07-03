class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0

        H = len(citations)
        d = collections.Counter()

        for c in citations: d[min(c, H)] += 1

        s = d[H]

        while H > s:
            H -= 1
            s += d[H]

        return H
