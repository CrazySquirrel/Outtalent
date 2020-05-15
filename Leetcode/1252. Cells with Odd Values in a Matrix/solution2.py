class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m

        for ri, ci in indices:
            rows[ri] += 1
            cols[ci] += 1

        odd_rows = sum(row % 2 == 1 for row in rows)
        odd_cols = sum(col % 2 == 1 for col in cols)

        return (odd_rows * (m - odd_cols)) + (odd_cols * (n - odd_rows))
