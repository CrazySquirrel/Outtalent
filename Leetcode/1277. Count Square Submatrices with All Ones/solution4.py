class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if m[i][j] != 0: m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1
        return sum([sum(k) for k in m])
