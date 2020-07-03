class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        worddict = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            count = len(word)

            for j in range(count + 1):
                prefix, subfix = word[:j], word[j:]
                reprefix, resubfix = prefix[::-1], subfix[::-1]

                if prefix == reprefix and resubfix in worddict:
                    m = worddict[resubfix]
                    if m != i: result.append([m, i])

                if j != count and subfix == resubfix and reprefix in worddict:
                    result.append([i, worddict[reprefix]])

        return result
