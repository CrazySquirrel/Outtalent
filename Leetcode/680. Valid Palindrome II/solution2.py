class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                s1 = s[:i] + s[i + 1:]
                s2 = s[:j] + s[j + 1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            i += 1
            j -= 1

        return True
