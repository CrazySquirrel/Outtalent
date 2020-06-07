class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = '*'

        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0
