# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, S: int):
            if not node: return 0
            S = S * 10 + node.val
            if not node.left and not node.right: return S
            return dfs(node.left, S) + dfs(node.right, S)

        return dfs(root, 0)
