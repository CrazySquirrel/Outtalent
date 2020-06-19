class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        n = len(nums)
        kmax = max(nums[:k])
        res = [kmax]
        for i in range(k, n):
            if kmax <= nums[i]:
                kmax = nums[i]
            elif nums[i - k] == kmax:
                kmax = max(nums[i - k + 1:i + 1])
            res.append(kmax)
        return res
