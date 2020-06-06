# Recursive with short cut 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if not l1 and not l2:
            if carry:
                return ListNode(carry)
            else:
                return None

        if l1 and not l2:
            if carry:
                carry += l1.val
                return ListNode(carry % 10, next=self.helper(l1.next, None, carry // 10))
            else:
                return l1

        if not l1 and l2:
            if carry:
                carry += l2.val
                return ListNode(carry % 10, next=self.helper(None, l2.next, carry // 10))
            else:
                return l2

        carry += l1.val + l2.val
        return ListNode(carry % 10, next=self.helper(l1.next, l2.next, carry // 10))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, 0)
```

[Prev](solution3.md) [Next](solution5.md)
