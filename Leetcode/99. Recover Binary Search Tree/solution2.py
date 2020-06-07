# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        node = root
        first = second = pre = None

        while nodes or node:
            while node:
                nodes.append(node)
                node = node.left

            node = nodes.pop()

            if pre and node.val < pre.val:
                second = node

                if first: break

                first = pre

            pre = node
            node = node.right

        first.val, second.val = second.val, first.val
