from itertools import product


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        return sorted(map(lambda x: sum(x), product(*mat)))[k - 1]
