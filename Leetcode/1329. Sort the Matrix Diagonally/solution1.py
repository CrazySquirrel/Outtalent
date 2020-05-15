class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = [[] for i in range(m + n)]
        for i in range(m):
            for j in range(n):
                q[i - j + n].append(mat[i][j])
        q = list(map(lambda x: sorted(x, reverse=True), q))
        for i in range(m):
            for j in range(n):
                mat[i][j] = q[i - j + n].pop()
        return mat
