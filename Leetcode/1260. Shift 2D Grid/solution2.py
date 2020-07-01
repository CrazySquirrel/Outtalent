class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col = len(grid[0])

        nums = sum(grid, [])
        nums_len = len(nums)
        move = nums_len - (k % nums_len)
        nums = nums[move:] + nums[:move]

        count = 0

        for i in range(0, nums_len, col):
            grid[count] = nums[i:i + col]
            count += 1

        return grid
