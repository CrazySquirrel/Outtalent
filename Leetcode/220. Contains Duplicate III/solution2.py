class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1 or k == 0 or t < 0: return False
        bucket = {}
        for i in range(0, n):
            b = nums[i] // (t + 1)
            if b in bucket: return True
            if (b - 1) in bucket and abs(nums[i] - bucket[b - 1]) <= t: return True
            if (b + 1) in bucket and abs(nums[i] - bucket[b + 1]) <= t: return True
            bucket[b] = nums[i]
            if i >= k: bucket.pop(nums[i - k] // (t + 1))
        return False
