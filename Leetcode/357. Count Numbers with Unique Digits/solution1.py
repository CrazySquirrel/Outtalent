class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        nums = [9]
        for x in range(9, 0, -1): nums.append(nums[-1] * x)
        return sum(nums[:n]) + 1
