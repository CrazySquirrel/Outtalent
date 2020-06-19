# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []

        def dfs(node: TreeNode, target: int, prefix: List[int]):
            prefix.append(node.val)
            if not node.left and not node.right:
                if node.val == target: result.append(list(prefix))
            else:
                if node.left: dfs(node.left, target - node.val, prefix)
                if node.right: dfs(node.right, target - node.val, prefix)
            prefix.pop()

        result = []

        dfs(root, sum, [])

        return result
