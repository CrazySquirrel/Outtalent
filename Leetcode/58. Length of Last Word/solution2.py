class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        s = s.strip()
        for c in s[::-1]:
            counter += 1
            if c == ' ': return counter - 1
        return counter
