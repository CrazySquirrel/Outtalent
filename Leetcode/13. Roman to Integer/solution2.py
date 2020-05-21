class Solution:
    def romanToInt(self, s: str) -> int:
        lastnum = result = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for roman in s[::-1]:
            if dic[roman] >= lastnum:
                result += dic[roman]
            else:
                result -= dic[roman]
            lastnum = dic[roman]
        return result
