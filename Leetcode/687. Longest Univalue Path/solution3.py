# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0

        result = [0]

        def helper(node, val):
            left = helper(node.left, node.val) if node.left else 0
            right = helper(node.right, node.val) if node.right else 0
            result[0] = max(result[0], left + right)
            return 1 + max(left, right) if node.val == val else 0

        helper(root, None)

        return result[0]
