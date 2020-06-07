# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, sum: int) -> int:
        if not node: return 0
        res = 1 if node.val == sum else 0
        res += self.dfs(node.left, sum - node.val)
        res += self.dfs(node.right, sum - node.val)
        return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
