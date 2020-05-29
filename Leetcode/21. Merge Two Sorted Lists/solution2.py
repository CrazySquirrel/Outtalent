# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1

        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next

        while l1:
            curr.next = ListNode(l1.val)
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = ListNode(l2.val)
            curr = curr.next
            l2 = l2.next

        return dummy.next
