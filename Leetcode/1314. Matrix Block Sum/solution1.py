class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat: return []

        m = len(mat)
        n = len(mat[0])

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for x in range(max(0, i - K), min(i + K + 1, m)):
                    for y in range(max(0, j - K), min(j + K + 1, n)):
                        answer[i][j] += mat[x][y]

        return answer
