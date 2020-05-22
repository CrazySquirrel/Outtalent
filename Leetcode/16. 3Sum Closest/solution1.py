class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)
        length = len(nums)
        result = diff = inf
        nums.sort()
        for i in range(0, length - 2):
            j = i + 1
            k = length - 1
            while j < k:
                sum0 = nums[i] + nums[j] + nums[k]
                if diff > abs(sum0 - target):
                    diff, result = abs(sum0 - target), sum0
                if sum0 == target:
                    return result
                elif sum0 < target:
                    j += 1
                elif sum0 > target:
                    k -= 1
        return result
