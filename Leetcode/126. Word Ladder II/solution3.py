from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_list = set(wordList)
        res = []
        layer = defaultdict(list)
        layer[beginWord] = [[beginWord]]

        while layer:
            new_layer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            new_word = w[:i] + c + w[i + 1:]
                            if new_word in word_list:
                                new_layer[new_word] += [j + [new_word] for j in layer[w]]
            word_list -= set(new_layer.keys())
            layer = new_layer

        return res
