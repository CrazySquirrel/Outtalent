class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        result = [0] * l
        result[0] = 1

        for i in range(1, l): result[i] = nums[i - 1] * result[i - 1]

        R = 1

        for i in range(l - 1, -1, -1):
            result[i] *= R
            R *= nums[i]

        return result
