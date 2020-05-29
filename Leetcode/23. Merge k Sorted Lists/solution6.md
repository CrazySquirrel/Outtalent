# Merge with Divide And Conquer

## Algorithm

This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

* Pair up k lists and merge each pair.
* After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
* Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log<sub>2</sub>k times.

![](13.png)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        while len(lists) > 1: lists.append(self.mergeTwoLists(lists.pop(0), lists.pop(0)))
        return lists[0]
```

## Complexity Analysis

* Time complexity: O(N log k) where k is the number of linked lists.

    * We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    * Sum up the merge process and we can get: ![](14.png)

* Space complexity: O(1)

    * We can merge two sorted linked lists in O(1) space.

[Prev](solution5.md)