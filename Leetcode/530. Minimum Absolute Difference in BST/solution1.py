# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root: return -inf

        prev = -inf
        result = inf

        node = root
        nodes = []

        while True:
            while node:
                nodes.append(node)
                node = node.left

            if nodes:
                node = nodes.pop()
                result = min(result, abs(prev - node.val))
                prev = node.val
                node = node.right
            else:
                break

        return result
