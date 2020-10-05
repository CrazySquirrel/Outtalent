class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(result) or len(word) == len(result) and word < result:
                if all(word[:k] in wordset for k in range(1, len(word))): result = word
        return result
