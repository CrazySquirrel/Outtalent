# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

## Example 1:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

## Example 2:

```
Input: "cbbd"
Output: "bb"
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Simple Recursion](solution1.md) | O(2<sup>n</sup>) | O(n) |
| [Dynamic programming](solution2.md) | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| [Manacher’s Algorithm](solution3.md) | O(n) | O(1) |

## Video

[![5. Longest Palindromic Substring](http://img.youtube.com/vi/kvNjXiqydY0/0.jpg)](http://www.youtube.com/watch?v=kvNjXiqydY0&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "5. Longest Palindromic Substring")