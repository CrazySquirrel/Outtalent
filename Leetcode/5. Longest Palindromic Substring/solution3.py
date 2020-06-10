class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        l = r = 0
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and (j - i + 1) > (r - l + 1):
                    l, r = i, j
        return s[l:r + 1]
