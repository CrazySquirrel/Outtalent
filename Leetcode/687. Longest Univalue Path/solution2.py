# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode, val: int) -> int:
        if not root: return 0

        left = self.helper(root.left, root.val)
        right = self.helper(root.right, root.val)

        self.result = max(self.result, left + right)

        if root.val == val:
            return 1 + max(left, right)
        else:
            return 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        self.helper(root, None)
        return self.result
