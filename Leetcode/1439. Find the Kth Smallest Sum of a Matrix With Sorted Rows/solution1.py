from itertools import product


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        return sum(sorted(product(*mat), key=lambda x: sum(x))[k - 1])
