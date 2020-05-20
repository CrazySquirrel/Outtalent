class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()

        h = []
        for h1 in range(2, -1, -1):
            for h2 in range(9, -1, -1):
                if h1 == 2 and h2 > 3: continue
                if h1 in A and h2 in A: h.append((h1, h2))

        m = []
        for m1 in range(5, -1, -1):
            for m2 in range(59, -1, -1):
                if m1 in A and m2 in A: m.append((m1, m2))

        for h1, h2 in h:
            for m1, m2 in m:
                if sorted([h1, h2, m1, m2]) == A:
                    return '%d%d:%d%d' % (h1, h2, m1, m2)

        return ''
