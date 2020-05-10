import numpy as np


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = np.matrix(matrix)
        for i in range(1, m.shape[0]):
            for j in range(1, m.shape[1]):
                if m[i, j] == 0: continue
                m[i, j] = min([m[i - 1, j], m[i, j - 1], m[i - 1, j - 1]]) + 1
        return np.sum(m)
