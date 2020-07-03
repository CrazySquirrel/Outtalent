class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            count = sum(n <= m for n in nums)

            if count > m:
                r = m - 1
            else:
                l = m + 1

        return l
