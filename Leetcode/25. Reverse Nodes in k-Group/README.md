# [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

## Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

## Note:

* Only constant extra memory is allowed.
* You may not alter the values in the list's nodes, only nodes itself may be changed.

## Solutions

|   Approach  | Time complexity | Space complexity |
|-------------|-----------------|------------------|
| [Recursive](solution1.md) | O(N) | O(N/k) |
| [Iterative](solution2.md) | O(N) | O(1) |

## Video

[![25. Reverse Nodes in k-Group](http://img.youtube.com/vi/5uSAYYiapoI/0.jpg)](http://www.youtube.com/watch?v=5uSAYYiapoI&list=PL9YvZlrMIj4msDfX2rTsl4hwETiKiwsy3 "25. Reverse Nodes in k-Group")
