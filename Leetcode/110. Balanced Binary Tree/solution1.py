# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode):
        if not root: return 0

        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)

        if left_depth == None or right_depth == None: return None
        if abs(left_depth - right_depth) > 1: return None

        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != None
