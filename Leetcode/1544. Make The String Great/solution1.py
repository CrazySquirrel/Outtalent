class Solution:
    def makeGood(self, s: str) -> str:
        if not s: return s
        for i in range(len(s) - 1):
            if s[i].lower() == s[i+1].lower() and (s[i].islower() != s[i+1].islower()):
                return self.makeGood(s[0:i] + s[i+2:])
        return s