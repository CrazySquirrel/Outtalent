# 29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

## Example 1:

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
```

## Example 2:

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
```

## Note:

* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Subtraction](solution1.md) | O(a/b) | O(1) |
| [Bit manipulation](solution2.md) | O(log(a)) | O(n) |

## Video

[![29. Divide Two Integers](http://img.youtube.com/vi/43wgcyntnLQ/0.jpg)](http://www.youtube.com/watch?v=43wgcyntnLQ&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "29. Divide Two Integers")
