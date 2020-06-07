# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None: return 0

        def helper(node):
            nonlocal result
            v = node.val
            l = helper(node.left) if node.left else 0
            r = helper(node.right) if node.right else 0
            result = max(result, v, v + l, v + r, v + l + r)
            return max(v, l + v, r + v)

        result = root.val
        helper(root)
        return result
