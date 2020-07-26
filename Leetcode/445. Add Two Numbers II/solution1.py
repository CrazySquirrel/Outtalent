# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toStack(l: ListNode) -> List[ListNode]:
            stack = []
            while l:
                stack.append(l)
                l = l.next
            return stack

        def addNode(v: int):
            nonlocal head
            temp = head
            head = ListNode(v)
            head.next = temp

        stack_l1 = toStack(l1)
        stack_l2 = toStack(l2)

        carry = 0
        head = None

        while stack_l1 or stack_l2:
            v1 = stack_l1.pop().val if stack_l1 else 0
            v2 = stack_l2.pop().val if stack_l2 else 0

            carry, v = divmod(v1 + v2 + carry, 10)

            addNode(v)

        if carry: addNode(carry)

        return head
