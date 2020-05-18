class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split(' ')[::-1]:
            if word: result.append(word)
        return ' '.join(result)
