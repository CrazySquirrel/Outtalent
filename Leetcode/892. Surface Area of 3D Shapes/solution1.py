class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        top = 0
        for row in grid:
            for num in row:
                if num > 0: top += 1

        left = 0
        for row in grid:
            std = 0
            for num in row:
                if num - std > 0: left += num - std
                std = num

        front = 0
        for i in range(len(grid[0])):
            std = 0
            for row in grid:
                if row[i] - std > 0: front += row[i] - std
                std = row[i]

        return 2 * (top + left + front)
