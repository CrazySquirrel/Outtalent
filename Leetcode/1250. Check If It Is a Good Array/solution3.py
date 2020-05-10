from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums[0]
        for y in nums[1:]:
            x = gcd(x, y)
            if x == 1:
                return True
        return False
