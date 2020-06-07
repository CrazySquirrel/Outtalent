# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def helper(node):
            if not node or not node.next: return node
            X = node.val
            if node.next.val == X:
                while node and node.val == X: node = node.next
                return helper(node)
            else:
                node.next = helper(node.next)
                return node

        dummy = ListNode(None, next=helper(head))
        return dummy.next
