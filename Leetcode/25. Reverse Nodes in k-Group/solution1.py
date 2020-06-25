# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head

        test = head

        for i in range(k):
            if test is None: return head
            test = test.next

        prev = None
        curr = head

        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        if curr: head.next = self.reverseKGroup(curr, k)

        return prev
