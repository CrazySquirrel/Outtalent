class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        row_idx = step = 0
        rows = [''] * numRows

        for c in s:
            rows[row_idx] += c
            if row_idx == 0:
                step = 1
            elif row_idx == numRows - 1:
                step = -1
            row_idx += step

        return ''.join(rows)
