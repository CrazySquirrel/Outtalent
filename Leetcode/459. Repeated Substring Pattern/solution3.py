class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        return (s + s)[1:-1].find(s) != -1
