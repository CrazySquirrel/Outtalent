from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum([(v * (v - 1)) // 2 for v in Counter([tuple(sorted(v)) for v in dominoes]).values()])
