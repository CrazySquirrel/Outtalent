class Solution:
    def max_substr(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.max_substr(s, i, i), self.max_substr(s, i, i + 1), res, key=len)
        return res
