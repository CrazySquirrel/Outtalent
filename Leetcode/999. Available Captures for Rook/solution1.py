class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        M, N = len(board), len(board[0])

        def check(indices):
            for i, j in indices:
                if board[i][j] == 'B': return 0
                if board[i][j] == 'p': return 1
            return 0

        for i in range(M):
            for j in range(N):
                if board[i][j] == 'R':
                    return sum([
                        check(((i, j) for j in range(j + 1, N))),
                        check(((i, j) for i in range(i + 1, M))),
                        check(((i, j) for j in range(j - 1, -1, -1))),
                        check(((i, j) for i in range(i - 1, -1, -1))),
                    ])

        return 0
