# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(node: TreeNode) -> int:
            nonlocal result
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)
            result = max(result, left + right + 1)
            return max(left, right) + 1

        result = 1

        helper(root)

        return result - 1
