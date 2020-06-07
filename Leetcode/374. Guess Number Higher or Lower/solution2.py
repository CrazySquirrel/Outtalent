# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            m1 = l + (h - l) // 3
            m2 = h - (h - l) // 3
            if guess(m1) == 0: return m1
            if guess(m2) == 0: return m2
            if guess(m1) < 0:
                h = m1 - 1
            elif guess(m2) > 0:
                l = m2 + 1
            else:
                l = m1 + 1
                h = m2 - 1
        return -1
