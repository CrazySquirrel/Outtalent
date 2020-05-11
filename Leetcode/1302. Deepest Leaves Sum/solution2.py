# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        prev = []
        curr = [root]

        while curr:
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            prev, curr = curr, next

        return sum(node.val for node in prev)
