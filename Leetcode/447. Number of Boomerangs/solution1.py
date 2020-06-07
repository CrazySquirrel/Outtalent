from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for x1, y1 in points:
            d = defaultdict(int)
            for x2, y2 in points: d[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for d, v in d.items(): result += v * (v - 1)
        return result
