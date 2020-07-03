# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            result.append(node.val)
            if node.right: nodes.append(node.right)
            if node.left: nodes.append(node.left)
        return result
