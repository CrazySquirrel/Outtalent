# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root
