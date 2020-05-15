class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m

        for ri, ci in indices:
            rows[ri] += 1
            cols[ci] += 1

        counter = 0

        for i in range(n):
            for j in range(m):
                if (rows[i] + cols[j]) % 2 == 1:
                    counter += 1

        return counter
