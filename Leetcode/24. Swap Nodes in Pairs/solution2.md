# Iterative

## Algorithm

* Create dummy node for result
* Set result next to head
* Save result to prev
* While prev next and prev next next exist iterate:
    * Set curr to prev next
    * Set next to curr next
    * Set curr next to next next
    * Set next next to curr
    * Set prev next to next
    * Set prev to curr
* Return result next

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode("*")
        result.next = head
        prev = result

        while prev.next and prev.next.next:
            curr = prev.next
            next = curr.next

            curr.next = next.next
            next.next = curr

            prev.next = next
            prev = curr

        return result.next
```

## Complexity Analysis

* Time complexity: O(N)

* Space complexity: O(N)

[Prev](solution1.md)