import numpy as np


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = np.full((3, 3), '.')

        for i, v in enumerate(moves): grid[v[0], v[1]] = 'B' if i % 2 else 'A'

        ab_set = {'A', 'B'}

        for i in range(3):
            s = set(grid[i, :])
            if len(s) == 1 and s & ab_set: return list(s)[0]

            s = set(grid[:, i])
            if len(s) == 1 and s & ab_set: return list(s)[0]

        s = set(np.diag(grid))
        if len(s) == 1 and s & ab_set: return list(s)[0]

        s = set(np.diag(np.fliplr(grid)))
        if len(s) == 1 and s & ab_set: return list(s)[0]

        return 'Pending' if len(moves) < 9 else 'Draw'
