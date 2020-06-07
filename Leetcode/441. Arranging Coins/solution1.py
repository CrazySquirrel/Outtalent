class Solution:
    def arrangeCoins(self, n: int) -> int:
        row_width = 1
        result = 0
        while row_width <= n:
            n -= row_width
            result += 1
            row_width += 1
        return result
