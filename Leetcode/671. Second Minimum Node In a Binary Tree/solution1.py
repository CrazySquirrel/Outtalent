# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1

        result = inf
        m = root.val

        def dfs(node):
            nonlocal result, m
            if m < node.val < result:
                result = node.val
            elif node.val == m:
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)

        dfs(root)

        return result if result < inf else -1
