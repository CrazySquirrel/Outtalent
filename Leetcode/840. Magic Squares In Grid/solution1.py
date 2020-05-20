MAGIC = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                a, b, c = grid[i][j: j + 3]
                d, e, f = grid[i + 1][j: j + 3]
                g, h, k = grid[i + 2][j: j + 3]
                if not ({a, b, c, d, e, f, g, h, k} == MAGIC): continue
                if not (15 == a + b + c == d + e + f == g + h + k): continue
                if not (15 == a + d + g == b + e + h == c + f + k): continue
                if not (15 == a + e + k == c + e + g): continue
                result += 1

        return result
