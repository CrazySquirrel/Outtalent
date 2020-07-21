# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Brute Force](solution1.md) | O(N log N) | O(N) |
| [Compare one by one](solution2.md) | O(K * N) | O(N) |
| [Compare one by one (Priority Queue)](solution3.md) | O(N log K) |  O(N) |
| [Compare one by one (Heap)](solution4.md) | O(N log K) | O(N) |
| [Merge lists one by one](solution5.md) | O(K * N) | O(1) |
| [Merge with Divide And Conquer](solution6.md) | O(N log K) | O(1) |

## Video

[![23. Merge k Sorted Lists](http://img.youtube.com/vi/SENsA3125cQ/0.jpg)](http://www.youtube.com/watch?v=SENsA3125cQ&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "23. Merge k Sorted Lists")
