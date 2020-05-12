# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        curr_level = [(root, None, None)]
        result = 0
        while curr_level:
            next_level = []
            for (node, parent, grandparent) in curr_level:
                if grandparent and grandparent.val % 2 == 0:
                    result += node.val
                if node.left:
                    next_level.append((node.left, node, parent))
                if node.right:
                    next_level.append((node.right, node, parent))
            curr_level = next_level
        return result
