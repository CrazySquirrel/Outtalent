from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for c in counter2:
            if counter1[c] != counter2[c]: return c
        return ''
