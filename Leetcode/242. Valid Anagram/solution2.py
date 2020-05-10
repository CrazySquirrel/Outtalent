class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h = {}

        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = 0

            h[s[i]] += 1

            if t[i] not in h:
                h[t[i]] = 0

            h[t[i]] -= 1

        for k in h:
            if h[k] != 0:
                return False

        return True
