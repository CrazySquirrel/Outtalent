# Iterative

## Algorithm

* Check if we've head or that we need to reverse at all
* Create dummy node that points to the head
* Get linked inst length
* If length if less than k just return dummy.next
* Create head pointer to the dummy.next and tail pointer to the dummy
* Iterate for length/k:
    * Create two pointers prev and curr for None and head
    * Iterate for k:
        * Set head.next to prev, head to head.next and prev to head
    * Set tail.next to prev and tail to curr
* Set tail.next to head
* Return dummy.next

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1: return head

        dummy = ListNode(0, head)

        length = 0
        while head:
            length += 1
            head = head.next

        if length < k: return dummy.next

        head, tail = dummy.next, dummy

        for _ in range(length // k):
            prev, curr = None, head
            for _ in range(k): head.next, head, prev = prev, head.next, head
            tail.next, tail = prev, curr

        tail.next = head

        return dummy.next
```

## Complexity Analysis

* Time complexity: O(N)

* Space complexity: O(1)
