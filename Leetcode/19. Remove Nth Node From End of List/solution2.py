# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None, next=head)
        first, second = dummy, dummy
        for i in range(n + 1): first = first.next
        while first: first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next
