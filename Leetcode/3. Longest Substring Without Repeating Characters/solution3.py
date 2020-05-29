class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = {}
        ans = i = 0
        for j in range(n):
            if s[j] in h:
                i = max(i, h[s[j]])
            ans = max(ans, j - i + 1)
            h[s[j]] = j + 1
        return ans
