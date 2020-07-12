class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        if not nums or nums[0] * k > target or target > nums[-1] * k: return []
        if k == 2: return self.twoSum(nums, target)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for sub_sum in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                res.append([nums[i]] + sub_sum)
        return res

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = len(nums) - 1
        lo, hi = 0, l
        while lo < hi:
            if lo > 0 and nums[lo] == nums[lo - 1]:
                lo += 1
            elif hi < l and nums[hi] == nums[hi + 1]:
                hi -= 1
            else:
                s = nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
        return res
