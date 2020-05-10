class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        counter = 0
        for size in range(1, min(len(matrix), len(matrix[0])) + 1):
            for i in range(0, len(matrix) - size + 1):
                for j in range(0, len(matrix[0]) - size + 1):
                    counter += sum([sum(m[j:j + size]) for m in matrix[i:i + size]]) == size ** 2
        return counter
