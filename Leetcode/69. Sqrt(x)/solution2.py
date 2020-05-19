class Solution:
    def mySqrt(self, x: int) -> int:
        y = x
        while not y * y - x < 1:
            y = (y + x / y) / 2
        return int(y)
