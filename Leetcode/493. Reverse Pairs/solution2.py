class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(start: int, end: int) -> int:
            mid = (start + end) >> 1

            if start == mid: return 0

            count = helper(start, mid) + helper(mid, end)

            i = mid

            for left in nums[start:mid]:
                while i < end and 2 * nums[i] < left: i += 1
                count += i - mid

            nums[start:end] = sorted(nums[start:end])

            return count

        return helper(0, n)
