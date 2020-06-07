# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def h(s, e):
            return [TreeNode(i, left=l, right=r) for i in range(s, e + 1) for l in h(s, i - 1) for r in h(i + 1, e)] or [None]

        return h(1, n) if n > 0 else []
