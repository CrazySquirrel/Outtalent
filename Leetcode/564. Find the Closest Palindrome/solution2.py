class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if not n: return '-1'

        nlen = len(n)
        num = int(n)

        if num < 10: return str(num - 1)
        if num == 10 ** (nlen) - 1: return str(10 ** (nlen) + 1)
        if (num - 10 ** (nlen - 1)) in [0, 1]: return str(10 ** (nlen - 1) - 1)

        halfnum = n[:nlen // 2]

        cands = []

        if nlen % 2:
            cands.append(halfnum + n[nlen // 2] + halfnum[::-1])
            for d in [-1, 1]:
                prefix = str(int(n[:nlen // 2 + 1]) + d)
                cands.append(prefix + prefix[:-1][::-1])
        else:
            cands.append(halfnum + halfnum[::-1])
            for d in [-1, 1]:
                prefix = str(int(n[:nlen // 2]) + d)
                cands.append(prefix + prefix[::-1])

        return min(sorted(cands), key=lambda x: abs(num - int(x)) if x != n else inf)
