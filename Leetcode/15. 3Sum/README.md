# [15. 3Sum](https://leetcode.com/problems/3sum/)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

## Note:

The solution set must not contain duplicate triplets.

## Example:

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Brute Force](solution1.md) | O(n<sup>3</sup>) | O(r) |
| [Binary search](solution2.md) | O(n<sup>2</sup>*log(n)) | O(r) |
| [Two sum](solution3.md) | O(n<sup>2</sup> + n * m) | O(n<sup>2</sup>) |
| [Two pointers](solution4.md) | O(n<sup>2</sup>) | O(r) |
| [Split negative and positive](solution5.md) | O(n + m<sup>2</sup>) | O(n + r) |
| [Binary search in range](solution6.md) | O(n + m) | O(n + r) |
