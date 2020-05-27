class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0: return max(i, j) + 1
            return dp(i - 1, j - 1) if word1[i] == word2[j] else min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1)) + 1

        return dp(len(word1) - 1, len(word2) - 1)
