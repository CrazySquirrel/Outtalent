from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce((lambda x, y: gcd(x, y)), nums) == 1
