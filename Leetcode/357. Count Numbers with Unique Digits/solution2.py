class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return sum([1, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920, 3265920][:n + 1])
