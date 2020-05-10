class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h = [0] * 256

        for i in range(len(s)):
            h[ord(s[i])] += 1
            h[ord(t[i])] -= 1

        for c in h:
            if c != 0:
                return False

        return True
