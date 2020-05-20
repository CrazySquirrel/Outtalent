class Solution:
    def diffByOneCharacter(self, word1: str, word2: str) -> bool:
        counter = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
                if counter > 1: return False

        return counter == 1

    def helper(self, beginWord: str, endWord: str, path: List[str]) -> List[List[str]]:
        if path[-1] == endWord: return [path]

        result = []

        for word in self.lookup_table.get(beginWord, []):
            if word in path: continue
            subresults = self.helper(word, endWord, path + [word])
            for subresult in subresults:
                if subresult and subresult[-1] == endWord:
                    result.append(subresult)

        return result

    def buildLookupTable(self, wordList: List[str]) -> None:
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self.diffByOneCharacter(wordList[i], wordList[j]):
                    if wordList[i] not in self.lookup_table:
                        self.lookup_table[wordList[i]] = []
                    self.lookup_table[wordList[i]].append(wordList[j])
                    if wordList[j] not in self.lookup_table:
                        self.lookup_table[wordList[j]] = []
                    self.lookup_table[wordList[j]].append(wordList[i])

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        self.lookup_table = {}
        self.buildLookupTable(wordList)

        result = self.helper(beginWord, endWord, [beginWord])

        if not result: return []

        min_length = len(min(result, key=lambda x: len(x)))

        return list(filter(lambda x: len(x) == min_length, result))
