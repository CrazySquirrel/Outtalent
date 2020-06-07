class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0

        m = len(grid)
        n = len(grid[0])

        grid[0][0] = 1

        for i in range(1, m):
            if grid[i][0] == 0:
                grid[i][0] = grid[i - 1][0]
            else:
                grid[i][0] = 0

        for i in range(1, n):
            if grid[0][i] == 0:
                grid[0][i] = grid[0][i - 1]
            else:
                grid[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = 0

        return grid[m - 1][n - 1]
