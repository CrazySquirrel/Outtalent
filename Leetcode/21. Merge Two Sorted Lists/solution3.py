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
