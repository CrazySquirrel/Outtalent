# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a 32-bit signed integer, reverse digits of an integer.

## Example 1:

```
Input: 123
Output: 321
```

## Example 2:

```
Input: -123
Output: -321
```

## Example 3:

```
Input: 120
Output: 21
```

## Note:

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Pop and Push Digits & Check before Overflow](solution1.md) | O(log(x)) | O(1) |
| [Pop and Push Digits & Simplified Check before Overflow](solution2.md) | O(log(x)) | O(1) |

## Video

[![7. Reverse Integer](http://img.youtube.com/vi/Y2f3zWqcT2Q/0.jpg)](http://www.youtube.com/watch?v=Y2f3zWqcT2Q&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "7. Reverse Integer")