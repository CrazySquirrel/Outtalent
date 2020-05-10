import numpy as np


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = np.matrix(matrix)
        h = len(matrix)
        w = len(matrix[0])
        counter = 0
        for size in range(1, min(h, w) + 1):
            for i in range(0, h - size + 1):
                for j in range(0, w - size + 1):
                    counter += np.all(m[i:i + size, j:j + size])
        return counter
