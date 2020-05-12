class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        counter = 0

        for row in grid:
            l, h = 0, n - 1

            while l <= h:
                m = l + (h - l) // 2

                if row[m] < 0:
                    h = m - 1
                else:
                    l = m + 1

            if l >= n or row[l] >= 0:
                continue

            counter += n - l

        return counter
