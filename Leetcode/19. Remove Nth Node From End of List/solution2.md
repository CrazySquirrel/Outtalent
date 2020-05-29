# One pass algorithm

## Algorithm

The above algorithm could be optimized to one pass. Instead of one pointer, we could use two pointers. The first pointer advances the list by n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by n nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. The second pointer will be pointing at the nth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.

![](2.png)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None, next=head)
        first, second = dummy, dummy
        for i in range(n + 1): first = first.next
        while first: first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next
```

## Complexity Analysis

* Time complexity: O(L).

The algorithm makes one traversal of the list of L nodes. Therefore time complexity is O(L).

* Space complexity: O(1).

We only used constant extra space.

[Prev](solution1.md)