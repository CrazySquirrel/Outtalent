# [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Example 1:

```
Input: haystack = "hello", needle = "ll"
Output: 2
```

## Example 2:

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

## Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Check by symbol](solution1.md) | O(m * n) | O(1) |
| [Slices](solution2.md) | O(m * n) | O(1) |
| [Rolling Hash](solution3.md) | O(m + n) | O(1) |
| [KMP](solution4.md) | O(n<sup>2</sup>) -> O(m + n) | O(n) |
| [Boyer–Moore](solution5.md) | O(n * m) -> O(m/n) | O(m) |