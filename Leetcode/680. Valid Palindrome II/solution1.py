class Solution:
    def isPalindrom(self, s: str, t: int) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                if t == 0: return False
                return self.isPalindrom(s[:i] + s[i + 1:], t - 1) or self.isPalindrom(s[:j] + s[j + 1:], t - 1)
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrom(s, 1)