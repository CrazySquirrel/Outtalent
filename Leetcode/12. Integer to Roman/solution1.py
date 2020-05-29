ROMAN = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
INTEGERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        for i, r in zip(INTEGERS, ROMAN):
            if num >= i:
                count = num // i
                num -= i * count
                result.append(r * count)
        return ''.join(result)
