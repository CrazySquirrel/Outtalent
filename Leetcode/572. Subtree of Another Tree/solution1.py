# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s and (self.isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
