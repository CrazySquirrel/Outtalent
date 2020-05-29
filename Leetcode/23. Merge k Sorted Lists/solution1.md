# Brute Force

## Algorithm

* Traverse all the linked lists and collect the values of the nodes into an array.
* Sort and iterate over this array to get the proper value of nodes.
* Create a new sorted linked list and extend it with the new nodes.

As for sorting, you can refer [here](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html) for more about sorting algorithms.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []

        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next

        dummy = curr = ListNode(0)

        for num in sorted(nums):
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
```

## Complexity Analysis

* Time complexity: O(NlogN) where N is the total number of nodes.

    * Collecting all the values costs O(N) time.
    * A stable sorting algorithm costs O(NlogN) time.
    * Iterating for creating the linked list costs O(N) time.

* Space complexity: O(N).

    * Sorting cost O(N) space (depends on the algorithm you choose).
    * Creating a new linked list costs O(N) space.
    
[Next](solution2.md)