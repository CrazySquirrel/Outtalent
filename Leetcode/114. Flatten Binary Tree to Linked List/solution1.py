# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        if root.right: self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            l, r = root.left, root.right
            root.left, root.right = None, l
            while l.right: l = l.right
            l.right = r
