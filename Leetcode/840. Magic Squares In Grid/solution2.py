import numpy as np


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)

        magic = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

        rows = [set(row) for row in grid]
        cols = [set(col) for col in zip(*grid)]

        cols_i = []
        for i in range(len(cols) - 2):
            if magic.issubset(cols[i] | cols[i + 1] | cols[i + 2]): cols_i.append(i)

        rows_i = []
        for i in range(len(rows) - 2):
            if magic.issubset(rows[i] | rows[i + 1] | rows[i + 2]): rows_i.append(i)

        result = 0

        for row_i in rows_i:
            for col_i in cols_i:
                magic_grid = grid[row_i:row_i + 3, col_i:col_i + 3]
                if set.union(*map(set, magic_grid)) != magic: continue
                magic_sum = sum(magic_grid.diagonal())
                if magic_sum != sum(magic_grid[::-1].diagonal()): continue
                if not all([sum(row) == magic_sum for row in magic_grid]): continue
                if not all([sum(col) == magic_sum for col in zip(*magic_grid)]): continue
                result += 1

        return result
