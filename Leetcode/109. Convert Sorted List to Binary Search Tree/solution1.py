# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size, tmp = 0, head
        while tmp: size, tmp = size + 1, tmp.next

        def convert(l, r):
            nonlocal head
            if l > r: return None
            m = l + (r - l) // 2
            left = convert(l, m - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(m + 1, r)
            return node

        return convert(0, size - 1)
