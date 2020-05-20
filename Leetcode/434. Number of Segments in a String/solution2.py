class Solution:
    def countSegments(self, s: str) -> int:
        if not s: return 0
        counter = 0
        for i in range(1, len(s)):
            if s[i] == ' ' and s[i - 1] != ' ': counter += 1
        if s[-1] != ' ': counter += 1
        return counter
