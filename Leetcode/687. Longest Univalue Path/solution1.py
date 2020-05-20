# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestPath(self, root: TreeNode, val: int) -> int:
        if not root or root.val != val: return 0
        return 1 + max(self.longestPath(root.left, val), self.longestPath(root.right, val))

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        result = self.longestPath(root.left, root.val) + self.longestPath(root.right, root.val)
        result = max(result, self.longestUnivaluePath(root.left))
        result = max(result, self.longestUnivaluePath(root.right))
        return result
