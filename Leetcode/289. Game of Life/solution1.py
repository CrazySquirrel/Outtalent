class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        result = [[board[i][j] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                neighbors = sum(board[i + di][j + dj] for di, dj in directions if 0 <= i + di < m and 0 <= j + dj < n)

                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    result[i][j] = 0

                if board[i][j] == 0 and neighbors == 3:
                    result[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = result[i][j]
