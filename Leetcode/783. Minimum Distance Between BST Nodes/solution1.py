# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root: return 0

        node = root
        nodes = []
        prev = None
        result = inf

        while True:
            while node is not None:
                nodes.append(node)
                node = node.left

            if nodes:
                node = nodes.pop()
                if prev is not None: result = min(result, abs(node.val - prev))
                prev = node.val
                node = node.right
            else:
                break

        return result
