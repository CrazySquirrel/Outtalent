# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        nodes = [root]
        result = 0
        while nodes:
            tmp = []
            for node in nodes:
                result += 1
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            nodes = tmp
        return result
