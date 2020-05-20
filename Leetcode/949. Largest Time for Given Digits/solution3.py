class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort(reverse=True)
        for h1 in A:
            if h1 > 2: continue
            for h2 in A:
                if h1 >= 2 and h2 > 3: continue
                for m1 in A:
                    if m1 > 5: continue
                    for m2 in A:
                        if sorted([h1, h2, m1, m2], reverse=True) == A:
                            return '%d%d:%d%d' % (h1, h2, m1, m2)
        return ''
