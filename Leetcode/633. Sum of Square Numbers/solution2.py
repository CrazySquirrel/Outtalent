class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            cur = left ** 2 + right ** 2
            if cur < c:
                left += 1
            elif cur > c:
                right -= 1
            else:
                return True
        return False
