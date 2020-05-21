class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[0:len(nums)] = sorted(list(set(nums)))
        return len(nums)
