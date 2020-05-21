class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        index = [0] * 128
        j = i = 0
        while j < len(s):
            i = max(i, index[ord(s[j])])
            result = max(result, j - i + 1)
            index[ord(s[j])] = j + 1
            j += 1
        return result
