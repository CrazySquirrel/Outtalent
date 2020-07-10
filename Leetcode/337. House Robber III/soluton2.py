# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node: return 0, 0
            lrob, lnorob = dfs(node.left)
            rrob, rnorob = dfs(node.right)
            rob = lnorob + rnorob + node.val
            norob = max(lrob, lnorob) + max(rrob, rnorob)
            return rob, norob

        return max(dfs(root))
