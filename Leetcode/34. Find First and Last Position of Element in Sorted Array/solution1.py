class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = end = i
                else:
                    end = i
        return [start, end]
