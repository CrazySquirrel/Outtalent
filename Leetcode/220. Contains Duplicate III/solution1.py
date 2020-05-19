class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, min(i + k + 1, l)):
                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False
