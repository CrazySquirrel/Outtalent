# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        level = [root]
        depth = 0
        while level:
            depth += 1
            new_level = []
            for node in level:
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            level = new_level
        return depth
