class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = num
        while result * result > num:
            result = (result + num // result) // 2
        return result * result == num
