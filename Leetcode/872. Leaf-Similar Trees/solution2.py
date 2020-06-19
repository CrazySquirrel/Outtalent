# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []

        def dfs(node, leaves):
            if not node: return
            if not node.left and not node.right: leaves.append(node.val)
            if node.left: dfs(node.left, leaves)
            if node.right: dfs(node.right, leaves)

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        if len(leaves1) != len(leaves2): return False

        for i1, i2 in zip(leaves1, leaves2):
            if i1 != i2: return False

        return True
