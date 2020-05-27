class Solution:
    def bisect(self, nums: List[int], target: int, left: bool) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > target or (left and nums[m] == target):
                r = m - 1
            else:
                l = m + 1

        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.bisect(nums, target, True)

        if start == len(nums) or nums[start] != target: return [-1, -1]

        end = self.bisect(nums, target, False) - 1

        return [start, end]
