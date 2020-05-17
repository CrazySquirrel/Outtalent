class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row = [1e5 + 1] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])

        result = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == col[j]:
                    result.append(row[i])

        return result
