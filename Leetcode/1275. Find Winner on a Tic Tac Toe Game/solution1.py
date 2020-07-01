import numpy as np


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = np.full((3, 3), '.')
        tag = 'A'
        for i, j in moves:
            grid[i, j] = tag
            if np.all(grid[i, :] == tag): return tag
            if np.all(grid[:, j] == tag): return tag
            if np.all(np.diag(grid) == tag): return tag
            if np.all(np.diag(np.fliplr(grid)) == tag): return tag
            tag = 'B' if tag == 'A' else 'A'
        return 'Pending' if len(moves) < 9 else 'Draw'
