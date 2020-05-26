class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1: return False
        while num % 5 == 0: num //= 5
        while num % 3 == 0: num //= 3
        while num % 2 == 0: num //= 2
        return num in {1, 2, 3, 5}
