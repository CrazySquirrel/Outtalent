class Solution:
    def countNegativesInLine(self, row: List[int]) -> int:
        n = len(row)
        l, h = 0, n - 1

        while l <= h:
            m = l + (h - l) // 2

            if row[m] < 0:
                h = m - 1
            else:
                l = m + 1

        return 0 if l >= n or row[l] >= 0 else n - l

    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(self.countNegativesInLine(row) for row in grid)
