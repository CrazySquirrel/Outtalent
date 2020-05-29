# Recursive

## Algorithm

1. If there is no l1 and l2 then just return None
2. If there only l1 or l2 then return l1 or l2 respectively
3. Compare value of l1 and l2:
    1. If l1 less than l2 then l1.next = mergeTwoLists(l1.next, l2)
    2. If l2 less than l1 then l2.next = mergeTwoLists(l1, l2.next)

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
```

## Complexity analysis

* Time complexity: O(l1+l2)

* Space complexity: O(l1+l2)

[Next](solution2.md)