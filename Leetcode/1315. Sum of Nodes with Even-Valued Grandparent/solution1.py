# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode, parent: TreeNode, grandparent: TreeNode) -> int:
        if not node: return 0

        result = node.val if grandparent and grandparent.val % 2 == 0 else 0

        return result + self.helper(node.left, node, parent) + self.helper(node.right, node, parent)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root, None, None)
