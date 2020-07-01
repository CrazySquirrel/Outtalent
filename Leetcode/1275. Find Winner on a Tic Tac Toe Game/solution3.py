class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[''] * 3 for _ in range(3)]

        for i, move in enumerate(moves):
            x, y = move
            grid[x][y] = 'B' if i % 2 else 'A'

        for i in range(3):
            x = grid[i][0]
            if x and x == grid[i][1] and x == grid[i][2]: return x

        for i in range(3):
            x = grid[0][i]
            if x and x == grid[1][i] and x == grid[2][i]: return x

        x = grid[0][0]

        if x and grid[1][1] == x and grid[2][2] == x: return x

        x = grid[0][2]

        if x and grid[1][1] == x and grid[2][0] == x: return x

        return "Pending" if len(moves) < 9 else "Draw"
