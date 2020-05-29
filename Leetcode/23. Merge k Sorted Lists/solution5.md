# Merge lists one by one

## Algorithm

Convert merge k lists problem to merge 2 lists (k-1) times. Here is the [merge 2 lists](../21.%20Merge%20Two%20Sorted%20Lists) problem page.

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
        result = lists[0]
        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        return result
```

## Complexity Analysis

* Time complexity: O(kN) where k is the number of linked lists.

    * We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    * Sum up the merge process and we can get: ![](12.png)

* Space complexity: O(1)

    * We can merge two sorted linked list in O(1) space.
    
[Prev](solution4.md) [Next](solution6.md)