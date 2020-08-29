from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def board2str(board: List[List[int]]) -> str:
            return ''.join([str(board[i][j]) for i in range(2) for j in range(3)])

        start = board2str(board)
        bfs = deque([(start, 0)])
        visited = {start}

        while bfs:
            path, step = bfs.popleft()

            if path == "123450": return step

            p = path.index("0")

            x, y = p // 3, p % 3

            path = list(path)

            for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                tx, ty = x + nx, y + ny

                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3: continue

                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]

                path_str = "".join(path)
                if path_str not in visited:
                    bfs.append((path_str, step + 1))
                    visited.add(path_str)

                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]

        return -1
