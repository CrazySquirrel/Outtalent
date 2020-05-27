class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not m: return None
        n = len(m)
        for i in range(n):
            for j in range(i + 1, n): m[j][i], m[i][j] = m[i][j], m[j][i]
        for i in range(n): m[i].reverse()
