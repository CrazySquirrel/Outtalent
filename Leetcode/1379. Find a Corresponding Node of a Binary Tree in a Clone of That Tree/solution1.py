# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not target or not original or not cloned: return None
        if target.val == original.val == cloned.val: return cloned
        node = self.getTargetCopy(original.left, cloned.left, target)
        if node: return node
        node = self.getTargetCopy(original.right, cloned.right, target)
        if node: return node
        return None
