class Solution:
    def gcd(self, x: int, y: int) -> int:
        while (y): x, y = y, x % y
        return x

    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums[0]
        for y in nums: x = self.gcd(x, y)
        return x == 1
