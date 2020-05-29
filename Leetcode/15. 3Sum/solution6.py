from collections import Counter
from bisect import bisect_left, bisect_right


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = sorted(counter)
        result = set()

        for i, itemI in enumerate(nums):
            if itemI == 0:
                if counter[itemI] > 2:
                    result.add((0, 0, 0))
            else:
                if counter[itemI] > 1 and -2 * itemI in counter:
                    result.add((itemI, itemI, -2 * itemI))

            if itemI < 0:
                target = -itemI
                left = bisect_left(nums, target - nums[-1], i + 1)
                right = bisect_right(nums, target // 2, left)

                for itemJ in nums[left: right]:
                    itemK = target - itemJ

                    if itemK in counter and itemK != itemJ:
                        result.add((itemI, itemJ, itemK))

        return result
