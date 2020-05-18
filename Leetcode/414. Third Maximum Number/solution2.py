class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        nums.sort(reverse=True)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: count += 1
            if count == 3: return nums[i]
        return max(nums)
