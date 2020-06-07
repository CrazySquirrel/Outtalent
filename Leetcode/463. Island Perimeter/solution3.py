class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                result += 4
                if i and grid[i - 1][j]: result -= 2
                if j and grid[i][j - 1]: result -= 2
        return result
