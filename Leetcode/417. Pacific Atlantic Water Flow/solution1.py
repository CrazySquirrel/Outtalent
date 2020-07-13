class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return

        row, col = len(matrix), len(matrix[0])

        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]

        def dfs(i: int, j: int, height: List[List[bool]], reached: List[List[bool]]):
            if not 0 <= i < row or not 0 <= j < col or reached[i][j] or matrix[i][j] < height: return

            reached[i][j] = True

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + x, j + y, matrix[i][j], reached)

        for i in range(row):
            dfs(i, 0, -1, pacific)
            dfs(i, col - 1, -1, atlantic)

        for i in range(col):
            dfs(0, i, -1, pacific)
            dfs(row - 1, i, -1, atlantic)

        result = []

        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    result.append((i, j))

        return result
