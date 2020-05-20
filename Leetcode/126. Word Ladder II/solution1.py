class Solution:
    def diffByOneCharacter(self, word1: str, word2: str) -> bool:
        counter = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1

        return counter == 1

    def helper(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord == endWord: return [[endWord]]

        result = []

        for i in range(len(wordList)):
            word = wordList.pop(i)
            if self.diffByOneCharacter(beginWord, word):
                subresults = self.helper(word, endWord, wordList)
                for subresult in subresults:
                    if subresult and subresult[-1] == endWord:
                        result.append([beginWord] + subresult)
            wordList.insert(i, word)

        return result

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []

        result = self.helper(beginWord, endWord, wordList)

        if not result: return []

        min_length = len(min(result, key=lambda x: len(x)))

        return list(filter(lambda x: len(x) == min_length, result))