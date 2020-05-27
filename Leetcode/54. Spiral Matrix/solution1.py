class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if 0 == m: return []
        n = len(matrix[0])
        if 0 == n: return []
        result = []
        for x in range(0, (min(m, n) + 1) // 2):
            for y in range(x, n - x): result.append(matrix[x][y])
            for y in range(x + 1, m - x - 1): result.append(matrix[y][n - x - 1])
            if m - 2 * x > 1:
                for y in range(n - x - 1, x - 1, -1): result.append(matrix[m - x - 1][y])
            if n - 2 * x > 1:
                for y in range(m - x - 2, x, -1): result.append(matrix[y][x])
        return result
