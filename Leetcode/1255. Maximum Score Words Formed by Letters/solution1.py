from collections import Counter


class Solution:
    def contains(self, set1: Counter, set2: Counter) -> bool:
        for k in set2:
            if set1[k] < set2[k]:
                return False
        return True

    def helper(self, words: List[Counter], letters: Counter, score: List[int]) -> int:
        words = list(filter(lambda word: self.contains(letters, word), words))

        result = 0

        for i in range(len(words)):
            word = words[i]

            result = max(
                result,
                sum([score[ord(c) - 97] * word[c] for c in word]) + self.helper(words[i + 1:], letters - words[i],
                                                                                score)
            )

        return result

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        return self.helper([Counter(word) for word in words], Counter(letters), score)
