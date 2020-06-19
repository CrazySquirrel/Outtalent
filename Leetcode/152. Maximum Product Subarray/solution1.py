class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        f = g = result = nums[0]
        for n in nums[1:]:
            if n < 0: f, g = g, f
            f, g = max(f * n, n), min(g * n, n)
            result = max(result, f)
        return result
