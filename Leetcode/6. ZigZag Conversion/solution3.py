class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        rows = [''] * numRows
        row_idx = 0
        direction = -1
        numRows -= 1

        for i, c in enumerate(s):
            rows[row_idx] += c
            if i % numRows == 0: direction *= -1
            row_idx += direction

        return ''.join(rows)
