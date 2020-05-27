class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]

                if e == '.': continue

                ind = i // 3 * 3 + j // 3

                if e in (row[i] | col[j] | grid[ind]): return False

                row[i].add(e)
                col[j].add(e)
                grid[ind].add(e)

        return True
