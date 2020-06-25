class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1

        alphabet = set(haystack)

        last = {letter: needle.rfind(letter) for letter in alphabet}

        n = len(needle)
        m = len(haystack)

        i = n - 1
        j = n - 1

        while i < m:
            if haystack[i] == needle[j]:
                if j == 0:
                    return i
                else:
                    i -= 1
                    j -= 1
            else:
                l = last[haystack[i]]
                i = i + n - min(j, 1 + l)
                j = n - 1

        return -1
