class Solution:
    def helper(self, board: List[List[str]], word: str, s: int, i: int, j: int, m: int, n: int) -> bool:
        if s == len(word): return True
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and word[s] == board[ni][nj]:
                c, board[ni][nj] = board[ni][nj], '*'
                if self.helper(board, word, s + 1, ni, nj, m, n): return True
                board[ni][nj] = c
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    c, board[i][j] = board[i][j], '*'
                    if self.helper(board, word, 1, i, j, m, n): return True
                    board[i][j] = c
        return False
