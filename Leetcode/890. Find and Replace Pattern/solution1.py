class Solution:
    letters = 'abcdefghijklmnopqrstuvwxyz'

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = self.remap(pattern)
        return list(filter(lambda w: self.remap(w) == p, words))

    def remap(self, word: str) -> str:
        h = {}
        i = 0
        result = ''
        for c in word:
            if c not in h:
                h[c] = Solution.letters[i]
                i += 1
            result += h[c]
        return result
