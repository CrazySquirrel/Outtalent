# Iterative (Optimized)

1. Create dummy list node and curr pointer to it
2. Until pointers l1 and l2 are exist check:
    1. If l1 is greater than l2 then set curr next to l2 and move curr and l2 to the next nodes respectively
    2. If l1 is smaller than l2 then set curr next to l1 and move curr and l1 to the next nodes respectively
3. If l1 still exist set curr next to l1 otherwise set curr next to l2
4. Return dummy next list node

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr, l1 = curr.next, l1.next
            else:
                curr.next = l2
                curr, l2 = curr.next, l2.next
        curr.next = l1 if l1 else l2
        return dummy.next
```

## Complexity analysis

* Time complexity: O(l1+l2)

* Space complexity: O(1)

[Prev](solution2.md) 