from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        h = Counter([i.lower() for i in licensePlate if "A" <= i <= "z"])
        for word in sorted(words, key=len):
            if all(h[i] <= word.count(i) for i in h): return word
        return ''
