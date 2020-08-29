class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        res = sum(mat[i][i] + mat[i][~i] for i in range(m))
        if m & 1: res -= mat[m // 2][m // 2]
        return res
