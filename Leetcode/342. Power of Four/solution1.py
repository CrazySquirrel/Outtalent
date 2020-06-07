class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num >= 4:
            if num % 4: break
            num //= 4
        return num == 1
