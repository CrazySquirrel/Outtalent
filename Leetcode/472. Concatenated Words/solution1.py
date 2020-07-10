class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def search(word: str, c: int = 0) -> bool:
            if c > 0 and word in word_set: return True
            for i in range(1, len(word)):
                if word[:i] in word_set and search(word[i:], c + 1): return True
            return False

        word_set = set(words)
        return filter(search, words)
