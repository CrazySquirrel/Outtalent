class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in h and h[complement] != i:
                return [i, h[complement]]

        raise ValueError('No two sum solution')
