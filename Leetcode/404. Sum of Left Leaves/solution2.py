# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        nodes = [(root, False)]
        result = 0
        while nodes:
            node, is_left = nodes.pop()
            if not node.left and not node.right and is_left:
                result += node.val
            if node.left:
                nodes.append((node.left, True))
            if node.right:
                nodes.append((node.right, False))
        return result
