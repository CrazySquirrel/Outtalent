# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = curr_head = ListNode()
        p, q = l1, l2

        carry = 0

        while p or q:
            if p:
                carry += p.val
                p = p.next

            if q:
                carry += q.val
                q = q.next

            curr_head.next = ListNode(carry % 10)
            curr_head = curr_head.next
            carry //= 10

        if carry > 0:
            curr_head.next = ListNode(carry)

        return dummy_head.next
