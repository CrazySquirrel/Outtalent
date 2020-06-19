class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == nums[r]:
                r -= 1
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]
