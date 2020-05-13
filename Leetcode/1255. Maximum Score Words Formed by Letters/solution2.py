from collections import Counter


class Solution:
    def contains(self, set1: Counter, set2: Counter) -> bool:
        for k in set2:
            if set1[k] < set2[k]:
                return False
        return True

    def helper(self, words: List[Counter], start: int, letters: Counter, score: List[int]) -> int:
        result = 0

        for i in range(start, len(words)):
            word = words[i]

            if self.contains(letters, word):
                result = max(
                    result,
                    sum([score[ord(c) - 97] * word[c] for c in word]) + self.helper(words, i + 1, letters - word, score)
                )

        return result

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        return self.helper([Counter(word) for word in words], 0, Counter(letters), score)
