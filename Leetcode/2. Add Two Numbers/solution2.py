# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head = ListNode()
        carry = 0
        while l1 or l2:
            if l1: carry, l1 = carry + l1.val, l1.next
            if l2: carry, l2 = carry + l2.val, l2.next
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10
        if carry: head.next = ListNode(carry)
        return result.next
