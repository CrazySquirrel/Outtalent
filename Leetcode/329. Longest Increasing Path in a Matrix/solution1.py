class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(i: int, j: int):
            r = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[i][j] > matrix[ni][nj]:
                    r = max(r, dfs(ni, nj))
            return r + 1

        result = 0

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
