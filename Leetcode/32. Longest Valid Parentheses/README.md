# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

## Example 1:

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

## Example 2:

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Brute Force](solution1.md) | O(n<sup>3</sup>) | O(n) |
| [Dynamic Programming](solution2.md) | O(n) | O(n) |
| [Using Stack](solution3.md) | O(n) | O(n) |
| [Without extra space](solution4.md) | O(n) | O(1) |