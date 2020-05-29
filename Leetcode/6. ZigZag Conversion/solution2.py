class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        result = ''
        n = len(s)
        cycle_len = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, n - i, cycle_len):
                result += s[j + i]

                if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                    result += s[j + cycle_len - i]

        return result
