class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(3, len(x)):
            if x[i - 3] >= x[i - 1] and x[i] >= x[i - 2]:
                return True
            if i >= 4 and x[i - 3] == x[i - 1] and x[i - 4] + x[i] >= x[i - 2]:
                return True
            if i >= 5 and x[i - 2] >= x[i - 4] and x[i - 1] <= x[i - 3] <= x[i - 5] + x[i - 1] and x[i - 4] + x[i] >= x[i - 2]:
                return True
        return False