class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high, ans = max(nums), sum(nums), -1

        while low <= high:
            mid = (low + high) >> 1

            if self.is_valid(nums, m, mid):
                ans, high = mid, mid - 1
            else:
                low = mid + 1

        return ans

    def is_valid(self, nums, m, mid):
        cuts, curr_sum = 0, 0

        for x in nums:
            curr_sum += x

            if curr_sum > mid:
                cuts, curr_sum = cuts + 1, x
        subs = cuts + 1

        return subs <= m
