# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode, k: int) -> ListNode:
        p = head

        for i in range(k):
            if p:
                p = p.next
            else:
                return head

        pre, now = head, head.next
        pre.next = None

        i = 1
        while now != None and i < k:
            nex = now.next
            now.next = pre
            pre, now = now, nex
            i += 1

        if now != None: head.next = self.reverse(now, k)

        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head
        return self.reverse(head, k)
