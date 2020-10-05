class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(self.reverseWord, s.split(' ')))

    def reverseWord(self, s: str) -> str:
        return s[::-1]
