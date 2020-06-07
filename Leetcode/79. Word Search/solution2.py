class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, w = len(board), len(board[0]), len(word) - 1

        def dfs(d: int, x: int, y: int) -> bool:
            if word[d] != board[y][x]: return False
            if d == w: return True

            c, board[y][x] = board[y][x], '*'

            if x > 0 and dfs(d + 1, x - 1, y): return True
            if x < n - 1 and dfs(d + 1, x + 1, y): return True
            if y > 0 and dfs(d + 1, x, y - 1): return True
            if y < m - 1 and dfs(d + 1, x, y + 1): return True

            board[y][x] = c

            return False

        return any(dfs(0, j, i) for i in range(m) for j in range(n))
