class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if counter == 0: return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                counter -= 1
        return True
