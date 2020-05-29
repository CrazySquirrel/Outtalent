V1 = ["", "M", "MM", "MMM"]
V2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
V3 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
V4 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


class Solution:
    def intToRoman(self, num: int) -> str:
        return V1[num // 1000] + V2[(num % 1000) // 100] + V3[(num % 100) // 10] + V4[num % 10];
