class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = '-' if num < 0 else ''
        num = abs(num)
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7
        return sign + ''.join(result[::-1]) if result else '0'
