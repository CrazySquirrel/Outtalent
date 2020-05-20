from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or endWord not in wordList: return []

        word_list = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction, parents = 1, defaultdict(set)

        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1

            next_forward = set()
            word_list -= forward

            for word in forward:
                for i in range(len(word)):
                    p1, p2 = word[:i], word[i + 1:]
                    for new_word in word_list:
                        if new_word != word and new_word.startswith(p1) and new_word.endswith(p2):
                            next_forward.add(new_word)
                            if direction == 1:
                                parents[new_word].add(word)
                            else:
                                parents[word].add(new_word)

            if next_forward & backward:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[p] + r for r in res for p in parents[r[0]]]
                return res

            forward = next_forward

        return []
