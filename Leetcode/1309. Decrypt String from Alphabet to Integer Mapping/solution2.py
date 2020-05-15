class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i + 2] == '#':
                result.append(chr(int(s[i:i + 2]) + 96))
                i += 3
            else:
                result.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(result)
