class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(filter(bool, s.split(' ')))[::-1])
