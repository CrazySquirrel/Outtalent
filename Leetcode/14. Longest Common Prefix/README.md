# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Example 1:

```
Input: ["flower","flow","flight"]
Output: "fl"
```

## Example 2:

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Note:

* All given inputs are in lowercase letters a-z.

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Horizontal scanning](solution1.md) | O(S) | O(1) |
| [Vertical scanning](solution2.md) | O(S) | O(1) |
| [Divide and conquer](solution3.md) | O(S) | O(m⋅logn) |
| [Binary search](solution4.md) | O(S⋅logm) | O(1) |
| [Min max compare](solution5.md) | O(N + S) | O(S) |
| [Further Thoughts / Follow up](solution6.md) | O(S) + O(m) | O(S) |
