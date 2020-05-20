from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = (-inf, -inf, -inf, -inf)
        for h1, h2, m1, m2 in permutations(A):
            h = 10 * h1 + h2
            m = 10 * m1 + m2
            if 0 <= h <= 23 and 0 <= m <= 59 and (h1, h2, m1, m2) > time:
                time = (h1, h2, m1, m2)
        return '%d%d:%d%d' % time if time[0] >= 0 else ''
