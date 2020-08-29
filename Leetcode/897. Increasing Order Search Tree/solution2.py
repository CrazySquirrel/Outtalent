# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return None

        def inorder(node: TreeNode):
            nonlocal curr
            if node.left: inorder(node.left)
            node.left = None
            curr.right = node
            curr = curr.right
            if node.right: inorder(node.right)

        result = curr = TreeNode(None)

        inorder(root)

        return result.right
