# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return False

        val = root.val
        nodes = [root]

        while nodes:
            node = nodes.pop()
            if node.val != val: return False
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)

        return True
