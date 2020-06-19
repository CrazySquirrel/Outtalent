class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        return sum(cell * 4 + 2 for row in grid for cell in row if cell) - sum(min(a, b) * 2 for row in grid + list(zip(*grid)) for a, b in zip(row, row[1:]))