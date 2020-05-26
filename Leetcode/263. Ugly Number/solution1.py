class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1: return False
        if num in {1, 2, 3, 5}: return True
        if num % 5 == 0: return self.isUgly(num // 5)
        if num % 3 == 0: return self.isUgly(num // 3)
        if num % 2 == 0: return self.isUgly(num // 2)
        return False
