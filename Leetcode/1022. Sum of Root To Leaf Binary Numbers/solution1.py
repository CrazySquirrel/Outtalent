# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root: return 0

        def dfs(node: TreeNode, pref: int) -> int:
            pref = (pref << 1) | node.val
            if not node.left and not node.right: return pref
            if node.left and node.right: return dfs(node.left, pref) + dfs(node.right, pref)
            if node.left: return dfs(node.left, pref)
            if node.right: return dfs(node.right, pref)

        return dfs(root, 0)
