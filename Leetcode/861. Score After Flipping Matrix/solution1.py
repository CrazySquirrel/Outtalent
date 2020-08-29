class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        def flipCol(j):
            for i in range(m): A[i][j] ^= 1

        def flipRow(i):
            for j in range(n): A[i][j] ^= 1

        def countColum(j):
            return sum([A[i][j] for i in range(m)])

        def getInt(i):
            out = 0
            for bit in A[i]: out = (out << 1) | bit
            return out

        def getScore():
            return sum([getInt(i) for i in range(m)])

        flipped = True

        while flipped:
            flipped = False

            for i in range(m):
                if A[i][0] == 0:
                    flipRow(i)
                    flipped = True

            for j in range(n):
                if countColum(j) < m / 2:
                    flipCol(j)
                    flipped = True

        return getScore()
