class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)
        nums.sort()
        length = len(nums)
        result = inf

        for i, num in enumerate(nums[0:-2]):
            r = length - 1
            rs = num + nums[r] + nums[r - 1]

            if rs < target:
                result = min(result, rs, key=lambda x: abs(x - target))
                continue

            l = i + 1
            ls = num + nums[l] + nums[l + 1]

            if ls > target:
                result = min(result, ls, key=lambda x: abs(x - target))
                continue

            while l < r:
                s = num + nums[l] + nums[r]

                result = min(result, s, key=lambda x: abs(x - target))

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target

        return result
