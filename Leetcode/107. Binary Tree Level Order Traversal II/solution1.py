# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = [[root]]
        i = 0
        while i < len(result):
            level = []
            for node in result[-1]:
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            if level: result.append(level)
            i += 1
        return [[node.val for node in level] for level in result[::-1]]
