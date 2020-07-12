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
        s = set()
        for i in range(len(nums)):
            if (not res or res[-1][1] != nums[i]) and target - nums[i] in s:
                res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
