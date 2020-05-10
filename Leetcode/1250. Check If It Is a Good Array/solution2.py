from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums[0]
        for y in nums: x = gcd(x, y)
        return x == 1
