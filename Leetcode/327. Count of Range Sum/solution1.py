from bisect import bisect_left, bisect_right


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0: return 0

        result = 0

        prefixsum = [0] * (len(nums) + 1)

        for a in range(len(nums)): prefixsum[a + 1] = prefixsum[a] + nums[a]

        rightlist = [prefixsum[-1]]

        for i in reversed(range(len(prefixsum) - 1)):
            loweridx = bisect_left(rightlist, lower + prefixsum[i])
            upperidx = bisect_right(rightlist, upper + prefixsum[i])

            result += (upperidx - loweridx)

            insertidx = bisect_left(rightlist, prefixsum[i])

            rightlist.insert(insertidx, prefixsum[i])

        return result
