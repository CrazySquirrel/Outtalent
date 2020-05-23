# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lA = lB = 0

        tmpA, tmpB = headA, headB

        while tmpA or tmpB:
            if tmpA:
                tmpA = tmpA.next
                lA += 1
            if tmpB:
                tmpB = tmpB.next
                lB += 1

        tmpA, tmpB = headA, headB

        while lA != lB:
            if lA > lB:
                tmpA = tmpA.next
                lA -= 1
            else:
                tmpB = tmpB.next
                lB -= 1

        while tmpA and tmpB:
            if tmpA == tmpB: return tmpA
            tmpA = tmpA.next
            tmpB = tmpB.next

        return None
