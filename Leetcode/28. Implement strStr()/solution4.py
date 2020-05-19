class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if n == 0: return 0
        if n > m: return -1

        failures = [-1 for i in range(n)]
        j = -1

        for i in range(1, n):
            while j >= 0 and needle[j + 1] != needle[i]: j = failures[j]
            if needle[j + 1] == needle[i]: j += 1
            failures[i] = failures[j] if i < n - 1 and needle[j + 1] == needle[i + 1] else j

        j = -1
        for i in range(0, m):
            while j >= 0 and needle[j + 1] != haystack[i]: j = failures[j]
            if needle[j + 1] == haystack[i]: j += 1
            if j == n - 1: return i - n + 1

        return -1
