class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = set()
        ans = i = j = 0
        while i < n and j < n:
            if s[j] in h:
                h.remove(s[i])
                i += 1
            else:
                h.add(s[j])
                j += 1
                ans = max(ans, j - i)
        return ans
