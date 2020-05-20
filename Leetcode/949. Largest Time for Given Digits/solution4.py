from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for h1, h2, m1, m2 in permutations(sorted(A, reverse=True)):
            h = 10 * h1 + h2
            m = 10 * m1 + m2
            if 0 <= h <= 23 and 0 <= m <= 59:
                return '%d%d:%d%d' % (h1, h2, m1, m2)
        return ''
