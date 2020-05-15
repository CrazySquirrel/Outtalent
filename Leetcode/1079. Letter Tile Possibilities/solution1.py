import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return sum([len(set(itertools.permutations(tiles, i + 1))) for i in range(len(tiles))])
