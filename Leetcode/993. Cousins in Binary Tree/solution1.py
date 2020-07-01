# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False

        nodes = [(root, 0, None)]
        node_x = node_y = None

        while nodes:
            tmp = []

            for node, depth, parent in nodes:
                if node.val == x: node_x = (depth, parent)
                if node.val == y: node_y = (depth, parent)
                if node.left: tmp.append((node.left, depth + 1, node))
                if node.right: tmp.append((node.right, depth + 1, node))

            if node_x or node_y:
                return node_x and node_y and node_x[0] == node_y[0] and node_x[1] != node_y[1]

            nodes = tmp

        return False
