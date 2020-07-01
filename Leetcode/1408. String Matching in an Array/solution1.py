class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = len(words)
        words.sort(key=lambda x: len(x))
        result = []
        for i in range(l - 1):
            for j in range(i + 1, l):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
