class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) // 26
        return res
