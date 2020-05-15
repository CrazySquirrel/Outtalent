class Solution:
    def dfs(self, grid: List[List[int]], w: int, h: int, x: int, y: int, n: int) -> int:
        if not (0 <= x < w and 0 <= y < h and grid[y][x] > -1): return 0
        if grid[y][x] == 2: return n == 0

        grid[y][x] = -1

        paths = 0
        paths += self.dfs(grid, w, h, x + 1, y, n - 1)
        paths += self.dfs(grid, w, h, x - 1, y, n - 1)
        paths += self.dfs(grid, w, h, x, y + 1, n - 1)
        paths += self.dfs(grid, w, h, x, y - 1, n - 1)

        grid[y][x] = 0

        return paths

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        w, h, x, y, n = len(grid[0]), len(grid), -1, -1, 1
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    n += 1
                elif grid[i][j] == 1:
                    x, y = j, i

        return self.dfs(grid, w, h, x, y, n)
