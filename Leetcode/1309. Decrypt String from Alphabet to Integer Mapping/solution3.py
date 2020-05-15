class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = ''
        while i >= 0:
            if s[i] == '#':
                res = chr(int(s[i - 2: i]) + 96) + res
                i -= 3
            else:
                res = chr(int(s[i]) + 96) + res
                i -= 1
        return res
