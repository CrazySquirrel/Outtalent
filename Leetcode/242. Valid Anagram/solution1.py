class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for c in s:
            if c not in h:
                h[c] = 0

            h[c] += 1

        for c in t:
            if c not in h:
                h[c] = 0

            h[c] -= 1

        for k in h:
            if h[k] != 0:
                return False

        return True
