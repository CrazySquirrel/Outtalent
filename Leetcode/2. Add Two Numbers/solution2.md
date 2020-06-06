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
        carry = 0
        while l1 or l2:
            if l1: carry, l1 = carry + l1.val, l1.next
            if l2: carry, l2 = carry + l2.val, l2.next
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10
        if carry: head.next = ListNode(carry)
        return result.next
```

[Prev](solution1.md) [Next](solution3.md)