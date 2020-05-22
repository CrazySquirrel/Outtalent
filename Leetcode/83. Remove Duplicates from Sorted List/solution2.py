# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        while tmp:
            while tmp.next and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head
