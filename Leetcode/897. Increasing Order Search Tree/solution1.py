# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        if root.left: root.left = self.increasingBST(root.left)
        if root.right: root.right = self.increasingBST(root.right)
        if not root.left: return root
        result = root.left
        root.left = None
        tmp = result
        while tmp.right: tmp = tmp.right
        tmp.right = root
        return result
