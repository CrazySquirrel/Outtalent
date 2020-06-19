class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        yz = sum(max(row) for row in grid)
        xz = sum(max(col) for col in zip(*grid))
        xy = sum(cell > 0 for row in grid for cell in row)

        return xy + yz + xz
