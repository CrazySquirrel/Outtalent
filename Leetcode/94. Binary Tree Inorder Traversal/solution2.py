# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []
        nodes = []
        node = root
        while node or nodes:
            while node:
                nodes.append(node)
                node = node.left
            node = nodes.pop()
            result.append(node.val)
            node = node.right
        return result
