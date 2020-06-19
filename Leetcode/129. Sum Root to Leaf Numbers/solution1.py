# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        result = 0

        def dfs(node: TreeNode, path: int):
            nonlocal result

            if not node.left and not node.right:
                result += path * 10 + node.val
            else:
                if node.left: dfs(node.left, path * 10 + node.val)
                if node.right: dfs(node.right, path * 10 + node.val)

        dfs(root, 0)

        return result
