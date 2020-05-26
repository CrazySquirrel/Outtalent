class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in s: result = result * 26 + ord(c) - 64
        return result
