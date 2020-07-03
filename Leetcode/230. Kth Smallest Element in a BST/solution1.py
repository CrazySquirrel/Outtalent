# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node: TreeNode):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return inorder(root)[k - 1]
