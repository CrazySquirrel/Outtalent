# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1: return head

        dummy = ListNode(0, head)

        length = 0
        while head:
            length += 1
            head = head.next

        if length < k: return dummy.next

        head, tail = dummy.next, dummy

        for _ in range(length // k):
            prev, curr = None, head
            for _ in range(k): head.next, head, prev = prev, head.next, head
            tail.next, tail = prev, curr

        tail.next = head

        return dummy.next
