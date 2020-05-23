# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        try:
            def helper(node):
                if not node: return 0

                left_depth = helper(node.left) if node.left else 0
                right_depth = helper(node.right) if node.right else 0

                if abs(left_depth - right_depth) > 1: raise StopIteration()

                return 1 + max(left_depth, right_depth)

            helper(root)

            return True
        except StopIteration:
            return False
