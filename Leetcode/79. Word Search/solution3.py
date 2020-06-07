from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False

        board_count = Counter(chain(*board))
        word_count = Counter(word)

        if any(c > board_count[s] for s, c in word_count.items()): return False

        m, n, w = len(board), len(board[0]), len(word) - 1

        def dfs(d: int, x: int, y: int) -> bool:
            if word[d] != board[y][x]: return False
            if d == w: return True

            c, board[y][x] = board[y][x], ''

            if x > 0 and dfs(d + 1, x - 1, y): return True
            if x < n - 1 and dfs(d + 1, x + 1, y): return True
            if y > 0 and dfs(d + 1, x, y - 1): return True
            if y < m - 1 and dfs(d + 1, x, y + 1): return True

            board[y][x] = c

            return False

        return any(dfs(0, j, i) for i in range(m) for j in range(n) if word[0] == board[i][j])
