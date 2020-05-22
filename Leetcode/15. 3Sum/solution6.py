from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ref = Counter(nums)
        nums = sorted(ref)
        result = []

        for i, itemI in enumerate(nums):
            if itemI == 0:
                if ref[itemI] > 2:
                    result.append((0, 0, 0))
            else:
                if ref[itemI] > 1 and -2 * itemI in ref:
                    result.append((itemI, itemI, -2 * itemI))

            if itemI < 0:
                target = -itemI
                left = bisect_left(nums, target - nums[-1], i + 1)
                right = bisect_right(nums, target // 2, left)

                for itemJ in nums[left: right]:
                    itemK = target - itemJ
                    if itemK in ref and itemK != itemJ:
                        result.append((itemI, itemJ, itemK))

        return result
