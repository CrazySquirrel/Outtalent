class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        M, N = len(matrix), len(matrix[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        max_len = 0

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])

        return max_len * max_len
