class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not m: return None
        r = len(m)
        c = len(m[0])
        for i in range(r // 2):
            for j in range(c):
                m[i][j], m[r - i - 1][j] = m[r - i - 1][j], m[i][j]
        for i in range(r):
            for j in range(i):
                m[i][j], m[j][i] = m[j][i], m[i][j]
