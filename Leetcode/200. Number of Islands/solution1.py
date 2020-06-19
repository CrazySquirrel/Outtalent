class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        M, N = len(grid), len(grid[0])

        counter = 2

        def dfs(i: int, j: int):
            grid[i][j] = counter
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == '1':
                    dfs(ni, nj)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    dfs(i, j)
                    counter += 1

        print(grid)

        return counter - 2
