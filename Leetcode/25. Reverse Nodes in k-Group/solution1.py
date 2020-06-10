# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isLongerThenK(self, head: ListNode, k: int) -> bool:
        for i in range(k):
            if not head: return False
            head = head.next
        return True

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 1 or not self.isLongerThenK(head, k): return head

        curr = head
        prev = next = None

        for i in range(k):
            if not curr: break
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = self.reverseKGroup(next, k)

        return prev
