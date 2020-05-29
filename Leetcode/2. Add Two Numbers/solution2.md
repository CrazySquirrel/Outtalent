# Elementary Math (Optimized)

We going to use the same solution as for [Elementary Math](solution1.md) by with some coding optimizations.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head = ListNode()
        v = 0
        while l1 or l2:
            if l1: v, l1 = v + l1.val, l1.next
            if l2: v, l2 = v + l2.val, l2.next
            head.next = ListNode(v % 10)
            head = head.next
            v //= 10
        if v: head.next = ListNode(v)
        return result.next
```

[Prev](solution1.md)