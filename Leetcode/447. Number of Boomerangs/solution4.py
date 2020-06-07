import numpy as np
from scipy.spatial.distance import pdist, squareform


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist_counter(dis):
            m = np.unique(dis, return_counts=True)[1]
            return np.sum(m * (m - 1))

        return sum(dist_counter(x) for x in squareform(pdist(np.array(points))))
