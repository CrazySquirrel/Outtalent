# [18. 4Sum](https://leetcode.com/problems/4sum/)

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

## Note:

The solution set must not contain duplicate quadruplets.

## Example:

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Two sum](solution1.md) | O(n<sup>3</sup>) | O(n<sup>2</sup>) |
| [Four pointers (Optimized)](solution2.md) | O(n<sup>3</sup>)<sup>*</sup> | O(1) |
| [Two Pointers](solution3.md) | O(n<sup>k−1</sup>) -> O(n<sup>3</sup>) | O(n) |
| [Two Pointers (Hash Set)](solution4.md) | O(n<sup>k−1</sup>) -> O(n<sup>3</sup>) | O(n) |

## Video

[![18. 4Sum](http://img.youtube.com/vi/isIRZcIvnKk/0.jpg)](http://www.youtube.com/watch?v=isIRZcIvnKk&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "18. 4Sum")
