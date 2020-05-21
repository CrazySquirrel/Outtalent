class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, tmp = 0, []
        for c in s:
            result = max(result, len(tmp))
            while c in tmp: tmp.pop(0)
            tmp.append(c)
        return max(result, len(tmp))
