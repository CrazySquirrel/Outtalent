class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])

        result = [[0] * C for _ in range(R)]

        if R == 1 and C == 1: return M

        if R == 1:
            result[0][0] = (M[0][0] + M[0][1]) // 2
            result[0][-1] = (M[0][-2] + M[0][-1]) // 2

            for i in range(1, C - 1): result[0][i] = (M[0][i - 1] + M[0][i] + M[0][i + 1]) // 3

            return result

        if C == 1:
            result[0][0] = (M[0][0] + M[1][0]) // 2
            result[-1][0] = (M[-2][0] + M[-1][0]) // 2

            for i in range(1, R - 1): result[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0]) // 3

            return result

        result[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        result[0][-1] = (M[0][-2] + M[0][-1] + M[1][-1] + M[1][-2]) // 4
        result[-1][0] = (M[-2][0] + M[-1][0] + M[-1][1] + M[-2][1]) // 4
        result[-1][-1] = (M[-2][-2] + M[-2][-1] + M[-1][-2] + M[-1][-1]) // 4

        for i in range(1, R - 1):
            result[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0] + M[i - 1][1] + M[i][1] + M[i + 1][1]) // 6
            result[i][-1] = (M[i - 1][-1] + M[i][-1] + M[i + 1][-1] + M[i - 1][-2] + M[i][-2] + M[i + 1][-2]) // 6

        for j in range(1, C - 1):
            result[0][j] = (M[0][j - 1] + M[0][j] + M[0][j + 1] + M[1][j - 1] + M[1][j] + M[1][j + 1]) // 6
            result[-1][j] = (M[-1][j - 1] + M[-1][j] + M[-1][j + 1] + M[-2][j - 1] + M[-2][j] + M[-2][j + 1]) // 6

        for i in range(1, R - 1):
            for j in range(1, C - 1):
                result[i][j] = (M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j - 1] + M[i][j] + M[i][j + 1] +
                                M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) // 9

        return result
