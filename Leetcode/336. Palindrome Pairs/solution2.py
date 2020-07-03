class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {word[::-1]: i for i, word in enumerate(words)}

        result = []

        for i, word in enumerate(words):
            for j in range(len(word)):
                left, right = word[:j], word[j:]

                if left in dic and right == right[::-1] and dic[left] != i:
                    result.append([i, dic[left]])

                    if left == '': result.append([dic[left], i])

                if right in dic and left == left[::-1] and dic[right] != i:
                    result.append([dic[right], i])

        return result
