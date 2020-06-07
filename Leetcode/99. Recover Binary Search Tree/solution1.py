# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first: self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
