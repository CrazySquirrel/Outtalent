from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        counter = Counter(chars)

        for word in words:
            word_counter = Counter(word)

            for k in word_counter:
                if word_counter[k] > counter[k]: break
            else:
                result += len(word)

        return result
