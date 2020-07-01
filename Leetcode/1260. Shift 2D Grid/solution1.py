import numpy as np


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid = np.array(grid)

        for i in range(k):
            grid[:, -1] = np.roll(grid[:, -1], 1)
            grid = np.roll(grid, 1, axis=1)

        return grid
