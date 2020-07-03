class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)
        while s[:i] != s[:i][::-1]: i -= 1
        return s[i:][::-1] + s
