# Iterative

## Algorithm

1. If there is no l1 and l2 then just return None
2. If there only l1 or l2 then return l1 or l2 respectively
3. Create dummy list node and curr pointer to it
4. Until pointers l1 and l2 are exist check:
    1. If l1 is greater than l2 then set curr next to the list node with value l2 and move curr and l2 to the next nodes respectively
    2. If l1 is smaller than l2 then set curr next to the list node with value l1 and move curr and l1 to the next nodes respectively
5. If l1 still exist iterate through it and set curr list nodes
6. If l2 still exist iterate through it and set curr list nodes
7. Return dummy next list node

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

        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next

        while l1:
            curr.next = ListNode(l1.val)
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = ListNode(l2.val)
            curr = curr.next
            l2 = l2.next

        return dummy.next
```

## Complexity analysis

* Time complexity: O(l1+l2)

* Space complexity: O(l1+l2)

[Prev](solution1.md) [Next](solution3.md)
