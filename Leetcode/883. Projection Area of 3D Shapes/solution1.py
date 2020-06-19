class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        result = 0
        for i in range(N):
            best_row = best_col = 0
            for j in range(N):
                if grid[i][j]: result += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            result += best_row + best_col
        return result
