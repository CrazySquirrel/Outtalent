class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = [0] * 128
        ans = i = 0
        for j in range(n):
            i = max(i, h[ord(s[j])])
            ans = max(ans, j - i + 1)
            h[ord(s[j])] = j + 1
        return ans
