class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for i in range(n)]
        num_layers = n // 2
        j = 1
        for l in range(num_layers):
            for i in range(n - 2 * l - 1):
                result[l][l + i] = j
                j += 1
            for i in range(n - 2 * l - 1):
                result[l + i][n - 1 - l] = j
                j += 1
            for i in range(n - 2 * l - 1):
                result[n - 1 - l][n - 1 - l - i] = j
                j += 1
            for i in range(n - 2 * l - 1):
                result[n - 1 - l - i][l] = j
                j += 1
        if n % 2 == 1: result[n // 2][n // 2] = j
        return result
