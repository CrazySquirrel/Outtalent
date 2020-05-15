class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            if i < len(s) - 2 and s[i + 2] == '#':
                result += chr(int(s[i:i + 2]) + ord('a') - 1)
                i += 3
            else:
                result += chr(int(s[i]) + ord('a') - 1)
                i += 1
        return result
