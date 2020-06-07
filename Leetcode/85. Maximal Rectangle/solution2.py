class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        M, N = len(matrix), len(matrix[0])

        dp = [[0] * N for i in range(M)]

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                else:
                    dp[i][j] = 0

        result = 0

        for i in range(M):
            for j in range(N):
                l = inf
                for k in range(i, M):
                    l = min(l, dp[k][j])
                    if l == 0: break
                    result = max(result, l * (k - i + 1))

        return result
