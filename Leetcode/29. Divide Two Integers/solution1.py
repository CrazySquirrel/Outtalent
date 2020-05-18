INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            dividend -= divisor
            result += 1

        result = -result if sign < 0 else result

        return min(INT_MAX, max(INT_MIN, result))
