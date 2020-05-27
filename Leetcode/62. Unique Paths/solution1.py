from itertools import permutations

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return len(set(permutations(['Right'] * (m-1) + ['Down'] * (n-1))))