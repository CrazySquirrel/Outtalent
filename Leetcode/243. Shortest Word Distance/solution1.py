class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)
        i1 = i2 = -1
        for i, word in enumerate(words):
            if word == word1: i1 = i
            if word == word2: i2 = i
            if i1 != -1 and i2 != -1: result = min(result, abs(i1 - i2))
        return result
