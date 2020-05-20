# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        if head.val == val: return self.removeElements(head.next, val)
        head.next = self.removeElements(head.next, val)
        return head
