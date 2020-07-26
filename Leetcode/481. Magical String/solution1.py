class Solution:
    def magicalString(self, n: int) -> int:
        S = [1, 2, 2]
        idx = 2
        while len(S) < n:
            S += [3 - S[-1]] * S[idx]
            idx += 1
        return S[:n].count(1)
