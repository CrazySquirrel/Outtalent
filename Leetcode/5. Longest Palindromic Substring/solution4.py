class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        if strlen < 2 or s == s[::-1]: return s
        start, maxlen = 0, 1
        for i in range(strlen):
            oddstart = i - maxlen - 1
            evenstart = i - maxlen
            odd = s[oddstart:i + 1]
            even = s[evenstart:i + 1]
            if oddstart >= 0 and odd == odd[::-1]:
                start = oddstart
                maxlen += 2
            elif evenstart >= 0 and even == even[::-1]:
                start = evenstart
                maxlen += 1
        return s[start:start + maxlen]
