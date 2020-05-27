class Solution:
    def dfs(self, n: int, y: int, cols: List[int], diag1: List[int], diag2: List[int], board: List[List[str]], result: List[List[List[str]]]) -> None:
        for x in range(n):
            if not cols[x]: continue
            if not diag1[x + y]: continue
            if not diag2[x - y + n - 1]: continue
            board[y][x] = 'Q'
            cols[x] = diag1[x + y] = diag2[x - y + n - 1] = False
            if y == n - 1:
                result[0] += 1
            else:
                self.dfs(n, y + 1, cols, diag1, diag2, board, result)
            cols[x] = diag1[x + y] = diag2[x - y + n - 1] = True
            board[y][x] = '.'

    def totalNQueens(self, n: int) -> int:
        cols = [True] * n
        diag1 = [True] * (2 * n - 1)
        diag2 = [True] * (2 * n - 1)
        board = [['.'] * n for _ in range(n)]
        result = [0]
        self.dfs(n, 0, cols, diag1, diag2, board, result)
        return result[0]
