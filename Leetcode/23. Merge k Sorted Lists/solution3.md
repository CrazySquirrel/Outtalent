# Compare one by one (Priority Queue)

## Algorithm

Almost the same as the one above but optimize the comparison process by priority queue. 
You can refer [here](https://en.wikipedia.org/wiki/Priority_queue) for more information about it.

```python
from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_indexes = PriorityQueue()

        for list_index in range(len(lists)):
            if lists[list_index]:
                list_indexes.put((lists[list_index].val, list_index))

        dummy = curr = ListNode(0)

        while not list_indexes.empty():
            val, list_index = list_indexes.get()

            curr.next = ListNode(val)
            curr = curr.next

            lists[list_index] = lists[list_index].next

            if lists[list_index]:
                list_indexes.put((lists[list_index].val, list_index))

        return dummy.next
```

## Complexity Analysis

* Time complexity: O(N log k) where k is the number of linked lists.

    * The comparison cost will be reduced to O(log k) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
    * There are N nodes in the final linked list.

* Space complexity:

    * O(n) Creating a new linked list costs O(n) space.
    * O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).
    
[Prev](solution2.md) [Next](solution4.md)