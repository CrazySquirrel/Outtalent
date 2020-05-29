# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string, find the length of the longest substring without repeating characters.

## Example 1:

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

## Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

## Example 3:

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Brute Force](solution1.md) | O(n<sup>3</sup>) | O(min(n,m)) |
| [Sliding Window](solution2.md) | O(n) | O(min(n,m)) |
| [Sliding Window Optimized (HashMap)](solution3.md) | O(n) | O(min(n,m)) |
| [Sliding Window Optimized (ASCII 128)](solution4.md) | O(n) | O(m) |
| [Sliding Window Optimized](solution5.md) | O(n) | O(min(n,m)) |