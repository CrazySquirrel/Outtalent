# Recursive

## Algorithm

* If there is no head or no head next then just return head
* Save head next to result
* Set head next to swapPairs of head next next
* Set result next as head
* Return result

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        result = head.next
        head.next = self.swapPairs(head.next.next)
        result.next = head
        return result
```

## Complexity Analysis

* Time complexity: O(N)

* Space complexity: O(N)

[Next](solution2.md)