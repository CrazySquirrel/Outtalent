from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if set(s) != set(t): return (set(t) - set(s)).pop()
        s = Counter(s)
        t = Counter(t)
        for i, j in s.items():
            if j != t[i]: return i
        return ''
