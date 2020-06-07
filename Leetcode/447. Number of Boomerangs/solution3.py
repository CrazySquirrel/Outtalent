from scipy.spatial.distance import cdist
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        distances = cdist(points, points, 'euclidean')
        result = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(len(points)): d[distances[i][j]] += 1
            for d, v in d.items(): result += v * (v - 1)
        return result
