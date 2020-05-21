class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        l, r = 0, 0
        for i in range(len(s)):
            start, end = i, i
            while start >= 0:
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and (s[start] == s[end])
                if dp[start][end] and (end - start + 1) > (r - l + 1):
                    l, r = start, end
                start = start - 1
        return s[l:r + 1]
