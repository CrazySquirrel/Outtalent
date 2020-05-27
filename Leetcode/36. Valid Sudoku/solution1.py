class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for cell in row:
                if cell == '.': continue
                if cell in s: return False
                s.add(cell)

        for col in zip(*board):
            s = set()
            for cell in col:
                if cell == '.': continue
                if cell in s: return False
                s.add(cell)

        for i in range(0, 10, 3):
            for j in range(0, 10, 3):
                s = set()
                for row in board[i:i + 3]:
                    for cell in row[j:j + 3]:
                        if cell == '.': continue
                        if cell in s: return False
                        s.add(cell)

        return True
