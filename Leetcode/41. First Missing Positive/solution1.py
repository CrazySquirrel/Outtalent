class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, i = len(nums), 0

        if n == 0: return 1

        while i < n:
            w = nums[i] - 1

            if 0 < nums[i] <= n and nums[i] != nums[w]:
                nums[i], nums[w] = nums[w], nums[i]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
