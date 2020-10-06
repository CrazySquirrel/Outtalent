class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        for c in s: count ^= 1 << ord(c)
        return count == 0 or (count & (count - 1)) == 0
