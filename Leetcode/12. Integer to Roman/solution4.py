class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = []
        for i,r in zip(integers, roman):
            if num >= i:
                count = num // i
                num -= i * count
                result.append(r * count)
        return ''.join(result)
