# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

## Example:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Brute force](solution1.md) | O(n<sup>2</sup>) | O(1) |
| [Dynamic Programming](solution2.md) | O(n) | O(n) |
| [Using stacks](solution3.md) | O(n) | O(n) |
| [Using 2 pointers](solution4.md) | O(n) | O(1) |