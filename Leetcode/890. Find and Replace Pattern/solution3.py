class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str) -> bool:
            h = {}
            for p, w in zip(pattern, word):
                if h.setdefault(p, w) != w: return False
            return len(set(h.values())) == len(h.values())

        return list(filter(lambda word: match(word), words))
