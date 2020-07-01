class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(0, n + 1):
            if str(i).count('0') == str(n - i).count('0') == 0:
                return [i, n - i]
