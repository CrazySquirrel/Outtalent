class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat: return []

        M = len(mat)
        N = len(mat[0])

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for r in range(1, M + 1):
            for c in range(1, N + 1):
                dp[r][c] = mat[r - 1][c - 1] - dp[r - 1][c - 1] + dp[r - 1][c] + dp[r][c - 1]

        res = [[0] * N for _ in range(M)]

        for r in range(M):
            for c in range(N):
                r0, c0 = max(r - K, 0), max(c - K, 0)
                r1, c1 = min(r + K + 1, M), min(c + K + 1, N)
                res[r][c] = dp[r1][c1] - dp[r0][c1] - dp[r1][c0] + dp[r0][c0]

        return res
