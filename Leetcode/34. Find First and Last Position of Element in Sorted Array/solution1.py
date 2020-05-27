from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)

        if start == len(nums) or nums[start] != target: return [-1, -1]

        end = bisect_right(nums, target) - 1

        return [start, end]
