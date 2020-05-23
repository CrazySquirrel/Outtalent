from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        if not all([word in s for word in words]): return []

        words_counter = Counter(words)
        words_length = len(words)

        word_length = len(words[0])

        result = []

        for i in range(len(s) - word_length * words_length + 1):
            j, dic = 0, defaultdict(int)

            while j < words_length:
                k = i + word_length * j

                word = s[k:k + word_length]

                dic[word] += 1

                if dic[word] > words_counter[word]: break

                j += 1

            if j == words_length: result.append(i)

        return result
