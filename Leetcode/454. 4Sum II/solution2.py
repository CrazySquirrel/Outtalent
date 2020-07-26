from collections import Counter, defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a, b, c, d = Counter(A), Counter(B), Counter(C), Counter(D)

        sums = defaultdict(int)

        for i in a:
            for j in b:
                sums[i + j] += a[i] * b[j]

        result = 0

        for i in c:
            for j in d:
                s = 0 - i - j

                if s in sums:
                    result += sums[s] * c[i] * d[j]

        return result
