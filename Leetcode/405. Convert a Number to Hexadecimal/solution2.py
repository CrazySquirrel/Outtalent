class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        h = '0123456789abcdef'
        result = ''
        for i in range(8):
            result = h[num % 16] + result
            num = num >> 4
        return result.lstrip('0')
