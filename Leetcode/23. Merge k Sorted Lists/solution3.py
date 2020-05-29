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
