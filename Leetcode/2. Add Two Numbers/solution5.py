# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head = ListNode()
        carry = 0

        while l1 and l2:
            carry, l1 = carry + l1.val, l1.next
            carry, l2 = carry + l2.val, l2.next
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10

        l3 = l1 if l1 else l2

        while l3:
            carry += l3.val
            if carry > 9:
                l3 = l3.next
                head.next = ListNode(carry % 10)
                head = head.next
                carry //= 10
            else:
                l3.val = carry
                head.next = l3
                break
        else:
            if carry: head.next = ListNode(carry)

        return result.next
