class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0: return False
        if c == 0: return True
        for i in range(1, int(c ** 0.5 + 1)):
            j = (c - i * i) ** 0.5
            if int(j) == j:
                return True
        return False
