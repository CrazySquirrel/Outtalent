from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        nodes = deque([(1, root)])
        while nodes:
            depth, node = nodes.popleft()
            if not node.left and not node.right: return depth
            if node.left: nodes.append((depth + 1, node.left))
            if node.right: nodes.append((depth + 1, node.right))
