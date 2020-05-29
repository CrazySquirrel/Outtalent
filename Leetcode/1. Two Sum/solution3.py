class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in h:
                return [i, h[complement]]

            h[nums[i]] = i

        raise ValueError('No two sum solution')
