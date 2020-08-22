class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s) - 1:
            if i >= 0 and s[i].lower() == s[i + 1].lower() and (s[i].islower() != s[i + 1].islower()):
                s.pop(i)
                s.pop(i)
                i -= 1
            else:
                i += 1
        return ''.join(s)
