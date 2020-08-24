class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat: return []

        m = len(mat)
        n = len(mat[0])

        get = lambda i, j: mat[i][j] if 0 <= i < m and 0 <= j < n else 0
        row = lambda i, j: sum([get(i, y) for y in range(j - K, j + K + 1)])
        col = lambda i, j: sum([get(x, j) for x in range(i - K, i + K + 1)])

        answer = [[0] * n for _ in range(m)]

        for i in range(0, K + 1):
            for j in range(0, K + 1):
                answer[0][0] += get(i, j)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if j == 0:
                    answer[i][j] = answer[i - 1][j] - row(i - K - 1, j) + row(i + K, j)
                else:
                    answer[i][j] = answer[i][j - 1] - col(i, j - K - 1) + col(i, j + K)

        return answer
