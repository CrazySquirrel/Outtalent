# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

* '.' Matches any single character.
* '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

## Note:

* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like . or *.

## Example 1:

```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

## Example 2:

```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

## Example 3:

```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

## Example 4:

```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
```

## Example 5:

```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Recursion](solution1.md) | ![](1.png) | ![](1.png) |
| [Dynamic Programming Top-Down](solution2.md) | O(TP) | O(TP) |
| [Dynamic Programming Bottom-Up](solution3.md) | O(TP) | O(TP) |

## Video

[![10. Regular Expression Matching](http://img.youtube.com/vi/G35YHrYxw1o/0.jpg)](http://www.youtube.com/watch?v=G35YHrYxw1o&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "10. Regular Expression Matching")
