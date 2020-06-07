class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        i = 0
        counter = 0
        while num:
            if num & 1:
                if i % 2 == 1: return False
                counter += 1
                if counter == 2: return False
            i += 1
            num >>= 1
        return counter == 1
