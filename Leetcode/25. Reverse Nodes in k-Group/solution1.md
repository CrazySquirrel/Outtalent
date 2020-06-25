# Group reversion

## Algorithm

* If there is no head or k equal to zero then just return head
* Check then list longer then k and just return head if not
* Set prev to None and curr to head
* Iterate from 0 to k:
    * Set tmp to curr next
    * Set curr next to prev
    * Set prev to curr
    * Set curr to tmp
* If there is curr then set head next to reverseKGroup(curr, k)
* Return prev

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head

        test = head

        for i in range(k):
            if test is None: return head
            test = test.next

        prev = None
        curr = head

        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        if curr: head.next = self.reverseKGroup(curr, k)

        return prev
```

## Complexity Analysis

* Time complexity: O(N)

* Space complexity: O(1)
