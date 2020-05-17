class Solution:
    def judgeCircle(self, moves: str) -> bool:
        M = {
            'U': (0, -1),
            'D': (0, 1),
            'R': (1, 0),
            'L': (-1, 0)
        }

        x, y = 0, 0

        for move in moves:
            dx, dy = M[move]
            x += dx
            y += dy

        return x == 0 and y == 0
