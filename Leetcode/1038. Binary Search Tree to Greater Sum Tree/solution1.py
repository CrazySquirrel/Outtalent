# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    summ = 0

    def helper(self, root: TreeNode) -> TreeNode:
        if not root: return None

        root.right = self.helper(root.right)

        Solution.summ += root.val
        root.val = Solution.summ

        root.left = self.helper(root.left)

        return root

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return None

        Solution.summ = 0

        return self.helper(root)
