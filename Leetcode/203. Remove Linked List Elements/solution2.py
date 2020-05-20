# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = node = ListNode(inf, head)

        while node:
            while node.next and node.next.val == val: node.next = node.next.next
            node = node.next

        return result.next
