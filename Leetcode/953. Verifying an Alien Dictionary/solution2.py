class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}

        def compare(word1, word2):
            fl = len(word1)
            sl = len(word2)
            i = j = 0

            while i < fl and j < sl:
                if word1[i] != word2[j]: return order[word1[i]] < order[word2[j]]

                i += 1
                j += 1

            return sl >= fl

        l = len(words)

        for i in range(1, l):
            if not compare(words[i - 1], words[i]): return False

        return True
