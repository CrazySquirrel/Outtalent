class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1: return False
        s = set()
        for i in range(min(k, len(nums))):
            if nums[i] in s: return True
            s.add(nums[i])
        for i in range(k, len(nums)):
            if nums[i] in s: return True
            s.remove(nums[i - k])
            s.add(nums[i])
        return False
