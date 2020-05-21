class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        y, z = 0, x
        while z:
            y = y * 10 + z % 10
            z = z // 10
        return x == y
