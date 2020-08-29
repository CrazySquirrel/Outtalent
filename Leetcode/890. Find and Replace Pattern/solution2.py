from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str) -> bool:
            p2w = defaultdict(str)
            w2p = defaultdict(str)
            for p, w in zip(pattern, word):
                if p not in p2w and w not in w2p:
                    p2w[p] = w
                    w2p[w] = p
                if p2w[p] != w or w2p[w] != p: return False
            return True

        return list(filter(lambda word: match(word), words))
