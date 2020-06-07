class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for p in range(2, len(s) + 1):
            if len(s) % p == 0 and s[:len(s) // p] * p == s: return True
        return False
