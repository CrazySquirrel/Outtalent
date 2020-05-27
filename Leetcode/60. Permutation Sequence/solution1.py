from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = permutations(range(1, n + 1))
        for i in range(k - 1): p.__next__()
        return ''.join(map(str, p.__next__()))
