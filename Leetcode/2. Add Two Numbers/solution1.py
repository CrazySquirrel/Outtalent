# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return ListNode(0)
        if not l1: return l2
        if not l2: return l1

        result = tmp = ListNode()
        cerry = 0

        while l1 and l2:
            v = l1.val + l2.val + cerry
            l1 = l1.next
            l2 = l2.next
            tmp.next = ListNode(v % 10)
            tmp = tmp.next
            cerry = v // 10

        while l1:
            v = l1.val + cerry
            l1 = l1.next
            tmp.next = ListNode(v % 10)
            tmp = tmp.next
            cerry = v // 10

        while l2:
            v = l2.val + cerry
            l2 = l2.next
            tmp.next = ListNode(v % 10)
            tmp = tmp.next
            cerry = v // 10

        if cerry > 0:
            tmp.next = ListNode(cerry)

        return result.next

