class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                        dp[i][j] = True
                    elif dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True

        return dp[len(s1)][len(s2)]
