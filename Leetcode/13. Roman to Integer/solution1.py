ROMAN_TO_INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        last = curr = result = 0
        for c in s[::-1]:
            last, curr = curr, ROMAN_TO_INT[c]
            result += curr if curr >= last else -curr
        return result
