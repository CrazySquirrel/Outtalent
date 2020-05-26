class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(set(s)) != len(set(t)): return False
        h = {}
        for i in range(len(s)):
            if s[i] not in h: h[s[i]] = t[i]
            if h[s[i]] != t[i]: return False
        return True
