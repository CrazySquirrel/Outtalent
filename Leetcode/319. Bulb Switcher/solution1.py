class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = [0] * n
        for i in range(1, n + 1):
            for j in range(i - 1, n, i):
                bulbs[j] = 0 if bulbs[j] else 1
        return sum(bulbs)
