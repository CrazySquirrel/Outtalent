class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        ones = 0

        while num:
            if num & 1: ones += 1
            i += 1
            num >>= 1

        return i + ones - 1
