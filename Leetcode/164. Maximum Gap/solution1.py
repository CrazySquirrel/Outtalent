from math import fabs, ceil


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        if len(nums) == 2: return int(fabs(nums[0] - nums[1]))

        Min, Max = min(nums), max(nums)

        average_gap = int(ceil((Max - Min) / (len(nums) - 2)))

        buckets = [[] for i in range(len(nums) - 2)]

        for num in nums:
            if num == Min or num == Max:
                continue
            else:
                buckets[(num - Min) // average_gap].append(num)

        pre, ret = Min, -inf

        for bucket in buckets:
            if bucket:
                ret = max(min(bucket) - pre, ret)
                pre = max(bucket)

        return max(ret, Max - pre)
