class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle) and haystack[i + j] == needle[j]: j += 1
                if j == len(needle): return i
        return -1
