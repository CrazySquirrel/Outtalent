class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1: return False
        h = {}
        for i, v in enumerate(nums):
            if v not in h:
                h[v] = i
            else:
                if i - h[v] <= k: return True
                h[v] = i
        return False
