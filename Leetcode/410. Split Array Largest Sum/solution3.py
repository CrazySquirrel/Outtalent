class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def is_valid(mid: int) -> bool:
            cuts = curr_sum = 0

            for x in nums:
                curr_sum += x

                if curr_sum > mid:
                    cuts, curr_sum = cuts + 1, x
                    if cuts >= m: return False

            return cuts + 1 <= m

        low, high, ans = max(nums), sum(nums), -1

        while low <= high:
            mid = low + ((high - low) >> 1)

            if is_valid(mid):
                ans, high = mid, mid - 1
            else:
                low = mid + 1

        return ans
