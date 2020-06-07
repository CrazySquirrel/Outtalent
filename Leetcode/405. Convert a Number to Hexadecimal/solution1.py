class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        if num < 0: num += 2 ** 32
        h = '0123456789abcdef'
        result = ''
        while num:
            result = h[num & 15] + result
            num >>= 4
        return result
