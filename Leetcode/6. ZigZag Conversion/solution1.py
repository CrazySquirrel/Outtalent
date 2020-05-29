class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = [''] * min(numRows, len(s))
        cur_row = 0
        goind_down = False

        for c in s:
            rows[cur_row] += c

            if cur_row == 0 or cur_row == numRows - 1:
                goind_down = not goind_down

            cur_row += 1 if goind_down else -1

        result = ''

        for row in rows:
            result += row

        return result
