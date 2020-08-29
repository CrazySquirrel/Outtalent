# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return -1

        nodes = [(root, 0)]
        levels = []

        while nodes:
            node, level = nodes.pop()

            if level == len(levels):
                levels.append(node.val)
            else:
                levels[level] += node.val

            if node.left: nodes.append((node.left, level + 1))
            if node.right: nodes.append((node.right, level + 1))

        maxLevel = 0
        maxValue = levels[0]

        for level, value in enumerate(levels):
            if value > maxValue:
                maxValue = value
                maxLevel = level

        return maxLevel + 1
