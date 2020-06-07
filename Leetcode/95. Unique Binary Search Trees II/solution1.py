# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, s, e):
        result = []
        for i in range(s, e + 1):
            for l in self.helper(s, i - 1):
                for r in self.helper(i + 1, e):
                    result.append(TreeNode(i, left=l, right=r))
        return result or [None]

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n) if n > 0 else []
