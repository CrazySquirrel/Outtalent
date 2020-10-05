class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if x == sum([n >= x for n in nums]): return x
        return -1
