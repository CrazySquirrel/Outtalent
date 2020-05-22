from bisect import bisect_left


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                x = 0 - nums[i] - nums[j]
                k = bisect_left(nums, x, lo=j + 1)
                if k != len(nums) and nums[k] == x:
                    result.add((nums[i], nums[j], nums[k]))

        return result
