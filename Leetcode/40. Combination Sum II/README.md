# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

##  Note:

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

## Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

## Example 2:

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [DFS](solution1.md) | O(k * n<sup>2</sup>) | O(k * n) |