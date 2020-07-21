class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    if row > 0 and board[row - 1][col] == "X":
                        continue
                    if col > 0 and board[row][col - 1] == "X":
                        continue
                    res += 1
        return res
