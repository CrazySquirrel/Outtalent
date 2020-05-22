# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val != root2.val: return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)