# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toInt(l: ListNode) -> int:
            result = 0
            while l:
                result = result * 10 + l.val
                l = l.next
            return result

        dummy = ListNode(0)
        temp = dummy

        for c in str(toInt(l1) + toInt(l2)):
            temp.next = ListNode(int(c))
            temp = temp.next

        return dummy.next
