class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, green, blue = 0, 0, len(nums) - 1

        while green <= blue:
            if nums[green] == 0:
                nums[red], nums[green] = nums[green], nums[red]
                green += 1
                red += 1
            elif nums[green] == 1:
                green += 1
            else:
                nums[green], nums[blue] = nums[blue], nums[green]
                blue -= 1
