class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i): result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
