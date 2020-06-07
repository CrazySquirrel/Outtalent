# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, sum: int) -> int:
        res = 1 if node.val == sum else 0
        if node.left:
            res += self.dfs(node.left, sum - node.val)
        if node.right:
            res += self.dfs(node.right, sum - node.val)
        return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        result = 0
        nodes = []
        nodes.append(root)
        while nodes:
            node = nodes.pop()
            result += self.dfs(node, sum)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
        return result
