from numpy import zeros, copy
from itertools import accumulate

M = 1e9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        k, m = k + 1, m + 1
        f1 = zeros((k, m))
        f1[1, 1:] = 1

        for _ in range(1, n):
            f2 = copy(f1)
            for j in range(1, k):
                item2s = list(accumulate(f1[j - 1]))
                for c in range(1, m):
                    f2[j, c] = (f1[j, c] * c + item2s[c - 1]) % M
            f1 = f2
        return int(sum(f1[k - 1, 1:]) % M)
