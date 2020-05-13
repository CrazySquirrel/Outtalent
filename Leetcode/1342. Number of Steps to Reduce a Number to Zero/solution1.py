class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            steps += 1
        return steps
