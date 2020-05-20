class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        for i in range(l - 1):
            for j in range(i + 1, min(i + k + 1, l)):
                if nums[i] == nums[j]:
                    return True
        return False
