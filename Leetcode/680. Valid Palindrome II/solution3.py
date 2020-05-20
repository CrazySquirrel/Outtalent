class Solution:
    def validPalindrome(self, s1: str) -> bool:
        if s1 == s1[::-1]: return True

        s2 = s1[::-1]

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1 = s1[:i] + s1[i + 1:]
                s2 = s2[:i] + s2[i + 1:]
                return s1 == s1[::-1] or s2 == s2[::-1]

        return True
