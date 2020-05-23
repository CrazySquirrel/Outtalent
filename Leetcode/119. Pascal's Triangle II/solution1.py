class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a, b = [], [1]

        for i in range(rowIndex + 1):
            a, b = b, [1] * (i + 1)
            for j in range(1, i): b[j] = a[j - 1] + a[j]

        return b
