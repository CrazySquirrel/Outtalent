# Bit manipulation

## Algorithm

Use bit manipulation in order to find the quotient. The divisor and dividend can be written as

```dividend = quotient * divisor + remainder```

As every number can be represented in base 2(0 or 1), represent the quotient in binary form by using shift operator as given below :

* Determine the most significant bit in the quotient. This can easily be calculated by iterating on the bit position i from 31 to 1.
* Find the first bit for which divisor << i is less than dividend and keep updating the ith bit position for which it is true.
* Add the result in temp variable for checking the next position such that (temp + (divisor << i) ) is less than dividend.
* Return the final answer of quotient after updating with corresponding sign.

```python
INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        temp = 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                result |= 1 << i

        result = -result if sign < 0 else result

        return min(INT_MAX, max(INT_MIN, result))
```

## Complexity Analysis:

* Time complexity: O(log(a))

* Space Complexity: O(1)

[Prev](solution1.md)
