class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(map(lambda c: chr(c + 32 if 64 < c < 91 else c), [ord(i) for i in s]))
