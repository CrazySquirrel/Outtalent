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

        if L <= root.val <= R:
            result += root.val

        if L <= root.val:
            result += self.rangeSumBST(root.left, L, R)

        if root.val <= R:
            result += self.rangeSumBST(root.right, L, R)

        return result
