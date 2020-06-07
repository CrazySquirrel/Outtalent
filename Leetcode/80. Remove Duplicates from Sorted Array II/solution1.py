class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return len(nums)

        slow = 2

        for fast in range(2, len(nums)):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

        del nums[slow:]

        return slow
