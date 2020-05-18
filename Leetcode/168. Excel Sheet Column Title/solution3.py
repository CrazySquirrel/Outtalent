class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n:
            res.append(chr((n - 1) % 26 + 65))
            n = (n - 1) // 26
        return ''.join(res[::-1])
