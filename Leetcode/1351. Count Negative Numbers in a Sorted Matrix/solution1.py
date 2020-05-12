class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0

        l = len(grid[0]) - 1
        j = l

        for i in range(len(grid)):
            while grid[i][j] < 0 <= j: j -= 1
            counter += l - j

        return counter
