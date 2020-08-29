# Subtraction

## Algorithm

* Keep subtracting the divisor from dividend until dividend becomes less than divisor. The dividend becomes the remainder, and the number of times subtraction is done becomes the quotient.

```python
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
```

## Complexity Analysis:

* Time complexity: O(a/b)

* Space Complexity: O(1)

[Next](solution2.md)
