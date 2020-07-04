class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1

        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        nums = nums[j:]
        n -= j

        for i in range(n):
            k = abs(nums[i]) - 1
            if k < n and nums[k] > 0: nums[k] = -nums[k]

        for i in range(n):
            if nums[i] > 0: return i + 1

        return n + 1
