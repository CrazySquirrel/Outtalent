import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_indexes = []

        for list_index in range(len(lists)):
            if lists[list_index]:
                heapq.heappush(list_indexes, (lists[list_index].val, list_index))

        dummy = curr = ListNode(0)

        while list_indexes:
            val, list_index = heapq.heappop(list_indexes)

            curr.next = ListNode(val)
            curr = curr.next

            lists[list_index] = lists[list_index].next

            if lists[list_index]:
                heapq.heappush(list_indexes, (lists[list_index].val, list_index))

        return dummy.next
