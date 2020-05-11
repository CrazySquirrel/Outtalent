# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0
    max_summ = 0

    def helper(self, root: TreeNode, depth: int) -> None:
        if not root: return

        if root.left or root.right:
            self.helper(root.left, depth + 1)
            self.helper(root.right, depth + 1)
        elif Solution.max_depth == depth:
            Solution.max_summ += root.val
        elif Solution.max_depth < depth:
            Solution.max_depth = depth
            Solution.max_summ = root.val

    def deepestLeavesSum(self, root: TreeNode) -> int:
        Solution.max_depth = 0
        Solution.max_summ = 0
        self.helper(root, 0)
        return Solution.max_summ
