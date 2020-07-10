# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dfs(node: TreeNode, parent: bool) -> int:
            if not node: return 0
            result = dfs(node.left, True) + dfs(node.right, True)
            if parent: result = max(result, node.val + dfs(node.left, False) + dfs(node.right, False))
            return result

        return dfs(root, True)
