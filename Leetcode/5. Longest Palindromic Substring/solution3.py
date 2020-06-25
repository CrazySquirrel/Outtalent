class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]: return s

        start, maxlen = 0, 1

        for i in range(len(s)):
            oddstart = i - maxlen - 1
            odd = s[oddstart:i + 1]

            if oddstart >= 0 and odd == odd[::-1]:
                start = oddstart
                maxlen += 2
                continue

            evenstart = i - maxlen
            even = s[evenstart:i + 1]

            if evenstart >= 0 and even == even[::-1]:
                start = evenstart
                maxlen += 1
                continue

        return s[start:start + maxlen]
