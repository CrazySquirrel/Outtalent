class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        return max(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]), key=lambda x: len(x))
