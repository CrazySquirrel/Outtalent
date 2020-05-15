# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0

        result = 0

        curr_nodes = [root]

        while curr_nodes:
            next_nodes = []

            for node in curr_nodes:
                if L <= node.val <= R:
                    result += node.val

                if L <= node.val and node.left:
                    next_nodes.append(node.left)

                if node.val <= R and node.right:
                    next_nodes.append(node.right)

            curr_nodes = next_nodes

        return result
