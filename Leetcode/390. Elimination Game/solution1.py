class Solution:
    def lastRemaining(self, n: int) -> int:
        result = range(1, n + 1)
        while len(result) > 1:
            result = result[1::2]
            if len(result) == 1: return result[0]
            result = result[::-1][1::2][::-1]
        return result[0]
