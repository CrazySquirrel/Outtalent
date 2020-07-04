class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1

        n, i = len(nums), 0

        while i < n:
            k = nums[i] - 1

            if 0 <= k < n and nums[i] != nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
