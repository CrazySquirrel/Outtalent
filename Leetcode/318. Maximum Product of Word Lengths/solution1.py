class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = len(words)
        result = 0

        for i in range(l - 1):
            for j in range(i + 1, l):
                k = len(words[i]) * len(words[j])
                if k < result or set(words[i]).intersection(words[j]): continue
                result = k

        return result
