# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.next.val == head.val:
                    head.next = head.next.next
                prev.next, head = head.next, head.next
            else:
                prev, head = head, head.next
        return dummy.next
