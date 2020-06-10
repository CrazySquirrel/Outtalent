from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        if not all([word in s for word in words]): return []

        words_counter = Counter(words)
        words_count = len(words)
        word_len = len(words[0])

        result = []

        for i in range(len(s) - word_len * words_count + 1):
            h = defaultdict(int)

            for j in range(words_count):
                k = i + j * word_len
                word = s[k:k + word_len]
                h[word] += 1

                if h[word] > words_counter[word]: break
            else:
                result.append(i)

        return result
