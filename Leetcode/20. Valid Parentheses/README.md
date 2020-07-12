# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

## Example 1:

```
Input: "()"
Output: true
```

## Example 2:

```
Input: "()[]{}"
Output: true
```

## Example 3:

```
Input: "(]"
Output: false
```

## Example 4:

```
Input: "([)]"
Output: false
```

## Example 5:

```
Input: "{[]}"
Output: true
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Stacks](solution1.md) | O(n) | O(n) |

## Video

[![20. Valid Parentheses](http://img.youtube.com/vi/8AQs-KY1mCk/0.jpg)](http://www.youtube.com/watch?v=8AQs-KY1mCk&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "20. Valid Parentheses")
