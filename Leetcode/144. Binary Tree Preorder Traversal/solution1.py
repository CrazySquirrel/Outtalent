# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []

        def traverse(node: TreeNode):
            if node is None: return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return result
