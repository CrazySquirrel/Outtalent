class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)

        return z == 0 or (x + y >= z and z % gcd(x, y) == 0)
