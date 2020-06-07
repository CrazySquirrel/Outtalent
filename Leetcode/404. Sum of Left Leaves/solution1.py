# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode, is_left: bool) -> int:
        if not node: return 0
        if not node.left and not node.right: return node.val if is_left else 0
        return self.helper(node.left, True) + self.helper(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        return self.helper(root.left, True) + self.helper(root.right, False)
