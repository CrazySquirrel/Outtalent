# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode):
        if node.left: yield from self.helper(node.left)
        yield node.val
        if node.right: yield from self.helper(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return list(self.helper(root))
