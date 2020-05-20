class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        for h1 in range(2, -1, -1):
            for h2 in range(9, -1, -1):
                if h1 == 2 and h2 > 3: continue
                for m1 in range(5, -1, -1):
                    for m2 in range(59, -1, -1):
                        if sorted([h1, h2, m1, m2]) == A:
                            return '%d%d:%d%d' % (h1, h2, m1, m2)
        return ''
